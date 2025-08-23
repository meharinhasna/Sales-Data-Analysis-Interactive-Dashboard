# import libery
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import os
import warnings
warnings.filterwarnings('ignore')

# set the page confiygure , page title , page icon , layout
st.set_page_config(page_title="Sales Performance" , page_icon='🛒',layout='wide')

# set  title
st.title(":chart_with_downwards_trend: Sales Performance & Customer Insights Dashboard")
st.markdown("<style>div.block-container{padding-top:3rem;}</style>" , unsafe_allow_html=True)

# uplode data
df = pd.read_csv("data.csv")

# getting min max oder data
col1 , col2 = st.columns((2))
df['Order Date'] = pd.to_datetime(df['Order Date'])
start_date = pd.to_datetime(df['Order Date'].min())
end_date = pd.to_datetime(df['Order Date'].max())
with col1:
    date1 = pd.to_datetime(st.date_input("Start Date" , start_date))
with col2:
    date2 = pd.to_datetime(st.date_input("End Date",end_date))
df = df[(df["Order Date"] >= date1) & (df['Order Date'] <= date2)].copy()	

# Sidebar section for user to apply filters
st.sidebar.header("👇 Choise Filter")

# region filters
region = st.sidebar.multiselect("Select Region", df['Region'].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

# state filters
state = st.sidebar.multiselect("Select State" , df2['State'].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df[df['State'].isin(state)]

# City filter
city = st.sidebar.multiselect("Select City", df3['City'].unique())
if not city:
    df4 = df3.copy()
else:
    df4= df3[df3['City'].isin(city)]


# filter the data based on region and city and state
if not region and not state and not city:
    filter_df = df
elif not state and not city:
    filter_df = df[df['Region'].isin(region)]
elif not region and not state:
    filter_df = df[df['City'].isin(city)]
elif not region and not city:
    filter_df = df[df['State'].isin(state)]
elif city and region :
    filter_df = df3[(df['City'].isin(city) & df3['Region'].isin(region))]
elif city and state :
    filter_df = df3[(df['City'].isin(city) & df3['State'].isin(state))]
elif state and region :
    filter_df = df3[(df['State'].isin(state) & df3['Region'].isin(region))]
elif city :
    filter_df = df3[df['City'].isin(city)]
else:
    filter_df = df3[(df3['City'].isin(city) & df3['State'].isin(state) & df3['Region'].isin(region))]

# Total Sales
current_year = filter_df['Year'].max()
current_month = filter_df[filter_df['Year'] == current_year]['Month'].max()
if current_month == 1:
    prev_month = 12
    prev_year = current_year - 1
else:
    prev_month = current_month - 1
    prev_year = current_year

current_df = filter_df[(filter_df['Year'] == current_year) & (filter_df['Month'] == current_month)] # Present Month data
prev_df = filter_df[(filter_df['Year'] == prev_year) & (filter_df['Month'] == prev_month)] # previous month data
total_sales = current_df['Sales'].sum()# Totall selas 
previous_sales = prev_df['Sales'].sum()# previous month selas 
sales_change = total_sales - previous_sales
 #Sales Card
with st.container():
    sales_icon = "↑" if sales_change >= 0 else "↓"
    sales_color = "#bac365" if sales_change >= 0 else "#FF5555"
    st.markdown(
        """
        <p style="text-align:center; font-weight:600; color:#444;">
        Sales compared to the previous month — increase or decrease.
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div style="background-color:#f1eef1 ; padding:10px; border-radius:8px; text-align:center;">
            <h4 style="color:#000000;">Total Sales</h4>
            <h1 style="color:#21421e;">$ {total_sales:,.0f}</h1>
            <p style="color:{sales_color}; font-size:16px;">{sales_icon} {abs(sales_change):,.0f}</p>
        </div>
        """,
        unsafe_allow_html=True
    
    )

#  categroy and ship mode by sales
c1 , c2 = st.columns((2))
category_monthly_sales = filter_df.groupby(['YearMonth', 'Category'])['Sales'].sum().reset_index()
with c1:
    colors = {
        "Furniture" : "#A2D2FF",
        "Office Supplies"  :  "#CDB4DB",
        "Technology"  : "#C07E98",}
    st.subheader('Category-wise Monthly Sales Trend')
    fig = px.line(category_monthly_sales, x='YearMonth', y='Sales', color='Category',
              color_discrete_map=colors,
              labels={'YearMonth': 'Month', 'Sales': 'Sales Amount', 'Category': 'Category'},
              line_shape='spline')  

    fig.update_layout(xaxis_tickangle=-45, height=500, template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)
with c2:
    colors = {
        "Second Class" : "#A2D2FF",
        "Standard Class"  :  '#CDB4DB',
        "First Class"  : '#FFC8DD',
        'Same Day' : "#C07E98"
    }
    st.subheader('Sales by Ship Mode Over Time')
    fig = px.bar(filter_df,x='YearMonth',  y='Sales',color='Ship Mode', color_discrete_map=colors,
    labels={'YearMonth': 'Year-Month', 'Sales': 'Sales Amount', 'Ship Mode': 'Shipping Mode'},
    barmode='stack')
    st.plotly_chart(fig, use_container_width=True)


#  categroy and ship mode by sales dataset download
cl1 , cl2 = st.columns((2)) 
with cl1:
   with st.expander("Category-wise Monthly Sales Trend Data"):
        st.write(category_monthly_sales )
        csv = category_monthly_sales .to_csv(index=False).encode('utf-8')
        st.download_button("Dowload Data", data = csv,file_name="category_monthly_sales .csv",mime='text/csv',
                       help = 'Click here to download the data as a CSV file')
with cl2:
    with st.expander("Sales by Ship Mode Over Time Data"):
        region = filter_df.groupby(by = "Ship Mode", as_index = False)["Sales"].sum()
        st.write(region) #st.write(region.style.background_gradient(cmap="Oranges"))
        csv = region.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "Sales_by_Ship_Mode_Over_Time.csv", mime = "text/csv",
                        help = 'Click here to download the data as a CSV file')

# create chart by category and seals columns
category_df = filter_df.groupby(by = ['Category'] , as_index = False)['Sales'].sum()
region_df = filter_df.groupby("Region")['Sales'].sum().reset_index()
cols1 , cols2 = st.columns((2))
with cols1:
    colors = {
        "Furniture" : "#A2D2FF",
        "Office Supplies"  :  "#CDB4DB",
        "Technology"  : "#C07E98",}
    st.subheader(" Category wise Sales") 
    fig = px.bar(category_df, x = "Category" , y ='Sales',text="Sales",template="seaborn",color_discrete_map=colors,color='Category')
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig,use_container_width=True, height = 200)
   
with cols2:
    colors = {
        "South" : "#A2D2FF",
        "East"  :  '#CDB4DB',
        "West"  : '#FFC8DD',
        'Central' : "#C07E98"
    }
    st.subheader("Region wise Sales")
    fig = px.pie(region_df , values='Sales',names='Region',hole=0.5,color_discrete_map=colors,color="Region")
    fig.update_traces(text = region_df["Region"], textposition = "outside")
    st.plotly_chart(fig,use_container_width=True)

#  category and seals columns by sales dataset download
cl1 , cl2 = st.columns((2)) 
with cl1:
   with st.expander("Category wise Sales"):
        st.write(category_df)
        csv = category_df.to_csv(index=False).encode('utf-8')
        st.download_button("Dowload Data", data = csv,file_name="Category_wise_Sales.csv",mime='text/csv',
                       help = 'Click here to download the data as a CSV file')
with cl2:
    with st.expander("Region wise Sales"):
        st.write(region_df) #st.write(region.style.background_gradient(cmap="Oranges"))
        csv = region_df.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "Region_wise_Sales.csv", mime = "text/csv",
                        help = 'Click here to download the data as a CSV file')

#time series analysis
filter_df['YearMonth'] = filter_df['Order Date'].dt.to_period("M")
colors = {
    "Consumer" : '#CDB4DB',
    "Corporate" : '#FFC8DD',
    "Home Office" : "#C07E98"}
st.markdown("""<h4 style='text-align: center;'>Time Series Analysis - YearMonth and Segment wise Sales trend</h4>""",unsafe_allow_html=True)
linechart = filter_df.groupby([filter_df['YearMonth'].dt.strftime("%Y : %b"), 'Segment'])['Sales'].sum().reset_index()
plot = px.line(linechart, x = "YearMonth" , y = "Sales",template='gridon', color = 'Segment', color_discrete_map=colors)
#time series analysis data
st.plotly_chart(plot)
with st.expander('Time Series Analysis - YearMonth and Segment wise Sales trend'):
    st.write(linechart.style.background_gradient(cmap='Blues'))
    csv = linechart.to_csv(index=False).encode('utf-8')
    st.download_button('Dowload Data', data = csv, file_name='Time_Series.csv',mime="text/csv",
                       help = 'Click here to download the data as a CSV file')

# segemnt and Ship Mode wise sales 
column1 , column2 = st.columns((2))
colors = {
    "Consumer" : "#E98181",
    "Corporate" : "#BB6969",
    "Home Office" : "#AA3645"}
with column1 :
    
    st.markdown("""<h3 style='text-align: center;'>Sement Wise Sales</h3>""",unsafe_allow_html=True)
    chart1 = px.pie(filter_df,
                    values="Sales",
                    names = "Segment" , color = 'Segment' , color_discrete_map=colors)
    st.plotly_chart(chart1)
colors = {
        "Second Class" : "#FFA2AE",
        "Standard Class"  :  "#C03E53",
        "First Class"  : "#AD7174",
        'Same Day' : "#79172C"
    }
with column2:
    st.markdown("""<h3 style='text-align: center;'>Ship Mode Wise Sales</h3>""",unsafe_allow_html=True)
    chart2 = px.pie(filter_df,
                    values="Sales",
                    names="Ship Mode", color = "Ship Mode" , color_discrete_map=colors)
    st.plotly_chart(chart2)

# make a Choropleth  and histplot 
co1 , co2 = st.columns([3,1])
with co1:
    st.subheader('City-wise Sales Distribution')
    plot1 = px.choropleth(filter_df,locations="City" , locationmode= 'country names', color="Sales",
                          hover_name="City" , hover_data={"Sales" : True} , color_continuous_scale=px.colors.sequential.Plasma)
    st.plotly_chart(plot1)
with co2:
    st.subheader("Sales Distribution")
    plot2 = px.histogram(filter_df,
                         x = 'Sales' , nbins=30, color_discrete_sequence=["#AD7174"])
    st.plotly_chart(plot2)

# summary tabel
st.subheader(":point_right: Summary Tabel ")
with st.expander("View Top 5 Records"):
     df_sample = df.head(5)[["Region","State","City","Category","Ship Mode","Segment","Sales"]]
     fig = ff.create_table(df_sample,colorscale='cividis')
     st.plotly_chart(fig)
     csv_sample = df_sample.to_csv(index=False).encode('utf-8')
     st.download_button("Download Table ", data=csv_sample, file_name="summary_table.csv", mime="text/csv")


# Seasonal Sales
st.markdown("""<h3 style='text-align: center;'>City wise Sales Distribution</h3>""",unsafe_allow_html=True)
plot =  px.scatter(
    filter_df,
    x="City",
    y="Sales",
    color="Segment",
    size="Sales",
    hover_name="City"
)
st.plotly_chart(plot)

#data
with st.expander("View Data"):
    st.write(filter_df.iloc[:500,1:20:2].style.background_gradient(cmap="Oranges"))

# Download filter DataSet
csv = filter_df.to_csv(index = False).encode('utf-8')
st.download_button('Download filter Data', data =csv, file_name = "filter_data.csv",mime = "text/csv")