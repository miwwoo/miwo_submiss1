import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membaca dataset
aotizhongxin_df = pd.read_csv('C:/Users/user/Desktop/submission/data/PRSA_Data_Aotizhongxin_20130301-20170228.csv')
changping_df = pd.read_csv('C:/Users/user/Desktop/submission/data/PRSA_Data_Changping_20130301-20170228.csv')
tiantan_df = pd.read_csv('C:/Users/user/Desktop/submission/data/PRSA_Data_Tiantan_20130301-20170228.csv')

# Menggabungkan dataset
df_combined = pd.concat([aotizhongxin_df, changping_df, tiantan_df])

# Menggabungkan kolom tahun, bulan, hari, dan jam menjadi kolom datetime
df_combined['datetime'] = pd.to_datetime(df_combined[['year', 'month', 'day', 'hour']])
df_combined.set_index('datetime', inplace=True)

# Mengisi nilai yang hilang
columns_to_fill_median = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
for column in columns_to_fill_median:
    df_combined[column] = df_combined[column].fillna(df_combined[column].median())
df_combined['wd'] = df_combined['wd'].fillna('Unknown')

# Menghapus kolom yang tidak perlu
df_combined.drop(columns=['year', 'month', 'day', 'hour'], inplace=True)

# Judul Dashboard
st.title("Dashboard Kualitas Udara")

# Visualisasi 1: Hubungan antara Kecepatan Angin dan Konsentrasi PM2.5
st.subheader('Kecepatan Angin vs PM2.5')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='WSPM', y='PM2.5', data=df_combined, ax=ax1)
ax1.set_xlabel('Kecepatan Angin (m/s)')
ax1.set_ylabel('Konsentrasi PM2.5')
ax1.grid(True)
st.pyplot(fig1)

# Visualisasi 2: Tekanan Atmosfer vs PM2.5
st.subheader('Tekanan Atmosfer vs PM2.5')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='PRES', y='PM2.5', data=df_combined, ax=ax2)
ax2.set_xlabel('Tekanan Atmosfer (hPa)')
ax2.set_ylabel('Konsentrasi PM2.5')
ax2.grid(True)
st.pyplot(fig2)

# Visualisasi 3: Curah Hujan vs PM2.5
st.subheader('Curah Hujan vs PM2.5')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='RAIN', y='PM2.5', data=df_combined, ax=ax3)
ax3.set_xlabel('Curah Hujan (mm)')
ax3.set_ylabel('Konsentrasi PM2.5')
ax3.grid(True)
st.pyplot(fig3)

# Menampilkan Kesimpulan
st.subheader("Kesimpulan")
st.write("1. Kecepatan angin (WSPM) dapat mempengaruhi penyebaran polutan.")
st.write("   Kecepatan angin yang lebih tinggi cenderung menyebarkan polusi udara, "
         "yang dapat menurunkan konsentrasinya.")
st.write("2. Kondisi cuaca seperti tekanan atmosfer dan curah hujan "
         "dapat secara signifikan mempengaruhi kualitas udara. Misalnya, hujan dapat menghilangkan "
         "polutan dari udara.")
