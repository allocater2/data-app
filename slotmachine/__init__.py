import streamlit.components.v1 as components

def my_component():
    component_func = components.declare_component("my_component", url="http://localhost:3001")
    return component_func()
