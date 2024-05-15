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
import pydeck as pdk
import subprocess

# FUNCTIONS

def application(source):
    
    points = []
    string = ''

    os.system(f'gtfs-realtime {source} -o {output_file}')
    
    if os.path.isfile(f'{cwd}/{output_file}'):
        
        with open(f'{cwd}/{output_file}', 'r') as f:
            j = json.load(f)
            
            try:
                for n in j['entity']:

                    if f'{feed_type}' in n.keys():
                        points.append([n['vehicle']['position']['latitude'], n['vehicle']['position']['longitude']])
                df = pd.DataFrame(points, columns=['lat', 'lon'])
                
                st.pydeck_chart(pdk.Deck(
                    map_style=None,
                    initial_view_state=pdk.ViewState(
                        latitude=df['lat'][0],
                        longitude=df['lon'][0],
                        zoom=11,
                        pitch=50,
                    ),
                    layers=[
                    pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=125)
                ],
            ))
            
            except:
                for n in j['entity']:
                    if f'{feed_type}' in n.keys():
                        string += str(n) + '\n'
                st.code(string)
            
    sleep(10)
    if not on:
        return
    else:
        st.rerun()
        application()
        

# VARIABLES

cwd = os.getcwd()
output_file = 'gtfs-rt_converted.json'

# APPLICATION

# st.set_page_config(layout="wide")

st.title('GTFS-RT to JSON Application')

on = st.toggle("Refresh data", value=True)

st.selectbox('Enter the GTFS-RT feed URL:', ('https://pysae.com/api/v2/groups/Transdev-Cr92/gtfs-rt', 
                                             'https://proxy.transport.data.gouv.fr/resource/lemet-metz-gtfs-rt-vehicle-position',
                                             'https://gtfs-rt.infra-hubup.fr/toutenbus/realtime',
                                             'https://zenbus.net/gtfs/rt/poll.proto?dataset=carsud-reunion',
                                             'https://data.montpellier3m.fr/TAM_MMM_GTFSRT/VehiclePosition.pb',
                                             'https://pysae.com/api/v2/groups/porto-vecchio/gtfs-rt',
                                             'https://proxy.transport.data.gouv.fr/resource/bibus-brest-gtfs-rt-vehicle-position',                                             
                                             ), key='input')

st.header('Vehicle Positions, Trip Updates and Alerts:')

st.selectbox('Feed type:', ['vehicle', 'tripUpdate', 'alert'], key='selectbox')

feed_type = st.session_state['selectbox']

source = st.session_state['input']

if source != '':           
    application(source)
    

