import pathlib
import os


def create_init_py():
    project_path=pathlib.Path(__file__).parent.parent.parent

    with open(os.path.join(project_path,"config","init.txt")) as file:
        data = file.read()

    with open(os.path.join(project_path,"application","__init__.py"), 'w') as f:
        f.write(data)

create_init_py()