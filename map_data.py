
import streamlit as st
import plotly.express as px
from streamlit_plotly_events import plotly_events
import pandas as pd
import plotly.graph_objects as go
import os
from PIL import Image
import csv


#@st.cache_data
def load_substations():
    data_substations = pd.read_csv("substations.csv") # this is actually a datafrom not data-object
    return data_substations
    
data_substations = load_substations()
#st.write(data_substations)
#st.write(type(data_substations))

#@st.cache_data
def load_lines(data_substations):
    #data = pd.read_csv("lines.csv")
    lines = []
    with open("lines.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lines.append(row)
    #return lines
    
    with open("links.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
        
            name0 = data_substations[data_substations['Bus'] == row['bus0']]
            name1 = data_substations[data_substations['Bus'] == row['bus1']]
            
            #st.write(type(name0))
            #st.write(type(name1))
            
            if name0.empty:
                first_element = row['bus0'].split("_")[0]
                #st.write(type(first_element))
                name0 = data_substations[data_substations['Bus'].str.contains(first_element)]
            
                if name0.empty:
                    st.write(row['bus0'] + "not found")
                    exit()
            
            if name1.empty:
                first_element = row['bus1'].split("_")[0]
                #st.write(type(first_element))
                name1 = data_substations[data_substations['Bus'].str.contains(first_element)]
                st.write(name1)
            
                if name1.empty:
                    st.write(row['bus1'] + "not found")
                    exit()
            
            line = {
                "Line": row['Link'], 
                "substation_0": name0['name'].values[0], 
                "substation_1": name1['name'].values[0],
                "Voltage [kV]": "HVDC",
                }
            lines.append(line)
    
    #st.dataframe(lines)
    #exit()
    
    for line in lines:
        #print(line)
        line['lon'] = [0,1]
        line['lat'] = [50,51]
        line['color'] = "white"
        
        lat0 = data_substations[data_substations['name'] == line['substation_0']]['latitude']
        lat1 = data_substations[data_substations['name'] == line['substation_1']]['latitude']
        
        if not lat0.empty:
            line['lat0'] = lat0.values[0]
        else:
            #print(lat0)
            print(line['substation_0'])
            st.write(line['substation_0'])
            continue
        
        if not lat1.empty:
            line['lat1'] = lat1.values[0]
        else:
            #print(lat0)
            print(line['substation_1'])
            continue
        #exit()
        
        lon0 = data_substations[data_substations['name'] == line['substation_0']]['longitude']
        lon1 = data_substations[data_substations['name'] == line['substation_1']]['longitude']

        if not lon0.empty:
            line['lon0'] = lon0.values[0]
        else:
            # If the substation is not found in the DataFrame, you may want to handle this case accordingly
            print("Substation 0 not found:", line['substation_0'])
            continue

        if not lon1.empty:
            line['lon1'] = lon1.values[0]
        else:
            # If the substation is not found in the DataFrame, you may want to handle this case accordingly
            print("Substation 1 not found:", line['substation_1'])
            continue
            
        line['lat'] = [line['lat0'], line['lat1']]
        line['lon'] = [line['lon0'], line['lon1']]
        
        if "220" in line['Line']:
            line['color'] = "green"
        if "HVDC" in line['Line'] or line['Voltage [kV]'] == "HVDC":
            line['color'] = "purple"
        if "275" in line['Line']:
            line['color'] = "orange"
            
        if line['Voltage [kV]'] == "275.0":
            line['color'] = "orange"
            #st.write(line['Line'])
            
        if line['Voltage [kV]'] == "220.0":
            line['color'] = "green"
            #st.write(line['Line'])
            
        if line['Voltage [kV]'] == "400.0" or line['Voltage [kV]'] == "380.0":
            line['color'] = "red"
            #st.write(line['Line'])
        
        if line['color'] == "white":
            st.write("unkown voltage" + line['Line'])
        
    return lines;
    
    
data_lines = load_lines(data_substations)
