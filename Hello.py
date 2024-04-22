import streamlit as st
#import plotly.express as px

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
    #df = px.data.iris()
    #dummy_graph = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

    # Display it in a Streamlit app
   
    st.title("# My Streamlit App with a Plotly Chart")
    st.write("This is a simple Streamlit app. Click the fullscreen button at the bottom right to toggle fullscreen mode.")
    st.plotly_chart(dummy_graph)
elif st.session_state.page == "Analysis":
    st.title("Analysis Page")
    st.write("This page will show analysis graphs and insights.")
elif st.session_state.page == "Data":
    st.title("Data Page")
    st.write("This page will display data tables and details.")






