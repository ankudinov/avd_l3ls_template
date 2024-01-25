#!/usr/bin/env python3

import os
import json
import yaml

avd_endpoints = json.loads("""{{ cookiecutter.out.endpoints | jsonify }}""")

for endpoints_key, endpoints in avd_endpoints.items():
    yaml_filename = os.getcwd() + """/group_vars/{{cookiecutter.in.avd.fabric_name}}_ENDPOINTS/"""+ endpoints_key + '.yml'
    with open(yaml_filename, 'w') as f:
        yaml.dump(endpoints, f)
