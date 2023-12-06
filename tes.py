import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset
url = "https://raw.githubusercontent.com/Adikaswandi/dicoding_bike-sharing-/main/bike_new_data.csv"
bike_data = pd.read_csv(url)

# Sidebar
st.sidebar.title("Dashboard Data Peminjaman Sepeda")
selected_chart = st.sidebar.selectbox("Pilih Chart:", ["Pengaruh Cuaca", "Perubahan Pola Musim", "Peminjaman Hari Kerja vs Akhir Pekan"])

# Main content
st.title("Analisis Data Peminjaman Sepeda")

if selected_chart == "Pengaruh Cuaca":
    st.subheader("Pengaruh Cuaca terhadap Jumlah Peminjam Sepeda")
    # Visualisasi 1: Pengaruh Cuaca terhadap Jumlah Peminjam Sepeda (Bar Chart)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=bike_data)
    plt.title('Pengaruh Cuaca terhadap Jumlah Peminjam Sepeda')
    plt.xlabel('Cuaca')
    plt.ylabel('Jumlah Peminjam Sepeda')
    st.pyplot(plt)

elif selected_chart == "Perubahan Pola Musim":
    st.subheader("Perubahan Pola Peminjaman Sepeda Selama Musim")
    # Visualisasi 2: Perubahan Pola Peminjaman Sepeda Selama Musim
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='mnth', y='cnt', hue='season', data=bike_data)
    plt.title('Perubahan Pola Peminjaman Sepeda Selama Musim')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjam Sepeda')
    st.pyplot(plt)

elif selected_chart == "Peminjaman Hari Kerja vs Akhir Pekan":
    st.subheader("Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
    # Visualisasi 3: Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weekday', y='cnt', hue='workingday', data=bike_data)
    plt.title('Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan')
    plt.xlabel('Hari')
    plt.ylabel('Jumlah Peminjam Sepeda')
    st.pyplot(plt)