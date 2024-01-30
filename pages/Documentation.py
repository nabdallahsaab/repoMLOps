### Import


import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
# Cach data @st.cache_data


### Config
st.set_page_config(page_title="Streamlit Page",page_icon="✨",layout="wide",initial_sidebar_state="expanded")

### Title et markdown : st.title et st.markdown
st.title("My Streamlit App")




## test api
components.html(
    """<iframe scrolling="yes"
  id="inlineFrameExample"
  title="Inline Frame Example"
  width="1200"
  height="2000"
  src="https://api-brest-isen-8f7979410f0b.herokuapp.com/docs">
</iframe>
    """,height=6000
)
### Forms st.form, st.form_submit_button et st.select_slider



### Columns st.columns



### Graphique Histogramme avec matplotlib.pyplot, seaborn et st.pyplot


### Image avec st.image


### Graphique Histogramme px.histogram et st.plotly_chart



### Graphique Pie chart px.pie et st.plotly_chart



### + De graphiques ici : https://plotly.com/python/


