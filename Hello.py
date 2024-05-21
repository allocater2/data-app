# streamlit run Hello.py

import streamlit as st
import plotly.express as px
from streamlit_plotly_events import plotly_events
import pandas as pd
import plotly.graph_objects as go
import os

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





st.markdown("""
    <style>
    
    .element-container:has(#button-after) + div button 
    {
        width: 100%;
    }

    .block-container
    {
        padding: 50px;
    }
    
    <style>
    .right-align-container 
    {
        display: flex;
        justify-content: flex-end;
    }
    </style>

    </style>
    """, unsafe_allow_html=True)
    
    


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
    exit_button = st.button("🚪 End Game Session")
    #st.markdown('</div>', unsafe_allow_html=True)
            
    if exit_button:
        st.session_state.clicked_building = None
        st.session_state.player_id = None
        st.session_state.location_id = None
        st.experimental_rerun()
        exit()



# Initialize session state to store clicked building

if not st.session_state.clicked_building:
    st.write("What do you want to build?")

    # Create ten columns for ten buttons
    buildings = ["☀️ Solar Power Plant", "🌬️ Wind Farm", "🌋 Geothermal Power Plant", "💧 Hydrolyzer", "🖥️ Serverfarm", "🔥 Industrial Heat Pump"]
    
    # .row-widget button
    # .e1f1d6gn5 div div div div div div button
    
    
    
    
    columns = st.columns(len(buildings))

        
    # Add a button in each column
    for i, building in enumerate(buildings):
        with columns[i]:
            st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
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
        st.write(f"You decided to build at Location {st.session_state.location_id}")
        if(st.button("📍 Change Location")):
            st.session_state.location_id = None
            st.experimental_rerun()

if not st.session_state.location_id or not st.session_state.clicked_building:
    exit()
    
    
    
    
st.write(f'You decided to build {st.session_state.clicked_building} at Location {st.session_state.location_id}')
if(st.button("♻️ Change Facility")):
    st.session_state.clicked_building = None
    st.experimental_rerun()
    
if(st.button("📍 Change Location")):
    st.session_state.location_id = None
    st.experimental_rerun()
    
if(st.button(f"🎖️ Start 5 Days Challenge with {st.session_state.clicked_building} at Location {st.session_state.location_id}")):
    st.write("Coming Soon...");
    
