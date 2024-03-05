import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# 
def create_weekday_df(day_df):
    # memfilter data berdasarkan weekday dan menyimpan pada tabel weekday_df
    weekday_df = day_df.groupby(by='weekday').agg({
        'count': 'sum'
    }).reset_index()
    # Mendefinisikan urutan hari sebagai kategori
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # Mengubah kolom weekday menjadi tipe data kategorikal dengan urutan yang ditentukan
    weekday_df['weekday'] = pd.Categorical(weekday_df['weekday'], categories=weekday_order, ordered=True)
    # Mengurutkan DataFrame berdasarkan kolom weekday
    return weekday_df.sort_values(by='weekday')

def create_weather_df(hour_df):
    weather_df = hour_df.groupby(by='weathersit').agg({
        'count': 'sum'
    }).reset_index()
    return weather_df

data1_df = pd.read_csv('day_data.csv')
data2_df = pd.read_csv('hour_data.csv')

min_date = data1_df["datetime"].min()
max_date = data1_df["datetime"].max()

min_date = data2_df["datetime"].min()
max_date = data2_df["datetime"].max()

weekday_df = create_weekday_df(data1_df)
weather_df = create_weather_df(data2_df)

with st.sidebar:
    
    st.header("Data Analysis Project")
    st.subheader("By Zahran Fikri")
    # st.image("")

st.header("Bike Sharing Data Dashboard :sparkles:")

with st.expander("About Dataset"):
        st.write(
            """Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions,
            precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
            publicly available in http://capitalbikeshare.com/system-data. We aggregated the data on two hourly and daily basis and then 
            extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com.
            """
        )

col1, col2, col3 = st.columns(3)
 
with col1:
    st.metric(label="Bikers Count", value=data1_df['count'].sum())
    st.caption("Total of bikers")
 
with col2:
    st.metric(label="Total Registered", value=data1_df['registered'].sum())
    st.caption("Total of registered users")
 
with col3:
    st.metric(label="Total Casual", value=data1_df['casual'].sum())
    st.caption("Total of casual users")

st.text("")

st.subheader("Bike Users Data Visualization")

tab1, tab2 = st.tabs(["Count by Weekday", "Count by Weather"])
 
with tab1:
    st.subheader("Count by Weekday")
    plt.figure(figsize=(10,5)) 
    plt.bar(weekday_df['weekday'],weekday_df['count'], color="#50C4ED")
    plt.title("Bike User Count by Weekday")
    plt.ticklabel_format(style='plain', axis='y')
    st.pyplot(plt)
    with st.expander("About This Visualization"):
        st.write(
            """This indicates that the intensity of bike usage throughout the week is very high, as seen in the data visualization graph. 
            The highest number of bike users occurs on Friday, indicating that many people use bikes as their primary mode of 
            transportation towards the end of the week, perhaps due to reasons such as recreational activities. 
            Conversely, bike usage intensity decreases on Sunday, which may be attributed to factors such as weekend holidays with family 
            or a preference for resting at home.
            """
        )
    
with tab2:
    st.subheader("Count by Weather")
    plt.figure(figsize=(10,5)) 
    plt.barh(weather_df['weathersit'],weather_df['count'], color="#50C4ED")
    plt.title("Bike User Count by Weather")
    plt.ticklabel_format(style='plain', axis='x')
    st.pyplot(plt)
    with st.expander("About This Visualization"):
        st.write(
            """Based on the above data, it can be concluded that the highest number of bike users occurs during clear weather conditions. 
            This indicates that sunny weather tends to increase people's interest and willingness to use bikes, as these conditions 
            are comfortable and safe for bike users. On the other hand, the least bike usage occurs during heavy rain. This is because 
            adverse weather conditions such as heavy rain can be a barrier for bike users, both in terms of comfort and safety.
            """
        )

st.caption('Copyright (c) 2024 Zahran Fikri')
