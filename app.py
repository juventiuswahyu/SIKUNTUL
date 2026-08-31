import streamlit as st
from PIL import Image
import os
from collections import Counter

st.set_page_config(
    page_title="SIKUNTUL - Konsultasi Jurusan UNKARTUR", 
    page_icon="🎓",
    layout="centered"
)

# Tampilkan Logo (Jika ada)
logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=150)

st.title("🎓 SIKUNTUL")
st.subheader("Sistem Konsultasi untuk Menentukan Tujuan Kuliah")
st.caption("Universitas Nasional Karangturi TA 2026/2027")
st.write("Jawab 7 pertanyaan di bawah ini untuk melihat rekomendasi jurusan beserta rincian biayanya!")

# Data Rincian Biaya Resmi UNKARTUR TA 2026/2027
# (Nama, Deskripsi, SPI, Inisiasi, Biaya 20 SKS, Daftar Ulang, Path Gambar)
jurusan_map = {
    "A": (
        "S1-Manajemen",
        "Kamu cocok di bidang bisnis, kepemimpinan, dan strategi organisasi.",
        "Rp 4.500.000",
        "Rp 1.200.000",
        "Rp 4.000.000",
        "Rp 1.500.000",
        "assets/manajemen.jpg"
    ),
    "B": (
        "S1-Akuntansi",
        "Kamu punya ketelitian tinggi dalam mengelola angka dan keuangan.",
        "Rp 4.500.000",
        "Rp 1.200.000",
        "Rp 4.000.000",
        "Rp 1.500.000",
        "assets/akuntansi.jpg"
    ),
    "C": (
        "S1-Psikologi",
        "Kamu memiliki empati tinggi dan tertarik pada perilaku manusia.",
        "Rp 4.500.000",
        "Rp 1.200.000",
        "Rp 4.000.000",
        "Rp 1.500.000",
        "assets/psikologi.jpg"
    ),
    "D": (
        "S1-Pendidikan Bahasa Inggris",
        "Kamu unggul dalam komunikasi dan interaksi internasional.",
        "Rp 4.500.000",
        "Rp 1.200.000",
        "Rp 4.000.000",
        "Rp 1.500.000",
        "assets/bahasa_inggris.jpg"
    ),
    "E": (
        "S1-Sistem Informasi",
        "Kamu tertarik memecahkan masalah menggunakan teknologi digital.",
        "Rp 4.500.000",
        "Rp 1.200.000",
        "Rp 4.000.000",
        "Rp 1.500.000",
        "assets/sistem_informasi.jpg"
    ),
    "F": (
        "S1-Teknologi Pangan",
        "Kamu suka bereksperimen dan berinovasi di industri makanan.",
        "Rp 4.500.000",
        "Rp 1.200.000",
        "Rp 4.000.000",
        "Rp 1.500.000",
        "assets/teknologi_pangan.jpg"
    ),
    "G": (
        "S1-Manajemen Informasi Kesehatan",
        "Kamu cocok mengelola data dan sistem administrasi kesehatan.",
        "Rp 4.500.000",
        "Rp 1.200.000",
        "Rp 4.000.000",
        "Rp 1.500.000",
        "assets/mik.jpg"
    )
}

# Daftar Pertanyaan
questions = [
    {
        "q": "1. Aktivitas seperti apa yang paling kamu nikmati?",
        "options": {
            "A. Mengatur kegiatan atau memimpin sebuah tim": "A",
            "B. Menghitung dan mengelola keuangan": "B",
            "C. Mendengarkan dan membantu orang lain": "C",
            "D. Berkomunikasi menggunakan bahasa Inggris": "D",
            "E. Menggunakan komputer dan teknologi": "E",
            "F. Bereksperimen dan menciptakan produk makanan": "F",
            "G. Mengelola informasi dan data kesehatan": "G"
        }
    },
    {
        "q": "2. Bidang pekerjaan mana yang paling menarik perhatianmu?",
        "options": {
            "A. Pengusaha, manager, atau business development": "A",
            "B. Akuntan, auditor, atau financial analyst": "B",
            "C. HR, konselor, atau bidang pengembangan manusia": "C",
            "D. Guru, penerjemah, atau profesional bahasa": "D",
            "E. Programmer, system analyst, atau IT": "E",
            "F. Quality control atau pengembangan produk makanan": "F",
            "G. Administrasi dan informasi rumah sakit": "G"
        }
    },
    {
        "q": "3. Jika kamu diberi sebuah masalah, kamu lebih suka…",
        "options": {
            "A. Membuat strategi agar tujuan dapat tercapai": "A",
            "B. Menganalisis angka dan data secara detail": "B",
            "C. Memahami orang-orang yang terlibat dalam masalah tersebut": "C",
            "D. Menjelaskan solusi kepada orang lain dengan komunikasi yang baik": "D",
            "E. Mencari solusi menggunakan teknologi": "E",
            "F. Melakukan penelitian atau percobaan": "F",
            "G. Mengorganisasi dan mengelola data/informasi": "G"
        }
    },
    {
        "q": "4. Kemampuan apa yang paling menggambarkan dirimu?",
        "options": {
            "A. Memimpin dan mengambil keputusan": "A",
            "B. Teliti terhadap angka dan detail": "B",
            "C. Mudah memahami perasaan orang lain": "C",
            "D. Suka berkomunikasi dan belajar bahasa": "D",
            "E. Cepat memahami teknologi": "E",
            "F. Suka eksperimen dan memahami proses": "F",
            "G. Suka mengelola data dan informasi": "G"
        }
    },
    {
        "q": "5. Lingkungan kerja seperti apa yang kamu bayangkan?",
        "options": {
            "A. Perusahaan atau dunia bisnis": "A",
            "B. Kantor keuangan atau perusahaan": "B",
            "C. Lingkungan yang banyak berinteraksi dengan orang": "C",
            "D. Sekolah atau lingkungan pendidikan": "D",
            "E. Perusahaan teknologi atau digital": "E",
            "F. Laboratorium atau industri makanan": "F",
            "G. Rumah sakit atau fasilitas kesehatan": "G"
        }
    },
    {
        "q": "6. Topik apa yang paling sering membuatmu penasaran?",
        "options": {
            "A. Bagaimana sebuah bisnis bisa sukses": "A",
            "B. Bagaimana perusahaan mengelola uang": "B",
            "C. Mengapa manusia memiliki perilaku yang berbeda": "C",
            "D. Bagaimana berkomunikasi dengan orang dari berbagai negara": "D",
            "E. Bagaimana teknologi dapat membantu kehidupan manusia": "E",
            "F. Bagaimana makanan dibuat dan dikembangkan": "F",
            "G. Bagaimana data kesehatan dapat membantu pelayanan pasien": "G"
        }
    },
    {
        "q": "7. Jika memiliki waktu untuk belajar hal baru, kamu paling tertarik belajar tentang…",
        "options": {
            "A. Bisnis dan cara membangun usaha": "A",
            "B. Investasi, keuangan, dan perpajakan": "B",
            "C. Kepribadian dan perilaku manusia": "C",
            "D. Bahasa dan komunikasi internasional": "D",
            "E. Coding dan teknologi digital": "E",
            "F. Inovasi produk makanan": "F",
            "G. Sistem dan informasi pelayanan kesehatan": "G"
        }
    }
]

# Form Input User
with st.form("sikuntul_form"):
    answers = []
    for i, item in enumerate(questions):
        choice = st.radio(item["q"], list(item["options"].keys()), key=i)
        answers.append(item["options"][choice])
    
    submitted = st.form_submit_button("Lihat Hasil Rekomendasi")

# Kalkulasi & Tampilan Hasil
if submitted:
    counts = Counter(answers)
    top_code, freq = counts.most_common(1)[0]
    
    jurusan, deskripsi, spi, inisiasi, biaya_sks, daftar_ulang = jurusan_map[top_code][:6]
    img_path = jurusan_map[top_code][6]
    
    st.divider()
    st.success("🎉 Hasil Rekomendasi Ditemukan!")
    
    # Menampilkan Gambar Jurusan jika File Ada
    if os.path.exists(img_path):
        st.image(img_path, caption=f"Program Studi {jurusan}", use_column_width=True)
    
    st.markdown(f"### **Rekomendasi Utama: {jurusan}**")
    st.write(deskripsi)
    
    # Rincian Biaya Pendidikan Resmi
    st.markdown("#### 💳 **Rincian Biaya Pendidikan (TA 2026/2027)**")
    
    st.markdown("**1. Dibayar 1x per Tahun Akademik:**")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="SPI (Sumbangan Pengembangan)", value=spi)
    with col2:
        st.metric(label="Inisiasi", value=inisiasi)
        
    st.markdown("**2. Dibayarkan Setiap Semester:**")
    col3, col4 = st.columns(2)
    with col3:
        st.metric(label="Biaya 20 SKS (Rp 200rb/SKS)", value=biaya_sks)
    with col4:
        st.metric(label="Daftar Ulang", value=daftar_ulang)
    
    # Catatan Ketentuan Tambahan
    with st.expander("📌 **Catatan Ketentuan Biaya**"):
        st.write("""
        1. **SPI** dapat diangsur selama 3x dan harus lunas sebelum kegiatan PKKMB.
        2. **Biaya Inisiasi** dibayar 1x saat registrasi (terdiri dari biaya orientasi, kaos, dan jas almamater).
        3. **Biaya Kuliah per Semester:**
           - Biaya SKS: Rp 200.000 / SKS
           - Biaya SKS Praktikum: Rp 250.000 / SKS
        4. Pelunasan Daftar Ulang dan SKS tiap semester sebagai syarat pengisian KRS di awal semester.
        5. Biaya belum termasuk biaya magang, cuti, skripsi, wisuda, dll.
        6. Biaya cuti = senilai biaya 4 SKS; Biaya wisuda = Rp 1.750.000.
        """)
