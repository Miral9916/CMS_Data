pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import base64

x=[116352]
y=['Total Patients']

beneficiary = pd.read_csv("benificiary_d.csv")

st.set_page_config(page_title=" CMS Dashboard", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="expanded")
st.markdown(f"<h1 style='text-align: center; color: #35BAE2 ; width:1360px;height : 100px '>CMS Dashboard</h1>",unsafe_allow_html=True)

colors = ["#F57878", "#C70039", "#900C3F"]


with st.sidebar:
    st.markdown(
        '<div style="background-color: #060505; color:black;height: 50px; width: 298px; border-radius: 5px">'
        '<h2 style="text-align: center;color: white">Demographic</h2>'
        '</div>', unsafe_allow_html=True
    )
    #st.markdown(f"<div style='background-color:{colors[0]}; height: 500px; display: flex; justify-content: center; align-items: center;'>"
    a=['All']          
    options1=st.multiselect('Select age', options=['All'] + list(beneficiary['AGE_INTERVAL'].unique().tolist()),default=a)
    options2=st.multiselect('Select Gender', options=['All'] + list(beneficiary['GENDER'].unique().tolist()),default=a)
    options3=st.multiselect('Select Race', options=['All'] + list(beneficiary['RACE'].unique().tolist()),default=a)
    options4=st.multiselect('Select State', options=['All'] + list(beneficiary['STATE'].unique().tolist()),default=a)


    options12=['All'] + list(beneficiary['AGE_INTERVAL'].unique())
    
       

        # Check the filters and update the data frame accordingly
    if 'All' in options1:
             filtered_df = beneficiary
                      
    else:
         filtered_df = beneficiary[beneficiary['AGE_INTERVAL'].isin(options1)]
         x.append(len(filtered_df))
         y.append(options1)
    if 'All' not in options2:
            filtered_df = filtered_df[filtered_df['GENDER'].isin(options2)]
            x.append(len(filtered_df))
            y.append(options2)
    if 'All' not in options3:
            filtered_df = filtered_df[filtered_df['RACE'].isin(options3)]
            x.append(len(filtered_df))
            y.append(options3)
    if 'All' not in options4:
            filtered_df = filtered_df[filtered_df['STATE'].isin(options4)]
            x.append(len(filtered_df))
            y.append(options4)


col1, col2, col3 = st.columns(3)
with col1:
    
    fig = px.histogram(df,
                   x='AGE_INTERVAL',
                   text_auto=True,
                   width=300,
                   title = " Age Base Analysis",
                   height=400
                   

                   )
    st.plotly_chart(fig)


with col2:
     st.write('<style>{}</style>'.format(style), unsafe_allow_html=True)
     value=df.groupby('RACE')['RACE'].count()
     name=df.groupby('RACE')['RACE'].count().index
     fig1 = px.pie(df, values = df.groupby('RACE')["RACE"].count(),names=name,title = "Race Base Analysis", width=400,height = 400)
     fig1.update(layout=dict(title=dict(x=0.1)))
     fig1.update_traces(textposition='inside', textinfo='percent')
     st.plotly_chart(fig1)

     
    


with col3:
    
    value=df.groupby('GENDER')['GENDER'].count()
    name=df.groupby('GENDER')['GENDER'].count().index
    chart1 = px.pie(df, values = value,names=name,title = "Gender Base Analysis",width=400, height = 400)
    chart1.update(layout=dict(title=dict(x=0.1)))
    st.plotly_chart(chart1)
