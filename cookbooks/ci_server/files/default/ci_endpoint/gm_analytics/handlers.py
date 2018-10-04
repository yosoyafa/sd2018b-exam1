import os
import requests
import json
from fabric import Connection
from flask import request

def manage_pullrequest():
    update = request.get_data().decode('utf8')
    updateJSON = json.load(update)
    pr = jsonFile["pull_request"]["head"]["sha"]
    url = 'https://raw.githubusercontent.com/yosoyafa/sd2018b-exam1/' + pr + '/packages.json'
    content = request.get(url)
    packages_json = json.loads(response.content)

    for a in content:

        package = a
        ic = package[installation_commands]

        for command in ic:

            Connection('vagrant@192.168.131.103').run('sudo yum install --downloadonly --downloaddir=/var/repo' + command)

    out = {'command_return': '1'}
return out
