"""
Python Solutions Week
Dashboard development
"""

# Imports

import streamlit as st
import pandas_datareader.data as wb
import plotly.graph_objs as go
import yfinance as yf
yf.pdr_override()

### Menu

# Columns
col1, col2 = st.columns([0.9, 0.1])

# Sidebar
st.sidebar.title('Menu')

# Selectbox
companies = ['PETR4.SA', 'AMER3.SA']
selection_ticket = st.sidebar.selectbox('Select the company: ', companies)

col1.title(f'Economic Analysis: {selection_ticket}')

# Slider
selection_range = st.sidebar.slider('Month period: ', 0, 12, 1, key='selection_bar')
selected_range = str(selection_range) + 'mo'

### Images

img = [
    'https://seeklogo.com/images/P/Petrobras-logo-03DABEE0AC-seeklogo.com.png',
    'https://files.tecnoblog.net/wp-content/uploads/2022/02/logo-americanas.png'
]

if selection_ticket == companies[0]:
    col2.image(img[0], width=70)
else:
    col2.image(img[1], width=70)

### Web Scraping

# API
data = wb.get_data_yahoo(selection_ticket, period=selected_range)

# Candlestick
chart_candlestick = go.Figure(
    data=[
        go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close']
        )
    ]
)

chart_candlestick.update_layout(
    xaxis_rangeslider_visible=False,
    xaxis_title='Date',
    yaxis_title='Price [BRL]',
    xaxis={'showgrid': False},
    yaxis={'showgrid': False}
)

st.plotly_chart(chart_candlestick)

# Table
if st.checkbox('Show data in table'):
    st.subheader('Table of Records')
    st.write(data)
