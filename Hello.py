import streamlit as st
import plotly.express as px
#from ipyplotly import plotly_events
#from ipywidgets import widgets
import ipywidgets as widgets
from IPython.display import display


st.set_page_config(page_title='My Graph App', layout='centered', initial_sidebar_state='expanded', page_icon=":bar_chart:")

# Custom CSS to inject for aligning content within columns
st.markdown("""
<style>
.e1f1d6gn5 {
    align-items: flex-start !important; // does not work
}

.st-emotion-cache-gh2jqd
{
    padding: 3rem 1rem 1rem;
]
</style>
""", unsafe_allow_html=True)

st.write("hello");

# does not render
slider = widgets.IntSlider(value=10, min=0, max=100, step=1, description='Test Slider:')
display(slider)

# low level API
import plotly.graph_objects as go
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='markers', marker=dict(size=[40, 60, 80, 100]))])
fig.update_layout(clickmode='event+select')
#fig.show()
st.plotly_chart(fig)



# Page Navigation
options = ["Home", "Analysis", "Data"]

# Initialize the session state if it doesn't exist
if 'page' not in st.session_state:
    st.session_state.page = "Home"  # Default page
    
#page = st.sidebar.selectbox("Choose a page", ["Home", "Analysis", "Data"])
current_index = options.index(st.session_state.page) if st.session_state.page in options else 0
#page = st.sidebar.radio("Select a page:", ["Home", "Analysis", "Data"], index=current_index)
#st.session_state.page = page

col1, col2, col3 = st.columns(3)

with col1:
    if(st.button("Home")):
        st.session_state.page = "Home"
with col2:
    if(st.button("Analysis")): 
        st.session_state.page = "Analysis"
with col3:
    if(st.button("Data")): 
        st.session_state.page = "Data"
        
if st.session_state.page == "Home":
    # Create a Plotly figure 
    # high level API
    df = px.data.iris()
    dummy_graph = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    dummy_graph.update_layout(clickmode='event+select')
    dummy_graph.update_layout(dragmode='select')
    
    # Display it in a Streamlit app
   
    st.title("# My Streamlit App with a Plotly Chart")
    st.write("This is a simple Streamlit app. Click the fullscreen button at the bottom right to toggle fullscreen mode.")
    select_data = st.plotly_chart(dummy_graph, on_select="rerun")
    st.write(select_data)
    
    if st.button('Analyze Selected Data'):
        st.write("Placeholder for analyzing selected data.")
        selected_data = plotly_events(fig, click_event=True, select_event=True, key="pe_selected")

    
elif st.session_state.page == "Analysis":
    st.title("Analysis Page")
    st.write("This page will show analysis graphs and insights.")
elif st.session_state.page == "Data":
    st.title("Data Page")
    st.write("This page will display data tables and details.")






