#!/usr/bin/env python3

import os
import json
import yaml

cookiecutter = json.loads("""{{ cookiecutter | jsonify }}""")

for csv_key, csv_entry_list in cookiecutter['in'].items():
    if "_endpoints" in csv_key:
        # build endpoint entries
        endpoints = dict()
        for csv_entry in csv_entry_list:
            server_name = csv_entry['server_name']
            if server_name not in endpoints.keys():
                endpoints.update({
                    server_name: {
                        'switch_ports': list(),
                        'switches': list()
                    }
                })
            endpoints[server_name]['switch_ports'].append(csv_entry['switch_port'])
            endpoints[server_name]['switches'].append(csv_entry['switch_hostname'])
            # find out if interface is in a port-channel
            if csv_entry['port_channel_mode']:
                endpoints[server_name].update({
                    "port_channel": {
                        "mode": csv_entry['port_channel_mode']
                    }
                })
            # set other parameters
            if csv_entry['switchport_mode']:
                endpoints[server_name].update({
                    "mode": csv_entry['switchport_mode']
                })
            if csv_entry['switchport_vlans']:
                endpoints[server_name].update({
                    "vlans": csv_entry['switchport_vlans']
                })
            if csv_entry['description']:
                endpoints[server_name].update({
                    "description": csv_entry['description']
                })
        # convert endpoints dict to AVD list
        avd_endpoints = {
            csv_key: list()
        }
        for server,adapters in endpoints.items():
            avd_endpoints[csv_key].append({
                "name": server,
                "adapters": [
                    adapters
                ]
            })
        yaml_filename = os.getcwd() + """/group_vars/{{cookiecutter.in.avd.fabric_name}}_ENDPOINTS/"""+ csv_key + '.yml'
        with open(yaml_filename, 'w') as f:
            yaml.dump(avd_endpoints, f)
