import streamlit as st
import plotly.express as px
from backend import get_data


st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

if place:
    # get the data
    data = get_data(place, days)
    if option == 'Temperature':
        temperatures = [item['main']['temp'] for item in data]
        dates = [item['dt_txt'] for item in data]
        labels = {'x': 'Dates', 'y': 'Temperature (C)'}
        figure = px.line(x=dates, y=temperatures, labels=labels)
        st.plotly_chart(figure)
    elif option == 'Sky':
        sky_conditions = [item['weather'][0]['main'] for item in data]
        paths = [f'images/{condition.lower()}.png' for condition in sky_conditions]
        st.image(paths, width=115)

