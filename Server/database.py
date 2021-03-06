import logging
import os
from configparser import ConfigParser

import mysql.connector as mysql

import config
import sql_commands
from loggerFunctions import info, warning, debug

logger = logging.getLogger("sql")
c = None
conn = None


class NoException(Exception):
    pass


def execute(command, ignore=NoException):
    try:
        result = c.execute(command)
        debug(logger, "Executing", command, "while ignoring", ignore, ". Result was", result)
        return result
    except ignore as e:
        warning(logger, "\n\nIgnored sql command error: ", command, e, "\n")
        return None


def make_new(dev_mode):
    info(logger, "Making new sql")

    if not os.path.exists(os.path.join(config.save_folder, "dbLogin.ini")):
        with open(os.path.join(config.save_folder, "dbLogin.ini"), "w") as f:
            f.write(config.default_db_login)
            f.close()

        info(logger, "Create dbLogin.ini because it was not there or dev_mode was enabled")
        input("Press enter when you have entered the db login details")

    info(logger, "Successfully connected to the database")

    execute(sql_commands.make_new_users_table, ignore=mysql.ProgrammingError)
    execute(sql_commands.make_new_games_table, ignore=mysql.ProgrammingError)

    conn.commit()
    info(logger, "Successfully ran and committed sql")


def check_for_uuid(uuid):
    result = execute(sql_commands.check_for_uuid.format(a=uuid))
    return False if result is None else True


def connect():
    global c, conn

    cp = ConfigParser()
    cp.read(os.path.join(config.save_folder, "dbLogin.ini"))
    sql_login = dict(cp.items("Login"))

    conn = mysql.connect(**sql_login)
    c = conn.cursor()


def stop():
    conn.commit()
    c.close()
    conn.close()
    info(logger, "Successfully closed the connection to the database")
