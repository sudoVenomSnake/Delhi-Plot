import streamlit as st
import geopandas as gpd
import plotly.express as px
import pandas as pd

st.set_page_config(layout = 'wide')
st.title("Delhi")

temp = pd.read_csv('Scores.csv')

col1, col2 = st.columns(2)

with col1:
    gjson = gpd.read_file('Delhi.geojson') # center = {'lat': 28.6139, 'lon': 77.2090}, 
    fig = px.choropleth_mapbox(temp, geojson = gjson, center = {'lat': 28.6139, 'lon': 77.1090}, featureidkey = "properties.Dist_Name", color = "Pincode", locations = "District",  mapbox_style = 'carto-darkmatter', color_continuous_scale = "OrRd", range_color = (0, 115), zoom = 8)
    fig.update_layout(margin = {"r" : 0, "t" : 0, "l" : 0, "b" : 0})
    st.plotly_chart(fig, use_container_width = True)

with col2:
    choice = st.selectbox('Select your area - ', options = temp['District'].unique())
    df = pd.read_csv('Delhi_Lawyers_Area.csv')
    st.write(df[df['District'] == choice][['Name', 'YOE', 'Registration Number', 'Mobile No.', 'Address', 'Pincode', 'Age']].sort_values('YOE', ascending = False).reset_index().drop('index', axis = 1).drop_duplicates())