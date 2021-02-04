import os
import appdirs

appname = "DrawSwap"
appauthor = "GreenJon902"
version = "Beta-V0.0.1-AA00"
roaming = False

array = {"appname": "DrawSwap",
         "appauthor": "GreenJon902",
         "version": "Beta-V0.0.1-AA00",
         "roaming": False}

AppDirs: appdirs.AppDirs = appdirs.AppDirs(**array)

user_data_dir: str = AppDirs.user_data_dir
kivy_home_dir: str = os.path.join(user_data_dir, "kivy")
config_dir: str = os.path.join(user_data_dir, "config")
code_dir: str = os.path.dirname(os.path.realpath(__file__))
default_user_data_file: str = os.path.join(code_dir, "default_user_data.json")
user_data_file: str = os.path.join(user_data_dir, "user_data.json")
resources_dir: str = os.path.join(code_dir, "Resources")
texture_link_file: str = os.path.join(resources_dir, "textureLink.ini")
kv_language_dir: str = os.path.join(resources_dir, "kv_language")

log_dir: str = AppDirs.user_log_dir

__all__ = ["appname", "appauthor", "version", "roaming",
           "array",
           "user_data_dir", "kivy_home_dir", "config_dir", "code_dir", "default_user_data_file", "user_data_file",
           "log_dir", "resources_dir", "texture_link_file", "kv_language_dir"]
