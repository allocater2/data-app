
import streamlit as st
import plotly.express as px
from streamlit_plotly_events import plotly_events
import pandas as pd
import plotly.graph_objects as go
import os
from PIL import Image

#from ipywidgets import widgets
#import ipywidgets as widgets
#from IPython.display import display


st.set_page_config(page_title='Energynautics App', layout='wide', initial_sidebar_state='collapsed', page_icon=":bar_chart:")

if 'clicked_building' not in st.session_state:
    st.session_state.clicked_building = None
if 'player_id' not in st.session_state:
    st.session_state.player_id = None
if 'location_id' not in st.session_state:
    st.session_state.location_id = None
if 'started_test' not in st.session_state:
    st.session_state.started_test = None
    
def get_new_player_id():
    if os.path.exists('player_id.txt'):
        with open('player_id.txt', 'r') as file:
            last_player_id = int(file.read())
    else:
        last_player_id = 0
        
    with open('player_id.txt', 'w') as file:
        current_player_id = last_player_id + 1
        file.write(str(current_player_id))
        return current_player_id

###################################################################################################

#stHorizontalBlock
    #column
        #stVerticalBlockBorderWrapper
            #garbage
                #stVerticalBlock
    #column
    #column
 #stVerticalBlock 
    #div.st-emotion-cache-1jjmcle
st.markdown("""
    <style>
    
    .block-container
    {
        padding: 30px;
    }
    
    div[data-testid="column"]:has(span) div div div
    {
        gap: 0rem;
    }
    
   
    .element-container:has(#right-align-content) ~ div div 
    {
        display: flex;
        justify-content: flex-end;
    }
    
    .element-container:has(svg) div div
    {
        display: flex;
        justify-content: flex-end;
    }
    
    .element-container:has(#button-after-fill) ~ div div button 
    {
        width: 100%;
    }

/* tests and experiments */

    div.row-widget
    {
        #display: flex;
        #justify-content: flex-end;
    }    
    
    .right-align-container 
    {
        display: flex;
        justify-content: flex-end;
    }

    </style>
    """, unsafe_allow_html=True)
    
    

# Load SVG content from a file
with open("energynautics-logo.svg", "r") as file:
    svg_content = file.read()

# Display the SVG using Streamlit's markdown functionality
#st.markdown(f'<div style="width:200px;text-align:center;">{svg_content}</div>', unsafe_allow_html=True)



#if not st.session_state.player_id:
    #st.session_state.player_id = get_new_player_id()
    #st.write("Logging in...");
    #st.write(f"Welcome Player {st.session_state.player_id}")
    #st.button("Start Game")
    #exit()
    
    
    
col1, col2, col3, col4 = st.columns(4)
with col1:
    
    if not st.session_state.player_id:
        st.session_state.player_id = get_new_player_id()
    #st.write("Logging in...");
        st.write(f"Welcome Player {st.session_state.player_id}")
    #st.button("Start Game")
    #exit()
    else:
        st.write(f"Player {st.session_state.player_id}")
    
with col4:
    #st.markdown('<div class="right-align-container">', unsafe_allow_html=True)
    st.markdown('<span id="right-align-content"></span>', unsafe_allow_html=True)
    exit_button = st.button("🚪 End Game Session")
    #st.markdown('</div>', unsafe_allow_html=True)
            
    if exit_button:
        st.session_state.clicked_building = None
        st.session_state.player_id = None
        st.session_state.location_id = None
        st.experimental_rerun()
        exit()



# Initialize session state to store clicked building
buildings = ["☀️ Solar Power Plant", "🌬️ Wind Farm", "🌋 Geothermal Power Plant", "💧 Hydrolyzer", "🖥️ Serverfarm", "🔥 Industrial Heat Pump"]
    
if not st.session_state.clicked_building:
    st.write("What do you want to build?")

    # Create ten columns for ten buttons
    
    # .row-widget button
    # .e1f1d6gn5 div div div div div div button
    
    
    
    
    columns = st.columns(len(buildings))

        
    # Add a button in each column
    for i, building in enumerate(buildings):
        with columns[i]:
            st.markdown('<span id="button-after-fill"></span>', unsafe_allow_html=True)
            if st.button(building, key=f"button{i}"): #, help="This is a facility"):
                st.session_state.clicked_building = building
                st.experimental_rerun()
            
            #tooltip = "test"
            #st.write(f'<span title="{tooltip}">{building}</span>', unsafe_allow_html=True)   
                
    #exit()
else:
    if not st.session_state.location_id:
        st.write(f"You decided to build {st.session_state.clicked_building}")
        columns = st.columns(1)
        with columns[0]:
            st.markdown('<span id="spacer"></span>', unsafe_allow_html=True)
            if(st.button("♻️ Change Facility")):
                st.session_state.clicked_building = None
                st.session_state.started_test = None
                st.experimental_rerun()
            
            
    
if not st.session_state.location_id:
    
    if st.session_state.clicked_building:
        st.write(f'Where do you want to build {st.session_state.clicked_building}?')
    else:
        st.write(f'Where do you want to build your facility?')
    
    data = []
    #data.append(go.Scatter({'x':[1],'y':[1]}))

    # Add a marker for London
    london_marker = go.Scattergeo(
        lon=[-0.1278],  # Longitude of London
        lat=[51.5074],  # Latitude of London
        mode='markers',
        marker=dict(
            size=10,
            color='red',  # Make the London marker red for visibility
            symbol='circle'
        ),
        name='London',  # Label for the marker
        hoverinfo='name',
    )
    data.append(london_marker)

    # Add a marker for London
    london_marker = go.Scattergeo(
        lon=[-10.1278],  # Longitude of London
        lat=[51.5074],  # Latitude of London
        mode='markers',
        marker=dict(
            size=10,
            color='red',  # Make the London marker red for visibility
            symbol='circle'
        ),
        name='Ireland',  # Label for the marker
        hoverinfo='name',
    )
    data.append(london_marker)


    line = go.Scattergeo(lon=[0,1],lat=[50,51],mode='lines',line=dict(width=5))
    data.append(line)

    # Define layout
    layout = go.Layout(
        geo=dict(
            projection=dict(
                type='azimuthal equal area', # mercator orthographic azimuthal equal area
                rotation=dict(lon=10, lat=50),
                scale=1.5
                ),
            showocean=False,
            #oceancolor='rgb(0, 255, 255)',
            showland=True,
            #landcolor='rgb(230, 145, 56)',
            #showlakes=True,
            #lakecolor='rgb(0, 255, 255)',
            showcountries=True,
            #lonaxis=dict(showgrid=True, gridcolor='rgb(102, 102, 102)'),
            #lataxis=dict(showgrid=True, gridcolor='rgb(102, 102, 102)'),
            scope='europe',
            center=dict(lat=55, lon=10),  # Center on Europe

            landcolor= 'rgb(243,243,243)',
            countrycolor= 'rgb(204,204,204)',
            lakecolor= 'rgb(255, 255, 255)',

            resolution=50,
        )
        ,
        margin=dict(l=0, r=0, t=0, b=0),  # Reducing left, right, and bottom margins
        #width=2000,  # Width of the figure in pixels
        height=500,  # Height of the figure in pixels   
    )

    # Create figure
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(clickmode='event+select')
    #fig.update_layout(dragmode=False)

    # Use Streamlit to display the figure
    #st.plotly_chart(fig)
    selected_data = st.plotly_chart(fig, on_select="rerun", use_container_width=True)

    if selected_data.get('select') != None:
        st.dataframe( selected_data.select["points"] )
        #st.dataframe( selected_data.select["lines"] )
        st.write(f"selected {selected_data.select['points'][0]['curve_number']}")
        st.session_state.location_id = selected_data.select['points'][0]['curve_number'] + 1
        st.experimental_rerun()
        #exit()
        
    exit()
else:
    if not st.session_state.clicked_building:
        st.write(f"You decided to build at 📍 Location {st.session_state.location_id}")
        if(st.button("🗺️ Change Location")):
            st.session_state.location_id = None
            st.session_state.started_test = None
            st.experimental_rerun()

if not st.session_state.location_id or not st.session_state.clicked_building:
    exit()
    
    
setups = st.columns(4)
with setups[0]:    
    st.write(f'You decided to build {st.session_state.clicked_building} at 📍 Location {st.session_state.location_id}')
with setups[1]:    
    if(st.button("♻️ Change Facility")):
        st.session_state.clicked_building = None
        st.session_state.started_test = None
        st.experimental_rerun()
with setups[2]:    
    if(st.button("📍 Change Location")):
        st.session_state.location_id = None
        st.session_state.started_test = None
        st.experimental_rerun()
    
    
    
# start gate
if(not st.session_state.started_test):
    if(st.button(f"⚙️ Test {st.session_state.clicked_building} at 📍 Location {st.session_state.location_id} for 5 days")):
        st.session_state.started_test = True
        st.experimental_rerun()
    exit()
     
    
st.write("Generating random weather...");


#symbols1 = ['🍒', '🍋', '🍊', '🍉', '🍇', '🔔', '⭐'];
symbols1 = ['☀️', '⛅', '🌧️'];
symbols2 = ['🌬️', '💤',];
symbols3 = ['❄️', '🌡️'];

names = {
    '☀️': "Sunny",
    '⛅': "Cloudy",
    '🌬️': "Windy",
    '💤': "Calm",
    '❄️': "Cold",
    '🌧️': "Rainy",
    '🌡️': "Hot",
}

ratings = ['️⚠️ Redipatch', '🚨 Curtailment', '✅ Perfect'];

import random as r
from time import sleep

#print(range(100))

for day in range(5):
    day_slots = st.columns(5)
    with day_slots[0]:
        placeholder1 = st.empty()
    with day_slots[1]:
        placeholder2 = st.empty()
    with day_slots[2]:
        placeholder3 = st.empty()
    with day_slots[3]:
        placeholder4 = st.empty()
    with day_slots[4]:
        placeholder5 = st.empty()

    placeholder1.write(f"Day {day+1}:")

    for i in range(20):
        sleep(0.05) # 0.01 0.05
        sun = symbols1[r.randint(0,len(symbols1) - 1)]
        wind = symbols2[r.randint(0,len(symbols2) - 1)]
        temp = symbols3[r.randint(0,len(symbols3) - 1)]
        #st.write(f"winner: {winner}")
        #st.write(symbols[winner])
        placeholder2.write(f"{sun}{wind}{temp}")

    placeholder3.write(f"{names[sun]} {names[wind]} {names[temp]}")

    rating = ratings[r.randint(0,len(ratings) - 1)]
    placeholder4.write(rating)
    
    #placeholder5.button("🔍 Analyze Scenario", key=f"analyze{day}")

score_column = st.columns(5)
with score_column[0]:
    st.write("Final Score:");
with score_column[1]:
    score_board = st.empty()
    
score = r.randint(3,9)
for day in range(score):
    sleep(0.3)
    stars = "";
    for star in range(day + 1):
        stars = stars + "⭐"
    score_board.write(stars)

sleep(0.5)

st.write(f"Best {st.session_state.clicked_building} at 📍 Location {st.session_state.location_id}! 🎉🎉🎉");

st.button("🎲 Roll Weather Again (3 🎲🎲🎲 rerolls remaining)")    


