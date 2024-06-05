# streamlit run Hello.py

import streamlit as st
import plotly.express as px
from streamlit_plotly_events import plotly_events
import pandas as pd
import plotly.graph_objects as go
import os
from PIL import Image
import csv

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

from map_data import data_substations
from map_data import data_lines

#st.dataframe(data_substations)

#print(data_lines[0]);
#exit();    

#data_lines = []
#data_lines.append({'Line':'Test','lon':[0,1],'lat':[50,51]})
#data_lines.append({'Line':'Test 2','lon':[5,6],'lat':[56,57]})
    

debug_table_lines = pd.DataFrame(data_lines)
#st.write(debug_table_lines)


# Read the text file
with open("player_id.txt", 'r') as file:
    file_content = file.read()

# Display the file content (optional)
#st.text_area("File Content", file_content, height=200)

# Offer the file for download
#st.download_button(
#    label="Download Text File",
#    data=file_content,
#    file_name='downloaded_textfile.txt',
#    mime='text/plain'
#)


    
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
        padding: 50px;
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
        #display: flex;
        #justify-content: flex-end;
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
    
###################################################################################################
# layout start
###################################################################################################
    
# testbutton = st.button("Test")    
    
    
# Load SVG content from a file
with open("energynautics-logo-st0-moved.svg", "r") as file:
    svg_content = file.read()

# Display the SVG using Streamlit's markdown functionality
#st.markdown(f'<div style="width:200px;text-align:left;">{svg_content}</div>', unsafe_allow_html=True)



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
    
    map_col, loc_col = st.columns([2,1])
    with map_col:
        map_slot = st.empty()
    with loc_col:
        loc_slot = st.empty()
        confirm_slot = st.empty()
    
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
    #data.append(london_marker)

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
    #data.append(london_marker)


    line = go.Scattergeo(lon=[0,1],lat=[50,51],mode='lines',line=dict(width=5))
    #data.append(line)

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
        height=450,  # Height of the figure in pixels   # flickers when using community events and >450 (hardcoded to 450)
    )

    #@st.cache_resource
    def get_fig_with_lines(layout):
    
        # Create figure
        fig = go.Figure(data=data, layout=layout)
        
        for i in range(len(debug_table_lines)):
            fig.add_trace(go.Scattergeo(
                lon=debug_table_lines['lon'][i],
                lat=debug_table_lines['lat'][i],
                #text=debug_table_lines['Line'][i],
                hoverinfo='none',
                #hoveron='skip',
                mode='lines',
                showlegend=False,
                line=dict(
                    width=1,
                    color=debug_table_lines['color'][i],                    
                ),
                opacity=0.5
            )
        )
        
        return fig
        
    #fig = fig = go.Figure(data=data, layout=layout);
    fig = get_fig_with_lines(layout)
    
    
    #print(data_substations['x'])
    
    fig.add_trace(go.Scattergeo(
            lon = data_substations['longitude'],
            lat = data_substations['latitude'],
            text = data_substations['name'],
            mode = 'markers',
            showlegend=False,
            marker = dict(
                size = 3,
                color = 'blue',
                symbol = 'circle'
            ),
            name = "Substation"
        ))
        
    #print("dots")
    #print(data_substations['latitude'])
    
    #print("lines")
    #print(debug_table_lines['lon'])
    
    #fig.add_trace(go.Scattergeo(
    #        lon = debug_table_lines['lon'],
    #        lat = debug_table_lines['lat'],
    #        text = debug_table_lines['Line'],
    #        mode = 'lines',
    #        line = dict(
    #            width = 10,
    #            color = 'red',
    #        )
    #    ))
     

    
     
    #fig.update_traces(marker=dict(size=8), selector=dict(mode='markers'))
    
    fig.update_layout(clickmode='event+select')
    fig.update_layout(dragmode='pan')
    #fig.update_layout(config=dict(modeBarButtonsToRemove=['lasso2d']))
    #fig.update_layout(
    #        updatemenus=[],
    #        annotations=[]
    #    )
    
        
    # Use Streamlit to display the figure
    #st.plotly_chart(fig)
    #selected_data = st.plotly_chart(fig, on_select="rerun", use_container_width=True, config=dict(modeBarButtonsToRemove=['lasso2d', 'select2d', 'toImage']))
        
    def OnSelect():
        st.write("select!")
        print("select!")
        #exit()
        
        
    ################################# MAP #############################    
    ################################# MAP #############################    
    ################################# MAP #############################    
    ################################# MAP #############################    
    ################################# MAP ############################# 
    #with map_col:    
    selected_data = st.plotly_chart(fig, on_select="rerun", key="sel", use_container_width=True, config=dict(modeBarButtonsToRemove=['lasso2d', 'select2d', 'toImage']))
    #plotly_chart(fig, on_select=OnSelect, key="sel", use_container_width=True, config=dict(modeBarButtonsToRemove=['lasso2d', 'select2d', 'toImage']))
    ################################# MAP #############################    
    ################################# MAP #############################    
    ################################# MAP #############################    
    ################################# MAP #############################    
    ################################# MAP #############################    
    
    #exit()
    #selected_data = st.session_state.sel
    
    
    #selected_data = plotly_events(fig, click_event=False, select_event=True, hover_event=False) #key="pe_selected"
    #if selected_data:
        #st.write(selected_data)
        
    from streamlit.elements.lib.event_utils import AttributeDictionary

    #st.write(type(selected_data))
        
    if selected_data and isinstance(selected_data, AttributeDictionary) and selected_data.selection.points:
        #st.write("official event")
        #st.write(selected_data)
        #print(type(selected_data))
        #st.dataframe( selected_data.selection )
        #exit()
        #st.dataframe( selected_data.select["lines"] )
        #st.write(f"selected {selected_data.select['points'][0]['point_index']}")
        
        #if st.button("Confirm"):
        location_id = selected_data.selection['points'][0]['point_index'] + 1
        location_data = data_substations.iloc[location_id - 1]
        location_name = location_data['name']
        #st.dataframe(location_data)
        st.write(location_name)
        
        if st.button("Confirm Location"):
            st.session_state.location_id = location_id
            st.experimental_rerun()
            
        #if st.button('Clear Selection'):
        #    fig.update_traces(selectedpoints=[], selector=dict(name='substation'))
        #    st.write("clered")
        
        exit()
        
    if selected_data and isinstance(selected_data, object):
        #print("Hello")
        #print(selected_data) 
        #st.dataframe(selected_data)
        
        
        #if st.button("Confirm"):
        #st.session_state.location_id = selected_data[0]['pointIndex'] + 1
        #location_name = data_substations.iloc[st.session_state.location_id - 1]['Bus']
        
        #st.experimental_rerun()
        exit()
        
    exit()
    
else:

    #st.write(st.session_state.location_id)
    #st.write(type(data_substations))
    #print(data_substations)
    #exit()
    location_name = data_substations.iloc[st.session_state.location_id - 1]['name']
    #st.write(location_name)
    #exit()
    
    if not st.session_state.clicked_building:
        st.write(f"You decided to build at 📍 Location {location_name}")
        if(st.button("🗺️ Change Location")):
            st.session_state.location_id = None
            st.session_state.started_test = None
            st.experimental_rerun()

if not st.session_state.location_id or not st.session_state.clicked_building:
    exit()
    
    
setups = st.columns(4)
with setups[0]:    
    st.write(f'You decided to build {st.session_state.clicked_building} at 📍 {location_name}')
with setups[1]:    
    if(st.button("♻️ Change Facility")):
        st.session_state.clicked_building = None
        st.session_state.started_test = None
        st.experimental_rerun()
with setups[2]:    
    if(st.button("🗺️ Change Location")):
        st.session_state.location_id = None
        st.session_state.started_test = None
        st.experimental_rerun()
    
    
    
# start gate
if(not st.session_state.started_test):
    if(st.button(f"⚙️ Test {st.session_state.clicked_building} at 📍 {location_name} for 5 days")):
        st.session_state.started_test = True
        st.experimental_rerun()
    exit()
     

###################################################################################################    
st.write("Generating random weather...");
###################################################################################################

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
        sleep(0.01) # 0.05
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
for i in range(score):
    sleep(0.3)
    stars = "";
    for star in range(i + 1):
        stars = stars + "⭐"
    score_board.write(stars)
    
    if i + 1 == score:
        score_board.write(stars + f" ({score})")



sleep(0.5)

# st.write(f"Best {st.session_state.clicked_building} at 📍 Location {st.session_state.location_id}! 🎉🎉🎉");

# st.button("🎲 Roll Weather Again (3 🎲🎲🎲 rerolls remaining)")    







#todo save entire slotmachine into session, so it does not reroll when pressing buttons below or when visiting the same facility and location again

st.write("💡 To improve your score, try a different facility or location!")

#if(st.button("♻️ Change Facility", key="improve_fa")):
#    st.session_state.clicked_building = None
#    st.session_state.started_test = None
#    st.experimental_rerun()
#    exit()
                
#if(st.button("🗺️ Change Location", key="improve_lo")):
#    st.session_state.location_id = None
#    st.session_state.started_test = None
#    st.experimental_rerun()
#    exit()



###################################################################################################
# high scores
###################################################################################################

myhigh, locationhigh = st.columns(2)

my_scores_data = [
    {'score': 7, 'location': 1, 'facility': 5},
    {'score': 9, 'location': 2, 'facility': 3},
    {'score': 5, 'location': 5, 'facility': 2},
    {'score': 3, 'location': 2, 'facility': 1},
]
my_scores_data = []

for data in my_scores_data:
    data['facility'] = buildings[data['facility']]

my_scores_data.append({'score': score, 'location': "📍 " + location_name, 'facility': st.session_state.clicked_building})

location_scores_data = [
    {'score': 7, 'player': 'Player 4', 'location': 1, 'facility': 5},
    {'score': 9, 'player': 'Player 7', 'location': 2, 'facility': 3},
    {'score': 5, 'player': 'Player 5', 'location': 5, 'facility': 2},
    {'score': 3, 'player': 'Player 17', 'location': 2, 'facility': 1},
]

for data in location_scores_data:
    data['facility'] = buildings[data['facility']]
    data.pop('location', None)

location_scores_data.append({'score': score, 'player': f"Player {st.session_state.player_id} (<- This is you)", 'facility': st.session_state.clicked_building})

# If you want to sort in descending order, you can use the reverse parameter
sorted_my_scores_data = sorted(my_scores_data, key=lambda x: x['score'], reverse=True)
sorted_location_scores_data = sorted(location_scores_data, key=lambda x: x['score'], reverse=True)



with myhigh:
    st.write("Your scores so far:")
    st.dataframe(sorted_my_scores_data)
with locationhigh:
    st.write(f"Top 5 scores at 📍 {location_name}:")
    st.dataframe(sorted_location_scores_data)