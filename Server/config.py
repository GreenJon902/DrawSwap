import os
from configparser import ConfigParser


is_in_dev = True

save_folder = "DrawSwapServer"
log_folder = os.path.join(save_folder, "Logs")

Config = ConfigParser()
Config.read(os.path.join(save_folder, "config.ini"))

default = """
[ServerSettings]
port = 42069

[Database]
name = database.db
"""


def make_new():
    with open(os.path.join(save_folder, "config.ini"), "w") as f:
        f.write(default)

    Config.read(os.path.join(save_folder, "config.ini"))
