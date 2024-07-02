# Streamlined Custom Component for Streamlit

Easy way to create bidirectional components for streamlit with no backend setup, just some imports and html strings. Limited to html / css / javascript blocks.

## Installation
```bash
pip install streamlined_custom_component
```

## Usage

There are two main usecases:
(1) Simple: Overwrite a small portion of the boilerplate `index.html`.
(2) Complex: Overwrite the whole `index.html`.


### Simple usage:
```
import streamlit as st
from streamlit_custom_component import create_component

modifications = {
    "input_id": "custom_input_id",
    "html": """<input id="{input_id}" value="" />""",
    "javascript": "console.log('Additional JavaScript');",
    "css": "body { background-color: lightblue; }"
}
my_component = create_component(modifications=modifications)
value = my_component(input_value="hello there")
st.write(f"Component returned: {value}")
```

### Complex usage:
```
# Overwrite the entire index.html
custom_html = """
<html>
  <body>
    <h1>Custom Component</h1>
    <input id="custom_input" value="" />
    <script>
      function sendMessageToStreamlitClient(type, data) {
        var outData = Object.assign({
          isStreamlitMessage: true,
          type: type,
        }, data);
        window.parent.postMessage(outData, "*");
      }

      function init() {
        sendMessageToStreamlitClient("streamlit:componentReady", {apiVersion: 1});
      }

      function setFrameHeight(height) {
        sendMessageToStreamlitClient("streamlit:setFrameHeight", {height: height});
      }

      function sendDataToPython(data) {
        sendMessageToStreamlitClient("streamlit:setComponentValue", data);
      }

      var myInput = document.getElementById("custom_input");

      function onDataFromPython(event) {
        if (event.data.type !== "streamlit:render") return;
        myInput.value = event.data.args.input_value;
      }

      myInput.addEventListener("change", function() {
        sendDataToPython({
          value: myInput.value,
          dataType: "json",
        });
      })

      window.addEventListener("message", onDataFromPython);
      init();

      window.addEventListener("load", function() {
        window.setTimeout(function() {
          setFrameHeight(document.documentElement.clientHeight)
        }, 0);
      });

      setFrameHeight(0);
    </script>
  </body>
</html>
"""
custom_component = create_component(full_html=custom_html, component_name="custom_component_full")
custom_value = custom_component(input_value="hello custom")
st.write(f"Custom component returned: {custom_value}")
```
