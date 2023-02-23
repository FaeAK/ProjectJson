from json import JSONDecodeError
import yaml
import json

def ourprogram(inp_file):
    try:
        with open(inp_file, 'r') as file:
            configuration = json.load(file)
    except JSONDecodeError as file:
        print("json file is not properly defined")
    try:
        with open('text.yaml', 'w') as yaml_file:
            yaml.dump(configuration, yaml_file)
            return "success"
    except FileNotFoundError:
        print("File error")

print(ourprogram('ttext.json'))



