import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load data from URL
url = 'https://raw.githubusercontent.com/plotly/datasets/master/globe_contours.csv'
df = pd.read_csv(url)

# Function to unpack columns
def unpack(df, key):
    return df[key].dropna()

# Color scale
scl = [
    'rgb(213,62,79)', 'rgb(244,109,67)', 'rgb(253,174,97)',
    'rgb(254,224,139)', 'rgb(255,255,191)', 'rgb(230,245,152)',
    'rgb(171,221,164)', 'rgb(102,194,165)', 'rgb(50,136,189)'
]

# Prepare data for plotting
data = []
for i in range(1, len(scl)):
    lat = unpack(df, f'lat-{i}')
    lon = unpack(df, f'lon-{i}')
    data.append(
        go.Scattergeo(
            lon=lon,
            lat=lat,
            mode='lines',
            line=dict(width=2, color=scl[i])
        )
    )

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
    st.write("selected")
else:
    st.write('click')