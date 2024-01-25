#!/usr/bin/env python3

import os
import json
import yaml

cookiecutter = json.loads("""{{ cookiecutter | jsonify }}""")

# add endpoint files
for endpoints_key, endpoints in cookiecutter['out']['endpoints'].items():
    yaml_filename = os.getcwd() + """/group_vars/{{cookiecutter.in.avd.fabric_name}}_ENDPOINTS/"""+ endpoints_key + '.yml'
    with open(yaml_filename, 'w') as f:
        yaml.dump(endpoints, f)
