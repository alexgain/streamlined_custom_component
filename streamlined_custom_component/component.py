import streamlit.components.v1 as components
import os

default_html_template = """
<html>
  <head>
    <style>
    {css}
    </style>
  </head>
  <body>
    {html}

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

      var myInput = document.getElementById("{input_id}");

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

      {javascript}
    </script>
  </body>
</html>
"""

def create_component(modifications=None, full_html=None, component_name="custom_component"):
    component_dir = os.path.dirname(__file__)
    component_path = os.path.join(component_dir, component_name)
    
    if not os.path.exists(component_path):
        os.makedirs(component_path)
    
    index_html_path = os.path.join(component_path, "index.html")
    
    if full_html:
        html_content = full_html
    else:
        # Default modifications
        input_id = modifications.get("input_id", "custom_input") if modifications else "custom_input"
        extra_html = modifications.get("html", "") if modifications else ""
        extra_javascript = modifications.get("javascript", "") if modifications else ""
        extra_css = modifications.get("css", "") if modifications else ""

        html_content = default_html_template.format(
            input_id=input_id,
            html=extra_html,
            javascript=extra_javascript,
            css=extra_css
        )
    
    with open(index_html_path, "w") as f:
        f.write(html_content)
    
    component = components.declare_component(
        component_name,
        path=component_path
    )
    
    return component