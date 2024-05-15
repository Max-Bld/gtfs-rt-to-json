#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:05:39 2024

@author: maximeb
"""

import streamlit as st
import os
from time import sleep
import json

cwd = os.getcwd()
output_file = 'gtfs-rt_converted.json'

st.set_page_config(layout="wide")
st.title('GTFS-RT to JSON')

while True:
    st.empty()
    os.system(f'gtfs-realtime https://pysae.com/api/v2/groups/Transdev-Cr92/gtfs-rt -o {output_file}')
    
    if os.path.isfile(f'{cwd}/{output_file}'):
        
        with open(f'{cwd}/{output_file}', 'r') as f:
            j = json.load(f)
        
        for n in j['entity']:
            if 'vehicle' in n.keys():
                st.write('vehicle')
                display = st.code(n)
            
    sleep(5)
    
    