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
import pandas as pd

cwd = os.getcwd()
output_file = 'gtfs-rt_converted.json'

st.set_page_config(layout="wide")
st.title('GTFS-RT to JSON')

st.header('Vehicle Positions:')

st.selectbox('Feed type:', ['vehicle', 'tripUpdate', 'alert'], key='selectbox')

feed_type = st.session_state['selectbox']


while True:
    points = []
    string = ''

    os.system(f'gtfs-realtime https://pysae.com/api/v2/groups/Transdev-Cr92/gtfs-rt -o {output_file}')
    
    if os.path.isfile(f'{cwd}/{output_file}'):
        
        with open(f'{cwd}/{output_file}', 'r') as f:
            j = json.load(f)
            
            try:
                for n in j['entity']:

                    if f'{feed_type}' in n.keys():
                        points.append([n['vehicle']['position']['latitude'], n['vehicle']['position']['longitude']])
                df = pd.DataFrame(points, columns=['lat', 'lon'])
                st.map(df)
            
            except:
                for n in j['entity']:
                    if f'{feed_type}' in n.keys():
                        string += str(n) + '\n'
                st.code(string)
            
    sleep(10)
    
    st.rerun()
