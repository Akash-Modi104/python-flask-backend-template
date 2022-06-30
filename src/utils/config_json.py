import json
import pathlib
import os


def create_config_json():
    project_path=pathlib.Path(__file__).parent.parent.parent

    with open(os.path.join(project_path,"config","config.json")) as file:
        data = json.load(file)

    with open(os.path.join(project_path,"configs","config.json"), 'w') as f:
        json.dump(data, f, indent=2)
