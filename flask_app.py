#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:20:50 2024

@author: maximeb
"""

from flask import Flask
import os
import json


cwd = os.getcwd()
output_file = 'gtfs-rt_converted.json'



app = Flask(__name__)

@app.route("/api")
def get():
    with open('source.txt', 'r') as f:
        source = f.read()

    source = source
    
    os.system(f'gtfs-realtime {source} -o {output_file}')
    
    if os.path.isfile(f'{cwd}/{output_file}'):
        
        with open(f'{cwd}/{output_file}', 'r') as f:
            j = json.load(f)

    return j

if __name__ == "__main__":
    app.run(debug=True)