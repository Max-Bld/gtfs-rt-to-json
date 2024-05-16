#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:38:21 2024

@author: maximeb
"""

import os
import webbrowser
import subprocess
from time import sleep

os.system('ngrok start --all &')

sleep(3)

if str(subprocess.check_output("curl -s localhost:4040/api/tunnels | jq -r '.tunnels[1].public_url'", shell=True)) == 'http://localhost:5000':
    api_url = str(subprocess.check_output("curl -s localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url'", shell=True))[2:-3]
    app_url = str(subprocess.check_output("curl -s localhost:4040/api/tunnels | jq -r '.tunnels[1].public_url'", shell=True))[2:-3]
else:
    api_url = str(subprocess.check_output("curl -s localhost:4040/api/tunnels | jq -r '.tunnels[1].public_url'", shell=True))[2:-3]
    app_url = str(subprocess.check_output("curl -s localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url'", shell=True))[2:-3]

os.system('python3 flask_app.py &')

os.system(f'streamlit run gtfs_rt_to_json.py --server.headless true {api_url} &')

webbrowser.open(app_url)