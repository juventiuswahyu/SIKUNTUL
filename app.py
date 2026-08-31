import streamlit as st
from groq import Groq

# ---------------------------------------------------------
# 1. Konfigurasi Halaman & Judul Center
# ---------------------------------------------------------
st.set_page_config(
    page_title="SIKUNTUL - Universitas Nasional Karangturi",
    page_icon="🎓",
    layout="centered"
)

# Inisialisasi state untuk reset form
if "form_key" not in st.session_state:
    st.session_state.form_key = 0

# Header Rata Tengah (Logo + Teks Rapat & Center)
st.markdown(
    """
    <style>
    .header-container {
        text-align: center;
        margin-top: -30px;
        margin-bottom: 20px;
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    .header-subtitle {
        font-size: 1.25rem;
        font-weight: 600;
        color: #31333F;
        margin-bottom: 8px;
    }
    .header-desc {
        font-size: 0.95rem;
        color: #555555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menampilkan logo di tengah
col_left, col_logo, col_right = st.columns([1.2, 1.6, 1.2])
with col_logo:
    st.image("logo (2).png", use_container_width=True)

# Teks Header Rata Tengah & Tanpa Topi Wisuda
st.markdown(
    """
    <div class="header-container">
        <div class="header-title">SIKUNTUL</div>
        <div class="header-subtitle">Sistem Konsultasi untuk Menentukan Tujuan Kuliah</div>
        <div class="header-desc">Pilih jawaban yang paling mencerminkan dirimu untuk mendapatkan analisis rekomendasi jurusan komprehensif beserta rincian biayanya!</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------------
# 2. Form Kuesioner (Radio Button Pilihan A - G Terbuka)
# ---------------------------------------------------------
responses = {}
key_suffix = str(st.session_state.form_key)

q1_options = [
    "A. Mengatur kegiatan atau memimpin sebuah tim",
    "B. Menghitung dan mengelola keuangan",
    "C. Mendengarkan dan membantu orang lain",
    "D. Berkomunikasi menggunakan bahasa Inggris",
    "E. Menggunakan komputer dan teknologi",
    "F. Bereksperimen dan menciptakan produk makanan",
    "G. Mengelola informasi dan data kesehatan"
]
responses['q1'] = st.radio("1. Aktivitas seperti apa yang paling kamu nikmati?", q1_options, key=f"q1_{key_suffix}")

q2_options = [
    "A. Pengusaha, manager, atau business development",
    "B. Akuntan, auditor, atau financial analyst",
    "C. HR, konselor, atau bidang pengembangan manusia",
    "D. Guru, penerjemah, atau profesional bahasa",
    "E. Programmer, system analyst, atau IT",
    "F. Quality control atau pengembangan produk makanan",
    "G. Administrasi dan informasi rumah sakit"
]
responses['q2'] = st.radio("2. Bidang pekerjaan mana yang paling menarik perhatianmu?", q2_options, key=f"q2_{key_suffix}")

q3_options = [
    "A. Membuat strategi agar tujuan dapat tercapai",
    "B. Menganalisis angka dan data secara detail",
    "C. Memahami orang-orang yang terlibat dalam masalah tersebut",
    "D. Menjelaskan solusi kepada orang lain dengan komunikasi yang baik",
    "E. Mencari solusi menggunakan teknologi",
    "F. Melakukan penelitian atau percobaan",
    "G. Mengorganisasi dan mengelola data/informasi"
]
responses['q3'] = st.radio("3. Jika kamu diberi sebuah masalah, kamu lebih suka…", q3_options, key=f"q3_{key_suffix}")

q4_options = [
    "A. Memimpin dan mengambil keputusan",
    "B. Teliti terhadap angka dan detail",
    "C. Mudah memahami perasaan orang lain",
    "D. Suka berkomunikasi dan belajar bahasa",
    "E. Cepat memahami teknologi",
    "F. Suka eksperimen dan memahami proses",
    "G. Suka mengelola data dan informasi"
]
responses['q4'] = st.radio("4. Kemampuan apa yang paling menggambarkan dirimu?", q4_options, key=f"q4_{key_suffix}")

q5_options = [
    "A. Perusahaan atau dunia bisnis",
    "B. Kantor keuangan atau perusahaan",
    "C. Lingkungan yang banyak berinteraksi dengan orang",
    "D. Sekolah atau lingkungan pendidikan",
    "E. Perusahaan teknologi atau digital",
    "F. Laboratorium atau industri makanan",
    "G. Rumah sakit atau fasilitas kesehatan"
]
responses['q5'] = st.radio("5. Lingkungan kerja seperti apa yang kamu bayangkan?", q5_options, key=f"q5_{key_suffix}")

q6_options = [
    "A. Bagaimana sebuah bisnis bisa sukses",
    "B. Bagaimana perusahaan mengelola uang",
    "C. Mengapa manusia memiliki perilaku yang berbeda",
    "D. Bagaimana berkomunikasi dengan orang dari berbagai negara",
    "E. Bagaimana teknologi dapat membantu kehidupan manusia",
    "F. Bagaimana makanan dibuat dan dikembangkan",
    "G. Bagaimana data kesehatan dapat membantu pelayanan pasien"
]
responses['q6'] = st.radio("6. Topik apa yang paling sering membuatmu penasaran?", q6_options, key=f"q6_{key_suffix}")

q7_options = [
    "A. Bisnis dan cara membangun usaha",
    "B. Investasi, keuangan, dan perpajakan",
    "C. Kepribadian dan perilaku manusia",
    "D. Bahasa dan komunikasi internasional",
    "E. Coding dan teknologi digital",
    "F. Inovasi produk makanan",
    "G. Sistem dan informasi pelayanan kesehatan"
]
responses['q7'] = st.radio("7. Jika memiliki waktu untuk belajar hal baru, kamu paling tertarik belajar tentang…", q7_options, key=f"q7_{key_suffix}")

st.divider()

# ---------------------------------------------------------
# 3. Tombol Eksekusi & Reset
# ---------------------------------------------------------
col1, col2 = st.columns([3, 1])

with col1:
    btn_analyze = st.button("🚀 Analisis Rekomendasi Jurusan", type="primary", use_container_width=True)

with col2:
    if st.button("🔄 Clear", use_container_width=True):
        st.session_state.form_key += 1
        st.rerun()

# ---------------------------------------------------------
# 4. Pemrosesan AI
# ---------------------------------------------------------
if btn_analyze:
    if "GROQ_API_KEY" not in st.secrets:
        st.error("GROQ_API_KEY belum ditemukan di Streamlit Secrets.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            prompt_content = f"""
            Kamu adalah konsultan akademik dan karir senior Universitas Nasional Karangturi bernama SIKUNTUL.
            Analisis pilihan kuesioner pengguna di bawah ini untuk menghasilkan **Hasil Analisis yang Komprehensif dan Terstruktur Sesuai Format Strict**.

            Pilihan Jurusan yang Tersedia:
            - S1-Manajemen
            - S1-Akuntansi
            - S1-Sistem Informasi
            - S1-Teknologi Pangan
            - S1-Psikologi
            - S1-Pendidikan Bahasa Inggris
            - S1-Manajemen Informasi Kesehatan

            Jawaban Pengguna:
            1. Aktivitas: {responses['q1']}
            2. Pekerjaan: {responses['q2']}
            3. Penanganan Masalah: {responses['q3']}
            4. Kemampuan Diri: {responses['q4']}
            5. Lingkungan Kerja: {responses['q5']}
            6. Topik Penasaran: {responses['q6']}
            7. Minat Belajar: {responses['q7']}

            WAJIB GUNAKAN FORMAT HIERARKI PENULISAN BERIKUT SECARA PERSIS:

            1. **Kesimpulan Jurusan Utama**: [Nama Jurusan]
            2. **Jurusan Alternatif**: [1-2 Nama Jurusan Cadangan]
            3. **Hasil Analisis**:
               Buatlah tabel HTML persis dengan 2 kolom: `Aspek` dan `Penjelasan`. Gunakan tag HTML `<table>`, `<tr>`, `<th>`, `<td>`, dan `<br>` agar penggantian baris di dalam sel tabel dapat dirender sempurna oleh browser.
               
               Tabel WAJIB mencakup 4 baris aspek berikut:
               <table>
                 <tr><th>Aspek</th><th>Penjelasan</th></tr>
                 <tr><td>Pola Dominasi Karakter & Minat</td><td>[Penjelasan kecenderungan profil pengguna]</td></tr>
                 <tr><td>Kesesuaian Kompetensi</td><td>• Gaya Pemecahan Masalah: [penjelasan selaras kurikulum]<br>• Kemampuan Detail/Teknis: [penjelasan mata kuliah]<br>• Ketertarikan Khusus: [penjelasan integrasi minat]</td></tr>
                 <tr><td>Alasan Pemilihan Jurusan Utama vs Alternatif</td><td>• <b>[Jurusan Utama]</b>: [alasan].<br>• <b>[Jurusan Alternatif 1]</b>: [alasan].<br>• <b>[Jurusan Alternatif 2]</b>: [alasan].</td></tr>
                 <tr><td>Rekomendasi Pengembangan Diri</td><td>1. [Langkah 1]<br>2. [Langkah 2]<br>3. [Langkah 3]</td></tr>
               </table>

            4. **Rincian Biaya**:
               Tampilkan rincian biaya Pendidikan TA 2026/2027 Universitas Nasional Karangturi dalam bentuk tabel Markdown ringkas:
               - SPI (1x bayar): Rp 4.500.000 (Dapat diangsur 3x sebelum PKKMB)
               - Inisiasi (1x bayar): Rp 1.200.000 (Orientasi, kaos, jas almamater)
               - Biaya per Semester: Rp 5.500.000 (20 SKS = Rp 4.000.000 + Daftar Ulang = Rp 1.500.000)
               Sertakan catatan ringkas biaya SKS praktikum (Rp 250.000/SKS), biaya wisuda (Rp 1.750.000), dan diskon karyawan di bawah tabel.
            """

            with st.spinner("SIKUNTUL sedang menyusun analisis terstruktur..."):
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "Kamu adalah konsultan pendidikan yang mematuhi format HTML dan Markdown dengan sangat teliti."
                        },
                        {
                            "role": "user",
                            "content": prompt_content,
                        }
                    ],
                    model="openai/gpt-oss-120b",
                    temperature=0.3,
                )
                
                result = chat_completion.choices[0].message.content
                st.success("Analisis Komprehensif Selesai!")
                st.markdown(result, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat mengonsultasikan ke AI: {e}")
