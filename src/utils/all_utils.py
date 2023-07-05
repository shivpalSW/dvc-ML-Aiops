import yaml
import os

def read_yaml(path_to_ml: str)-> dict:
    with open(path_to_ml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content 

