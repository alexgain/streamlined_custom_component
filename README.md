# Streamlined Custom Component for Streamlit

Easy way to create bidirectional components for streamlit with no backend setup, just some imports and html strings.

## Installation
```bash
pip install streamlined_custom_component
```

## Usage

```
from streamlit_custom_component import create_component

html_content = """
<html>
  <body>
    <input id="myinput" value="" />
    <script>
      // ... JavaScript code ...
    </script>
  </body>
</html>
"""

my_component = create_component(html_content)
value = my_component(my_input_value="hello there")
st.write(f"Component returned: {value}")
```
