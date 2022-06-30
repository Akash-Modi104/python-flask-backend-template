import os
import pathlib
from src.utils.file import create_dirs
from src.utils.config_json import create_config_json


class Create_File:
    def __init__(self):
        self.configs_path = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "configs")
        self.application_path = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "application")
        self.controllers = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent,"application","controllers")
        self.database = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent,"application","database")
        self.models = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent,"application","models")
        self.views = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent,"application","views")
        self.utils = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent,"application","utils")
        self.tests = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, "tests")

        create_dirs([self.configs_path,self.application_path,self.controllers,self.database,
                     self.database,self.models,self.views,self.utils,self.tests])
        create_config_json()
