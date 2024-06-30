import streamlit.components.v1 as components
import os

def create_component(html_content, component_name="mycomponent"):
    component_dir = os.path.dirname(__file__)
    component_path = os.path.join(component_dir, component_name)
    
    if not os.path.exists(component_path):
        os.makedirs(component_path)
    
    index_html_path = os.path.join(component_path, "index.html")
    
    with open(index_html_path, "w") as f:
        f.write(html_content)
    
    component = components.declare_component(
        component_name,
        path=component_path
    )
    
    return component