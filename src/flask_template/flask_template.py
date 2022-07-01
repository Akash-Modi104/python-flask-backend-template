import os
import pathlib
from src.utils.file import create_dirs
from src.utils.config_json import create_config_json
from src.utils.create_python_files import create_init_py


class Flask_Backend_Template:
    def __init__(self):
        self.configs_path = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "configs")
        self.application_path = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "application")
        self.controllers = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "application",
                                        "controllers")
        self.database = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "application", "database")
        self.models = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "application", "models")
        self.views = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "application", "views")
        self.utils = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "application", "../utils")
        self.tests = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "tests")

        create_dirs([self.configs_path, self.application_path, self.controllers, self.database,
                     self.database, self.models, self.views, self.utils, self.tests])

    def create_all_files(self):
        create_config_json()
        print("config.json created")
        create_init_py()
        print("__init__.py created")

