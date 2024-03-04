import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

pwd = os.getcwd()

# Membuat function untuk manipulasi dataframe
def byweather(df):
    weather_rental = df.groupby(by='weathersit')['cnt'].mean()
    return weather_rental

# import dataframe
weather_df = pd.read_csv('all_data.csv')

# Menyiapkan dataframe yang dikelompokkan
byweather_df = byweather(weather_df)

st.header('Bike Sharing Dashboard - Penggunaan Berdasarkan Cuaca')
st.markdown("""
<div style="text-align: justify">
  Dashboard ini menyajikan visualisasi data yang menunjukkan penggunaan rental sepeda berdasarkan kategori cuaca pada tahun 2011 dan 2012. 
</div>
""", unsafe_allow_html=True)

# Plotting Rata-rata Pengguna Sepeda Berdasarkan Cuaca
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(byweather_df.index, byweather_df.values, color='#00E8FF')
ax.tick_params(axis='y', labelsize=14)
ax.tick_params(axis='x', labelsize=12)

# Mengubah latar belakang grafik menjadi putih
fig.patch.set_facecolor('white')
ax.set_facecolor('#F0F0F0')

# Menambahkan label x, label y, dan judul
ax.set_xlabel('Cuaca', fontsize=14)
ax.set_ylabel('Jumlah Penggunaan', fontsize=14)
ax.set_title('Rata-rata Pengguna Sepeda Berdasarkan Cuaca', fontsize=16)

# Tampilkan plot menggunakan st.pyplot()
st.pyplot(fig)

# Seaborn Plot for 2011 and 2012 with Hue
st.subheader("Jumlah Rental Sepeda Berdasarkan Cuaca pada Tahun 2011 dan 2012")
data_2011_2012 = weather_df[(weather_df['yr'] == 2011) | (weather_df['yr'] == 2012)]
sns.barplot(x='weathersit', y='cnt', data=data_2011_2012, hue='yr')

plt.xlabel("Cuaca")
plt.ylabel("Jumlah Rental Sepeda")
plt.title("Jumlah Rental Sepeda Berdasarkan Cuaca pada Tahun 2011 dan 2012")

# Tampilkan plot menggunakan st.pyplot()
st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """Berdasarkan data tahun 2011 sampai tahun 2012, jumlah tertinggi pengguna sepeda terjadi pada saat cuaca cerah/*clear*
        dan jumlah terendah pengguna sepeda terjadi pada saat cuaca hujan lebat/*heavy precipitation*. Dari grafik juga terlihat menunjukkan *right-skewed distribution*."""
    )

st.caption('Copyright © Dayn Albab 2024')
