## Importing Required Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

## Improting CSV File
beneficiary = pd.read_csv("benificiary_d.csv")

## Setting Up Title of Dashboad
st.set_page_config(page_title="Demographic Distribution of CMS Beneficiary Data", layout="wide")
st.markdown(f"<h1 style='text-align: left; color: #00008B; width:1360px; height : 100px '>Demographic Distribution of CMS Beneficiary Data</h1>",unsafe_allow_html=True)

## Filtering Options
with st.sidebar:
    st.markdown(
        '<div style="background-color: #00008B; height: 50px; width: 298px; border-radius: 5px">'
        '<h2 style = "text-align: center; color: white"> Filter </h2>'
        '</div>', unsafe_allow_html=True
    )

    a=['All']          
    options1=st.multiselect('Select age', options=['All'] + list(beneficiary['AGE_INTERVAL'].unique().tolist()),default=a)

    options2=st.multiselect('Select Gender', options=['All'] + list(beneficiary['GENDER'].unique().tolist()),default=a)

    options3=st.multiselect('Select Race', options=['All'] + list(beneficiary['RACE'].unique().tolist()),default=a)


    if 'All' in options1:
             filtered_df = beneficiary
    else:
         filtered_df = beneficiary[beneficiary['AGE_INTERVAL'].isin(options1)]
    
    if 'All' not in options2:
         filtered_df = filtered_df[filtered_df['GENDER'].isin(options2)]
           
    if 'All' not in options3:
            filtered_df = filtered_df[filtered_df['RACE'].isin(options3)]

df = filtered_df.drop_duplicates(subset=["DESYNPUF_ID"], keep='first')
st.dataframe(df)


## Statistics
    
style = """
div[data-testid="metric-value-container"] {
    font-size: 2em;
    font-weight: bold;
    color: #ffffff;
}

div[data-testid="metric-delta-container"] {
    font-size: 2rem;
    font-weight: bold;
}

div[data-testid="metric-container"] {
    background-color: #B0C4DE; ## color of no. of unqiue patient
    border-radius: 10px;
    padding: 2em;
}
"""
st.write('<style>{}</style>'.format(style), unsafe_allow_html=True)
st.metric("Number of Unique Patients",f"{len(df['DESYNPUF_ID'].unique())}")



## Individual Graphs
col1, col2 = st.columns(2)
with col1:
    fig = px.histogram(df,
                   x= 'AGE_INTERVAL',
                   text_auto=True,
                   width=400,
                   title = "Age-wise Distribution",
                   height=400
                   

                   )
    st.plotly_chart(fig)
    
    value=df.groupby('RACE')['RACE'].count()
    name=df.groupby('RACE')['RACE'].count().index
    fig1 = px.pie(df, values = value,names=name,title = "Race-wise Distribution", width=400,height = 400)
    fig1.update(layout=dict(title=dict(x=0.1)))
    fig1.update_traces(textposition='inside', textinfo='percent')
    st.plotly_chart(fig1)    
    
with col2:
     
    value=df.groupby('GENDER')['GENDER'].count()
    name=df.groupby('GENDER')['GENDER'].count().index
    chart1 = px.pie(df, values = value,names=name,title = "Gender-wise Distribution",width=400, height = 400)
    chart1.update(layout=dict(title=dict(x=0.1)))
    st.plotly_chart(chart1)
   
# with col4:
    
#     df['value'] = df['AGE_INTERVAL'].value_counts(normalize=True) * 100
#     fig2 = px.bar(df,
#              x='AGE_INTERVAL',
#              y='value',
#              text='value',
#              width=600,
#              title="Age Base Analysis",
#              height=400)

#     fig2.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

#     fig2.update_layout(xaxis_title='Age Interval', yaxis_title='Percentage'
# )
#     st.plotly_chart(fig2)


