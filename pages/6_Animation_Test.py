import streamlit as st
import plotly.express as px
import pandas as pd


#import my_component
#st.write("Here is my custom component:")
#my_component.my_component()

st.markdown("""
    <div id="animation"></div>
    <script>
        const svg = d3.select("#animation").append("svg")
            .attr("width", 500)
            .attr("height", 500);

        svg.append("circle")
            .attr("cx", 250)
            .attr("cy", 250)
            .attr("r", 0)
            .transition()
            .duration(2000)
            .attr("r", 200);
    </script>
""", unsafe_allow_html=True)

df = pd.DataFrame({
    'x': range(100),
    'y': range(100),
    'frame': range(100)
})

fig = px.scatter(df, x='x', y='y', animation_frame='frame', range_x=[0, 100], range_y=[0, 100])
st.plotly_chart(fig)