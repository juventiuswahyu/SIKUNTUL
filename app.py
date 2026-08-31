import streamlit as st
from groq import Groq

# ---------------------------------------------------------
# 1. Konfigurasi Halaman & Judul
# ---------------------------------------------------------
st.set_page_config(
    page_title="SIKUNTUL - Universitas Nasional Karangturi",
    page_icon="🎓",
    layout="centered"
)

# Inisialisasi state untuk mereset pilihan jika tombol clear diklik
if "form_key" not in st.session_state:
    st.session_state.form_key = 0

st.title("🎓 SIKUNTUL")
st.subheader("Sistem Konsultasi untuk Menentukan Tujuan Kuliah")
st.write("Pilih jawaban yang paling mencerminkan dirimu pada setiap pertanyaan. AI akan menganalisis jurusan yang paling cocok beserta rincian biaya pendidikannya di Universitas Nasional Karangturi!")

st.divider()

# ---------------------------------------------------------
# 2. Form Kuesioner (Dropdown Pilihan A - G)
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
responses['q1'] = st.selectbox("1. Aktivitas seperti apa yang paling kamu nikmati?", q1_options, key=f"q1_{key_suffix}")

q2_options = [
    "A. Pengusaha, manager, atau business development",
    "B. Akuntan, auditor, atau financial analyst",
    "C. HR, konselor, atau bidang pengembangan manusia",
    "D. Guru, penerjemah, atau profesional bahasa",
    "E. Programmer, system analyst, atau IT",
    "F. Quality control atau pengembangan produk makanan",
    "G. Administrasi dan informasi rumah sakit"
]
responses['q2'] = st.selectbox("2. Bidang pekerjaan mana yang paling menarik perhatianmu?", q2_options, key=f"q2_{key_suffix}")

q3_options = [
    "A. Membuat strategi agar tujuan dapat tercapai",
    "B. Menganalisis angka dan data secara detail",
    "C. Memahami orang-orang yang terlibat dalam masalah tersebut",
    "D. Menjelaskan solusi kepada orang lain dengan komunikasi yang baik",
    "E. Mencari solusi menggunakan teknologi",
    "F. Melakukan penelitian atau percobaan",
    "G. Mengorganisasi dan mengelola data/informasi"
]
responses['q3'] = st.selectbox("3. Jika kamu diberi sebuah masalah, kamu lebih suka…", q3_options, key=f"q3_{key_suffix}")

q4_options = [
    "A. Memimpin dan mengambil keputusan",
    "B. Teliti terhadap angka dan detail",
    "C. Mudah memahami perasaan orang lain",
    "D. Suka berkomunikasi dan belajar bahasa",
    "E. Cepat memahami teknologi",
    "F. Suka eksperimen dan memahami proses",
    "G. Suka mengelola data dan informasi"
]
responses['q4'] = st.selectbox("4. Kemampuan apa yang paling menggambarkan dirimu?", q4_options, key=f"q4_{key_suffix}")

q5_options = [
    "A. Perusahaan atau dunia bisnis",
    "B. Kantor keuangan atau perusahaan",
    "C. Lingkungan yang banyak berinteraksi dengan orang",
    "D. Sekolah atau lingkungan pendidikan",
    "E. Perusahaan teknologi atau digital",
    "F. Laboratorium atau industri makanan",
    "G. Rumah sakit atau fasilitas kesehatan"
]
responses['q5'] = st.selectbox("5. Lingkungan kerja seperti apa yang kamu bayangkan?", q5_options, key=f"q5_{key_suffix}")

q6_options = [
    "A. Bagaimana sebuah bisnis bisa sukses",
    "B. Bagaimana perusahaan mengelola uang",
    "C. Mengapa manusia memiliki perilaku yang berbeda",
    "D. Bagaimana berkomunikasi dengan orang dari berbagai negara",
    "E. Bagaimana teknologi dapat membantu kehidupan manusia",
    "F. Bagaimana makanan dibuat dan dikembangkan",
    "G. Bagaimana data kesehatan dapat membantu pelayanan pasien"
]
responses['q6'] = st.selectbox("6. Topik apa yang paling sering membuatmu penasaran?", q6_options, key=f"q6_{key_suffix}")

q7_options = [
    "A. Bisnis dan cara membangun usaha",
    "B. Investasi, keuangan, dan perpajakan",
    "C. Kepribadian dan perilaku manusia",
    "D. Bahasa dan komunikasi internasional",
    "E. Coding dan teknologi digital",
    "F. Inovasi produk makanan",
    "G. Sistem dan informasi pelayanan kesehatan"
]
responses['q7'] = st.selectbox("7. Jika memiliki waktu untuk belajar hal baru, kamu paling tertarik belajar tentang…", q7_options, key=f"q7_{key_suffix}")

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
# 4. Logika Pemrosesan AI dengan Informasi Biaya
# ---------------------------------------------------------
if btn_analyze:
    if "GROQ_API_KEY" not in st.secrets:
        st.error("GROQ_API_KEY belum ditemukan di Streamlit Secrets.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            prompt_content = f"""
            Kamu adalah konsultan karir dan pendaftaran mahasiswa baru Universitas Nasional Karangturi bernama SIKUNTUL.
            Analisis pilihan kuesioner pengguna berikut untuk memberikan rekomendasi jurusan kuliah beserta rincian biaya pendidikannya untuk TA 2026/2027.

            Pilihan Jurusan yang Tersedia di Universitas Nasional Karangturi:
            1. S1-Manajemen
            2. S1-Akuntansi
            3. S1-Sistem Informasi
            4. S1-Teknologi Pangan
            5. S1-Psikologi
            6. S1-Pendidikan Bahasa Inggris
            7. S1-Manajemen Informasi Kesehatan

            Pilihan Jawaban Pengguna:
            1. Aktivitas: {responses['q1']}
            2. Pekerjaan: {responses['q2']}
            3. Penanganan Masalah: {responses['q3']}
            4. Kemampuan: {responses['q4']}
            5. Lingkungan Kerja: {responses['q5']}
            6. Topik Penasaran: {responses['q6']}
            7. Minat Belajar: {responses['q7']}

            Informasi Struktur Biaya Pendidikan Universitas Nasional Karangturi TA 2026/2027 (Berlaku untuk SEMUA Jurusan):
            - SPI (Sumbangan Pengembangan Institusi) [1x Bayar Tahun Akademik]: Rp 4.500.000 (Dapat diangsur 3x sebelum PKKMB)
            - Inisiasi [1x Bayar Tahun Akademik]: Rp 1.200.000 (Orientasi, kaos, jas almamater)
            - 20 SKS (1 SKS = Rp 200.000) [Dibayarkan Setiap Semester]: Rp 4.000.000
            - Daftar Ulang [Dibayarkan Setiap Semester]: Rp 1.500.000
            - Catatan Tambahan: 
              * Biaya SKS Praktikum = Rp 250.000 / SKS
              * Biaya Cuti = Senilai biaya 4 SKS
              * Biaya Wisuda = Rp 1.750.000
              * Diskon khusus karyawan dengan menunjukkan ID card karyawan.

            Format Keluaran (Gunakan Markdown rapi dan terstruktur):
            1. **Kesimpulan Jurusan Utama**: [Nama Jurusan]
            2. **Jurusan Alternatif**: [1-2 Nama Jurusan Cadangan]
            3. **Alasan Analisis**: [Penjelasan logis kecocokan minat dengan jurusan]
            4. **Prospek Karir**: [3-5 Peluang Karir]
            5. **Rincian Biaya Pendidikan TA 2026/2027 (Universitas Nasional Karangturi)**:
               Tampilkan rincian biaya komponen di atas (SPI, Inisiasi, Biaya per Semester (SKS + Daftar Ulang)) untuk jurusan rekomendasi tersebut dalam format tabel Markdown. Sertakan juga catatan ringkas biaya wisuda/praktikum di bawahnya.
            """

            with st.spinner("SIKUNTUL sedang menganalisis rekomendasi jurusan & menyusun rincian biaya..."):
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "Kamu adalah konsultan pendidikan Universitas Nasional Karangturi yang ramah, jelas, profesional, dan detail."
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
                st.success("Analisis & Rincian Biaya Selesai!")
                st.markdown(result)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat mengonsultasikan ke AI: {e}")
