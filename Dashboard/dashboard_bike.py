import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk menghitung persentase peningkatan jumlah peminjam sepeda pada hari libur dibandingkan dengan hari kerja
def calculate_percentage_increase(df_Bday):
    grouped_data = df_Bday.groupby('holiday')['cnt'].mean()
    avg_rental_holiday = grouped_data[1]
    avg_rental_workday = grouped_data[0]
    percentage_increase = ((avg_rental_holiday - avg_rental_workday) / avg_rental_workday) * 100
    return percentage_increase

# Fungsi untuk menampilkan rata-rata jumlah peminjam sepeda per jam pada hari-hari musim panas di tahun 2012
def plot_average_hourly_rentals(df_Bhour):
    summer_2012_data = df_Bhour[(df_Bhour['yr'] == 0) & (df_Bhour['mnth'].isin([6, 7, 8]))]
    average_hourly_rentals = summer_2012_data.groupby('hr')['cnt'].mean()
    fig, ax = plt.subplots()
    ax.plot(average_hourly_rentals.index, average_hourly_rentals.values, marker='o', linestyle='-')
    ax.set_title('Rata-rata Jumlah Peminjam Sepeda per Jam (Musim Panas 2012)')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Rata-rata Jumlah Peminjam')
    ax.grid(True)
    ax.set_xticks(range(24))
    return fig

# Fungsi untuk menampilkan hubungan antara cuaca dan jumlah peminjam sepeda
def plot_average_rentals_by_weather(df_Bday):
    average_rentals_by_weather = df_Bday.groupby('weathersit')['cnt'].mean()
    fig, ax = plt.subplots()
    average_rentals_by_weather.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Rata-rata Jumlah Peminjam Sepeda Berdasarkan Kondisi Cuaca')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Rata-rata Jumlah Peminjam Sepeda')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.grid(axis='y')
    return fig

# Fungsi untuk menampilkan scatter plot antara suhu udara dan jumlah peminjam sepeda
def plot_scatter_temp_vs_cnt(df_Bday):
    fig, ax = plt.subplots()
    ax.scatter(df_Bday['temp'], df_Bday['cnt'], color='blue', alpha=0.5)
    ax.set_title('Hubungan antara Suhu Udara dan Jumlah Peminjam Sepeda')
    ax.set_xlabel('Suhu Udara (°C)')
    ax.set_ylabel('Jumlah Peminjam Sepeda')
    ax.grid(True)
    return fig

# Fungsi untuk menampilkan tren penggunaan sepeda pada jam-jam puncak selama hari libur pada bulan Desember 2011
def plot_hourly_rentals_december_2011(df_Bhour):
    december_2011_holiday = df_Bhour[(df_Bhour['yr'] == 0) & (df_Bhour['mnth'] == 12) & (df_Bhour['holiday'] == 1)]
    hourly_rentals_december_2011 = december_2011_holiday.groupby('hr')['cnt'].sum()
    fig, ax = plt.subplots()
    ax.plot(hourly_rentals_december_2011.index, hourly_rentals_december_2011.values)
    ax.set_title('Tren Penggunaan Sepeda pada Jam-jam Puncak selama Hari Libur Bulan Desember 2011')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Peminjam Sepeda')
    ax.grid(True)
    ax.set_xticks(range(24))
    return fig

st.title('Dashboard Analisis Data Sepeda')
st.write("Pilihlah Pada Bagian Kiri Untuk menampilkan Hasil Analisis")

# Membaca dataset

df_Bday = pd.read_csv("Bike-sharing-dataset/day.csv")
df_Bhour = pd.read_csv("Bike-sharing-datase/hour.csv")

# Mengonversi kolom "dteday" menjadi tipe data datetime
df_Bday["dteday"] = pd.to_datetime(df_Bday["dteday"])
df_Bhour["dteday"] = pd.to_datetime(df_Bhour["dteday"])

st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write("Day")
    st.write(df_Bhour)
    st.write("Hour")
    st.write(df_Bday)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write("Bike Day")
    st.write(df_Bday.describe())
    st.write("""melihat info dari dataset day:\n
            Jumlah data: 731 entri.
            Musim paling umum: Musim panas (season 2).
            Dominan Tahun: 2012 (yr = 1).
            Bulan yang sering muncul: Juli (mnth 7).
            Hari libur hanya ada sekitar 2.87% dari total hari.
            Hari kerja adalah mayoritas (sekitar 68.40%).
            Cuaca rata-rata pada keadaan yang baik (weathersit 1).
            Suhu rata-rata adalah sekitar 0.50, dengan suhu perasaan rata-rata sekitar 0.47.
            Kelembaban rata-rata sekitar 0.63 (63%).
            Kecepatan angin rata-rata adalah sekitar 0.19/19% (maksimal 50%).
            Jumlah pengguna casual rata-rata sekitar 848.
            Jumlah pengguna terdaftar rata-rata sekitar 3656.
            Total rental rata-rata sekitar 4504 per hari.
            """)
    st.subheader("Summary Statistics")
    st.write("Bike Hour")
    st.write(df_Bhour.describe())
    st.write("""melihat info dari dataset hour:\n
            Dataset terdiri dari 17,379 entri.
            Rata-rata kolom-kolom utama adalah sekitar:
            Season atau Musim 2.50 adalah musim rata-rata.
            Tahun atau yr 0.50, perbandingan antara tahun 2011 dan 2012.
            Bulan atau mnth 6.54, rata-rata bulan dalam setahun.
            hr 11.55 adalah jam rata-rata dalam sehari.
            Holiday 0.03 adalah persentase hari libur.
            weekday 3.00 adalah hari rata-rata dalam seminggu.
            workingday 0.68 menunjukan persentase hari kerja.
            Kweathersit 1.43 untuk kondisi cuaca rata-rata.
            temp 0.50 menunjukan suhu rata-rata yang normal.
            atemp 0.48 ialah suhu perasaan mendekati suhu sebenarnya.
            hum 0.48 mengindikasikan kelembaban rata-rata.
            windspeed 0.63 merupakan kecepatan angin rata-rata.
            casual 35.68 itu rata-rata jumlah pengguna casual.
            registered dengan jumlah 153.79 pengguna terdaftar.
            cnt 189.46 yaitu rata-rata jumlah total rental sepeda.
            """)
    
# Checkbox untuk menampilkan heatmap korelasi
show_heatmap = st.sidebar.checkbox('Tampilkan Heatmap Korelasi')

# Jika checkbox dicentang, tampilkan heatmap korelasi
if show_heatmap:
    st.header("Heatmap Korelasi")
    # Menghitung korelasi antar atribut numerik
    correlation_matrix_day = df_Bday.corr()

    # Membuat heatmap korelasi untuk df_day
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix_day, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Heatmap Korelasi untuk Dataset Day')
    st.pyplot(plt)
    
# Fungsi untuk menampilkan boxplot
def show_boxplot(dataframe, x, y, title, xlabel, ylabel):
    fig, ax = plt.subplots()  # Membuat objek figure
    sns.boxplot(data=dataframe, x=x, y=y, palette='Set2', ax=ax)  # Menggambar boxplot
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)  # Menampilkan gambar menggunakan st.pyplot()

# Fungsi untuk menampilkan scatter plot
def show_scatterplot(x, y, title, xlabel, ylabel):
    fig, ax = plt.subplots()  # Membuat objek figure
    ax.scatter(x, y, color='blue', alpha=0.5)  # Menggambar scatter plot
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)  # Menampilkan gambar menggunakan st.pyplot()

# Menampilkan visualisasi dalam satu checkbox
if st.sidebar.checkbox("Tampilkan Visualisasi Data"):
    # Menampilkan visualisasi hubungan antara musim dan jumlah sewa
    st.header("Hubungan antara Musim dan Jumlah Sewa")
    show_boxplot(df_Bday, 'season', 'cnt', 'Hubungan antara Musim dan Jumlah Sewa', 'Musim', 'Jumlah Sewa')

    # Menampilkan visualisasi hubungan antara hari libur dan jumlah sewa
    st.header("Hubungan antara Hari Libur dan Jumlah Sewa")
    show_boxplot(df_Bday, 'holiday', 'cnt', 'Hubungan antara Hari Libur dan Jumlah Sewa', 'Hari Libur', 'Jumlah Sewa')

    # Menampilkan visualisasi hubungan antara cuaca dan jumlah sewa
    st.header("Hubungan antara Cuaca dan Jumlah Sewa")
    show_boxplot(df_Bday, 'weathersit', 'cnt', 'Hubungan antara Cuaca dan Jumlah Sewa', 'Cuaca', 'Jumlah Sewa')

    # Menampilkan scatter plot antara suhu dan jumlah sewa
    st.header("Scatter Plot antara Suhu dan Jumlah Sewa")
    show_scatterplot(df_Bday['temp'], df_Bday['cnt'], 'Scatter Plot antara Suhu dan Jumlah Sewa', 'Suhu (°C)', 'Jumlah Sewa')

# Membuat kolom Cluster
selected_features = df_Bhour[['temp', 'hum']]
clusters = []

for temp, hum in zip(selected_features['temp'], selected_features['hum']):
    if temp <= 5:
        clusters.append('Cluster 1')
    elif 5 < temp <= 15:
        clusters.append('Cluster 2')
    elif 15 < temp <= 25:
        clusters.append('Cluster 3')
    else:
        clusters.append('Cluster 4')

# Tambahkan label cluster ke DataFrame
df_Bhour['Cluster'] = clusters

# Checkbox untuk menampilkan visualisasi
show_plot = st.sidebar.checkbox('Tampilkan Visualisasi Hasil Clustering')

# Jika checkbox dicentang, tampilkan visualisasi
if show_plot:
    st.write('Hasil Clustering:')
    st.write(df_Bhour.head())

    # Visualisasi scatter plot
    st.write('Visualisasi Hasil Clustering:')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df_Bhour, x='temp', y='hum', hue='Cluster', palette='Set1', ax=ax)
    plt.title('Hasil Clustering')
    plt.xlabel('Temperature')
    plt.ylabel('Humidity')
    plt.grid(True)
    st.pyplot(fig)

# Daftar opsi analisis data
analysis_options = ['Persentase Peningkatan Jumlah Peminjam Sepeda pada Hari Libur',
                    'Rata-rata Jumlah Peminjam Sepeda per Jam pada Musim Panas 2012',
                    'Rata-rata Jumlah Peminjam Sepeda Berdasarkan Kondisi Cuaca',
                    'Hubungan antara Suhu Udara dan Jumlah Peminjam Sepeda',
                    'Tren Penggunaan Sepeda pada Jam-jam Puncak selama Hari Libur Bulan Desember 2011',
                    'Kesimpulan Hasil Analisis']

# Checkbox untuk memilih opsi analisis data
selected_options = st.sidebar.multiselect('Pilih Hasil Analisis Data:', analysis_options)

# Melakukan analisis data berdasarkan opsi yang dipilih
if 'Persentase Peningkatan Jumlah Peminjam Sepeda pada Hari Libur' in selected_options:
    percentage_increase = calculate_percentage_increase(df_Bday)
    st.write(f'Persentase peningkatan jumlah peminjam pada hari libur dibandingkan dengan hari kerja: {percentage_increase:.2f}%')

if 'Rata-rata Jumlah Peminjam Sepeda per Jam pada Musim Panas 2012' in selected_options:
    st.write('Rata-rata Jumlah Peminjam Sepeda per Jam pada Musim Panas 2012:')
    fig = plot_average_hourly_rentals(df_Bhour)
    st.pyplot(fig)

if 'Rata-rata Jumlah Peminjam Sepeda Berdasarkan Kondisi Cuaca' in selected_options:
    st.write('Rata-rata Jumlah Peminjam Sepeda Berdasarkan Kondisi Cuaca:')
    fig = plot_average_rentals_by_weather(df_Bday)
    st.pyplot(fig)

if 'Hubungan antara Suhu Udara dan Jumlah Peminjam Sepeda' in selected_options:
    st.write('Hubungan antara Suhu Udara dan Jumlah Peminjam Sepeda:')
    fig = plot_scatter_temp_vs_cnt(df_Bday)
    st.pyplot(fig)

if 'Tren Penggunaan Sepeda pada Jam-jam Puncak selama Hari Libur Bulan Desember 2011' in selected_options:
    st.write('Tren Penggunaan Sepeda pada Jam-jam Puncak selama Hari Libur Bulan Desember 2011:')
    fig = plot_hourly_rentals_december_2011(df_Bhour)
    st.pyplot(fig)
    
if 'Kesimpulan Hasil Analisis' in selected_options:
    st.header("Kesimpulan Hasil Analisis yang Dilakukan")
    st.write("""
            1. Penurunan Jumlah Peminjam Sepeda pada Hari Libur: Terjadi penurunan sebesar -17.50 persen dalam jumlah peminjam sepeda pada hari libur dibandingkan dengan hari kerja. Penurunan ini dapat disebabkan oleh perbedaan perilaku masyarakat, ketersediaan sepeda, kondisi cuaca, dan promosi khusus yang mungkin mempengaruhi penggunaan sepeda.

            2. Pola Penggunaan Sepeda pada Hari-hari Musim Panas 2012:
            Analisis menunjukkan variasi rata-rata penggunaan sepeda per jam selama hari-hari musim panas 2012. Puncak penggunaan terjadi pada jam 08.00 dan jam 17.00, sedangkan jumlah peminjam paling rendah terjadi pada jam 4.00.

            3. Strategi untuk Cuaca Buruk:
            Berbagai strategi dapat diterapkan untuk meningkatkan penggunaan sepeda saat cuaca buruk, termasuk perlindungan cuaca, promosi khusus, perbaikan infrastruktur, edukasi, dan perbaikan layanan transportasi publik.

            4. Hubungan Suhu Udara dengan Jumlah Peminjam Sepeda:
            Ada korelasi antara suhu udara dan jumlah peminjam sepeda, dengan cuaca hangat cenderung meningkatkan penggunaan sepeda.

            5. Tren Penggunaan Sepeda pada Hari Libur di Bulan Desember 2011:
            Tren penggunaan sepeda pada hari libur di bulan Desember 2011 menunjukkan peningkatan aktivitas pada siang hari, dengan puncak penggunaan sepeda terjadi sekitar jam 14:00.
             """)
    
st.sidebar.markdown("Nama  : Fahril Sidik Alfarizi")
st.sidebar.markdown("Email : fahrilsidik207@gmail.com")
st.sidebar.markdown("ID    : fahrilalfarizi15")
st.sidebar.markdown("Github: https://github.com/fahrilAlfarizi/project_Dicoding/tree/master")
