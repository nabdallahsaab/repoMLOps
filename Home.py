### Import


import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import json
# Cach data @st.cache_data


### Config
st.set_page_config(page_title="Streamlit Page",page_icon="✨",layout="wide",initial_sidebar_state="expanded")

### Title et markdown : st.title et st.markdown
st.title("My Streamlit App")

### Checkbox st.checkbox
@st.cache_data
def load_data():
    df=pd.read_csv('train.csv',sep=";")
    df['id'] = range(len(df))
    return df

    return df

df=load_data()

show_dataframe = st.checkbox("Show Dataframe")

# Display the DataFrame if the checkbox is checked
if show_dataframe:
    st.write(df)



with open("all_dict.json") as json_file:
    data=json.load(json_file)
st.write(df.columns)
st.write(data.keys)
### Forms st.form, st.form_submit_button et st.select_slider



### Columns st.columns



### Graphique Histogramme avec matplotlib.pyplot, seaborn et st.pyplot


### Image avec st.image


### Graphique Histogramme px.histogram et st.plotly_chart



### Graphique Pie chart px.pie et st.plotly_chart



### + De graphiques ici : https://plotly.com/python/


