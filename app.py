import streamlit as st
import os
from groq import Groq

st.set_page_config(
    page_title="SIKUNTUL - AI Counseling UNKARTUR", 
    page_icon="🎓",
    layout="centered"
)

# Inisialisasi Groq Client dari Streamlit Secrets atau Environment Variable
groq_api_key = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")

if not groq_api_key:
    st.error("⚠️ API Key Groq belum dipasang. Silakan tambahkan GROQ_API_KEY di Streamlit Secrets!")
    st.stop()

client = Groq(api_key=groq_api_key)

# Tampilkan Logo (Jika file ada)
logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=150)

st.title("🎓 SIKUNTUL AI")
st.subheader("Sistem Konsultasi Cerdas Menentukan Tujuan Kuliah")
st.caption("Powered by Groq AI • Universitas Nasional Karangturi TA 2026/2027")
st.write("Jawab 7 pertanyaan di bawah ini. AI akan menganalisis preferensimu secara mendalam untuk menentukan 1 dari 7 program studi UNKARTUR yang paling cocok!")

# Data 7 Prodi dan Biaya Resmi UNKARTUR (Sesuai Flyer TA 2026/2027)
prodi_info = {
    "S1-Manajemen": {
        "spi": "Rp 4.500.000", "inisiasi": "Rp 1.200.000", 
        "sks": "Rp 4.000.000", "daftar_ulang": "Rp 1.500.000", 
        "img": "assets/manajemen.jpg"
    },
    "S1-Akuntansi": {
        "spi": "Rp 4.500.000", "inisiasi": "Rp 1.200.000", 
        "sks": "Rp 4.000.000", "daftar_ulang": "Rp 1.500.000", 
        "img": "assets/akuntansi.jpg"
    },
    "S1-Sistem Informasi": {
        "spi": "Rp 4.500.000", "inisiasi": "Rp 1.200.000", 
        "sks": "Rp 4.000.000", "daftar_ulang": "Rp 1.500.000", 
        "img": "assets/sistem_informasi.jpg"
    },
    "S1-Teknologi Pangan": {
        "spi": "Rp 4.500.000", "inisiasi": "Rp 1.200.000", 
        "sks": "Rp 4.000.000", "daftar_ulang": "Rp 1.500.000", 
        "img": "assets/teknologi_pangan.jpg"
    },
    "S1-Psikologi": {
        "spi": "Rp 4.500.000", "inisiasi": "Rp 1.200.000", 
        "sks": "Rp 4.000.000", "daftar_ulang": "Rp 1.500.000", 
        "img": "assets/psikologi.jpg"
    },
    "S1-Pendidikan Bahasa Inggris": {
        "spi": "Rp 4.500.000", "inisiasi": "Rp 1.200.000", 
        "sks": "Rp 4.000.000", "daftar_ulang": "Rp 1.500.000", 
        "img": "assets/bahasa_inggris.jpg"
    },
    "S1-Manajemen Informasi Kesehatan": {
        "spi": "Rp 4.500.000", "inisiasi": "Rp 1.200.000", 
        "sks": "Rp 4.000.000", "daftar_ulang": "Rp 1.500.000", 
        "img": "assets/mik.jpg"
    }
}

questions = [
    {
        "q": "1. Aktivitas seperti apa yang paling kamu nikmati?",
        "options": [
            "Mengatur kegiatan atau memimpin sebuah tim",
            "Menghitung dan mengelola keuangan",
            "Mendengarkan dan membantu orang lain",
            "Berkomunikasi menggunakan bahasa Inggris",
            "Menggunakan komputer dan teknologi",
            "Bereksperimen dan menciptakan produk makanan",
            "Mengelola informasi dan data kesehatan"
        ]
    },
    {
        "q": "2. Bidang pekerjaan mana yang paling menarik perhatianmu?",
        "options": [
            "Pengusaha, manager, atau business development",
            "Akuntan, auditor, atau financial analyst",
            "HR, konselor, atau bidang pengembangan manusia",
            "Guru, penerjemah, atau profesional bahasa",
            "Programmer, system analyst, atau IT",
            "Quality control atau pengembangan produk makanan",
            "Administrasi dan informasi rumah sakit"
        ]
    },
    {
        "q": "3. Jika kamu diberi sebuah masalah, kamu lebih suka…",
        "options": [
            "Membuat strategi agar tujuan dapat tercapai",
            "Menganalisis angka dan data secara detail",
            "Memahami orang-orang yang terlibat dalam masalah tersebut",
            "Menjelaskan solusi kepada orang lain dengan komunikasi yang baik",
            "Mencari solusi menggunakan teknologi",
            "Melakukan penelitian atau percobaan",
            "Mengorganisasi dan mengelola data/informasi"
        ]
    },
    {
        "q": "4. Kemampuan apa yang paling menggambarkan dirimu?",
        "options": [
            "Memimpin dan mengambil keputusan",
            "Teliti terhadap angka dan detail",
            "Mudah memahami perasaan orang lain",
            "Suka berkomunikasi dan belajar bahasa",
            "Cepat memahami teknologi",
            "Suka eksperimen dan memahami proses",
            "Suka mengelola data dan informasi"
        ]
    },
    {
        "q": "5. Lingkungan kerja seperti apa yang kamu bayangkan?",
        "options": [
            "Perusahaan atau dunia bisnis",
            "Kantor keuangan atau perusahaan",
            "Lingkungan yang banyak berinteraksi dengan orang",
            "Sekolah atau lingkungan pendidikan",
            "Perusahaan teknologi atau digital",
            "Laboratorium atau industri makanan",
            "Rumah sakit atau fasilitas kesehatan"
        ]
    },
    {
        "q": "6. Topik apa yang paling sering membuatmu penasaran?",
        "options": [
            "Bagaimana sebuah bisnis bisa sukses",
            "Bagaimana perusahaan mengelola uang",
            "Mengapa manusia memiliki perilaku yang berbeda",
            "Bagaimana berkomunikasi dengan orang dari berbagai negara",
            "Bagaimana teknologi dapat membantu kehidupan manusia",
            "Bagaimana makanan dibuat dan dikembangkan",
            "Bagaimana data kesehatan dapat membantu pelayanan pasien"
        ]
    },
    {
        "q": "7. Jika memiliki waktu untuk belajar hal baru, kamu paling tertarik belajar tentang…",
        "options": [
            "Bisnis dan cara membangun usaha",
            "Investasi, keuangan, dan perpajakan",
            "Kepribadian dan perilaku manusia",
            "Bahasa dan komunikasi internasional",
            "Coding dan teknologi digital",
            "Inovasi produk makanan",
            "Sistem dan informasi pelayanan kesehatan"
        ]
    }
]

# Form Input User
with st.form("sikuntul_form"):
    user_answers = []
    for i, item in enumerate(questions):
        choice = st.radio(item["q"], item["options"], key=i)
        user_answers.append(f"{item['q']}: {choice}")
    
    submitted = st.form_submit_button("🤖 Analisis dengan AI")

if submitted:
    with st.spinner("AI SIKUNTUL sedang menganalisis minat dan bakatmu..."):
        prompt_system = """
        Kamu adalah AI Konselor Akademik profesional untuk Universitas Nasional Karangturi (UNKARTUR).
        Tugasmu adalah menganalisis jawaban kuesioner siswa dan memilih EXACT 1 PROGRAM STUDI TERBAIK dari 7 pilihan berikut:
        - S1-Manajemen
        - S1-Akuntansi
        - S1-Sistem Informasi
        - S1-Teknologi Pangan
        - S1-Psikologi
        - S1-Pendidikan Bahasa Inggris
        - S1-Manajemen Informasi Kesehatan

        Format Output Bahasa Indonesia yang rapi:
        **Rekomendasi Utama: [Nama Prodi Tepat seperti daftar di atas]**
        
        **Alasan Analisis AI:**
        [Penjelasan personal dan mendalam mengapa prodi ini paling cocok berdasarkan pola jawaban siswa]

        **Prospek Karir Masa Depan:**
        - [Karir 1]
        - [Karir 2]
        - [Karir 3]
        """

        prompt_user = "Berikut adalah jawaban kuesioner siswa:\n" + "\n".join(user_answers)

        try:
            # Menggunakan model llama3-8b-8192 yang stabil di Groq API
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": prompt_system},
                    {"role": "user", "content": prompt_user}
                ],
                temperature=0.7,
                max_tokens=800
            )

            result_text = response.choices[0].message.content
            
            # Parsing Hasil Groq untuk Menentukan Gambar & Biaya Mana yang Tampil
            selected_prodi = "S1-Manajemen" # Default Fallback
            for prodi in prodi_info.keys():
                if prodi.lower() in result_text.lower():
                    selected_prodi = prodi
                    break
            
            st.divider()
            st.success("🎉 Analisis AI SIKUNTUL Selesai!")
            
            # Tampilkan Gambar Prodi Terpilih
            img_path = prodi_info[selected_prodi]["img"]
            if os.path.exists(img_path):
                st.image(img_path, caption=f"Program Studi {selected_prodi}", use_column_width=True)
            
            # Tampilkan Hasil Analisis Teks dari AI
            st.markdown(result_text)
            
            # Tampilkan Rincian Biaya Pendidikan Resmi
            data_biaya = prodi_info[selected_prodi]
            st.markdown("---")
            st.markdown(f"#### 💳 **Rincian Biaya Pendidikan Resmi ({selected_prodi})**")
            st.caption("Universitas Nasional Karangturi TA 2026/2027")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="SPI (1x Bayar)", value=data_biaya["spi"])
                st.metric(label="Biaya Inisiasi (1x Bayar)", value=data_biaya["inisiasi"])
            with col2:
                st.metric(label="Biaya 20 SKS / Semester", value=data_biaya["sks"])
                st.metric(label="Daftar Ulang / Semester", value=data_biaya["daftar_ulang"])
                
            with st.expander("📌 **Catatan Ketentuan Biaya**"):
                st.write("""
                1. **SPI (Sumbangan Pengembangan Institusi)** dapat diangsur selama 3x dan harus lunas sebelum kegiatan PKKMB.
                2. **Biaya Inisiasi** dibayar 1x saat registrasi (terdiri dari biaya orientasi, kaos, dan jas almamater).
                3. **Biaya SKS per Semester:** Rp 200.000 / SKS (Praktikum: Rp 250.000 / SKS).
                4. Pelunasan Daftar Ulang dan SKS tiap semester sebagai syarat pengisian KRS di awal semester.
                5. Biaya belum termasuk biaya magang, cuti, skripsi, dan wisuda (Biaya wisuda = Rp 1.750.000).
                """)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat berkomunikasi dengan AI: {e}")
