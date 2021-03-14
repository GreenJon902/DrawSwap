import os
import shutil

import config

if __name__ == "__main__":
    if config.is_in_dev:
        print("Dev mode activated")

        shutil.rmtree(config.save_folder)

    make_new = False
    if not os.path.exists(config.save_folder) or make_new:
        print("Save folder is not here, making a new one")

        make_new = True
        os.makedirs(config.save_folder)
        os.makedirs(config.log_folder)
        config.make_new()

    import logger

    logger.rootLogger.info("Starting...")

    import logging

    mainLogger = logging.getLogger("Main")

    from loggerFunctions import info
    from entrance import Entrance
    import sql

    info(mainLogger, "Imported all modules!")

    sql.make_new()

    info(mainLogger, "Starting DrawSwap server!")

    e = Entrance()
    e.start()
    e.accept_incoming_connections()
