import streamlit as st
from groq import Groq

# ---------------------------------------------------------
# 1. Konfigurasi Halaman & Judul
# ---------------------------------------------------------
st.set_page_config(
    page_title="SIKUNTUL - Sistem Konsultasi Tujuan Kuliah",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 SIKUNTUL")
st.subheader("Sistem Konsultasi untuk Menentukan Tujuan Kuliah")
st.write("Pilih jawaban yang paling mencerminkan dirimu pada setiap pertanyaan berikut. AI akan menganalisis jurusan yang paling cocok untukmu!")

st.divider()

# ---------------------------------------------------------
# 2. Form Kuesioner (Dropdown Pilihan A - G)
# ---------------------------------------------------------
responses = {}

# Pertanyaan 1
q1_options = [
    "A. Mengatur kegiatan atau memimpin sebuah tim",
    "B. Menghitung dan mengelola keuangan",
    "C. Mendengarkan dan membantu orang lain",
    "D. Berkomunikasi menggunakan bahasa Inggris",
    "E. Menggunakan komputer dan teknologi",
    "F. Bereksperimen dan menciptakan produk makanan",
    "G. Mengelola informasi dan data kesehatan"
]
responses['q1'] = st.selectbox("1. Aktivitas seperti apa yang paling kamu nikmati?", q1_options)

# Pertanyaan 2
q2_options = [
    "A. Pengusaha, manager, atau business development",
    "B. Akuntan, auditor, atau financial analyst",
    "C. HR, konselor, atau bidang pengembangan manusia",
    "D. Guru, penerjemah, atau profesional bahasa",
    "E. Programmer, system analyst, atau IT",
    "F. Quality control atau pengembangan produk makanan",
    "G. Administrasi dan informasi rumah sakit"
]
responses['q2'] = st.selectbox("2. Bidang pekerjaan mana yang paling menarik perhatianmu?", q2_options)

# Pertanyaan 3
q3_options = [
    "A. Membuat strategi agar tujuan dapat tercapai",
    "B. Menganalisis angka dan data secara detail",
    "C. Memahami orang-orang yang terlibat dalam masalah tersebut",
    "D. Menjelaskan solusi kepada orang lain dengan komunikasi yang baik",
    "E. Mencari solusi menggunakan teknologi",
    "F. Melakukan penelitian atau percobaan",
    "G. Mengorganisasi dan mengelola data/informasi"
]
responses['q3'] = st.selectbox("3. Jika kamu diberi sebuah masalah, kamu lebih suka…", q3_options)

# Pertanyaan 4
q4_options = [
    "A. Memimpin dan mengambil keputusan",
    "B. Teliti terhadap angka dan detail",
    "C. Mudah memahami perasaan orang lain",
    "D. Suka berkomunikasi dan belajar bahasa",
    "E. Cepat memahami teknologi",
    "F. Suka eksperimen dan memahami proses",
    "G. Suka mengelola data dan informasi"
]
responses['q4'] = st.selectbox("4. Kemampuan apa yang paling menggambarkan dirimu?", q4_options)

# Pertanyaan 5
q5_options = [
    "A. Perusahaan atau dunia bisnis",
    "B. Kantor keuangan atau perusahaan",
    "C. Lingkungan yang banyak berinteraksi dengan orang",
    "D. Sekolah atau lingkungan pendidikan",
    "E. Perusahaan teknologi atau digital",
    "F. Laboratorium atau industri makanan",
    "G. Rumah sakit atau fasilitas kesehatan"
]
responses['q5'] = st.selectbox("5. Lingkungan kerja seperti apa yang kamu bayangkan?", q5_options)

# Pertanyaan 6
q6_options = [
    "A. Bagaimana sebuah bisnis bisa sukses",
    "B. Bagaimana perusahaan mengelola uang",
    "C. Mengapa manusia memiliki perilaku yang berbeda",
    "D. Bagaimana berkomunikasi dengan orang dari berbagai negara",
    "E. Bagaimana teknologi dapat membantu kehidupan manusia",
    "F. Bagaimana makanan dibuat dan dikembangkan",
    "G. Bagaimana data kesehatan dapat membantu pelayanan pasien"
]
responses['q6'] = st.selectbox("6. Topik apa yang paling sering membuatmu penasaran?", q6_options)

# Pertanyaan 7
q7_options = [
    "A. Bisnis dan cara membangun usaha",
    "B. Investasi, keuangan, dan perpajakan",
    "C. Kepribadian dan perilaku manusia",
    "D. Bahasa dan komunikasi internasional",
    "E. Coding dan teknologi digital",
    "F. Inovasi produk makanan",
    "G. Sistem dan informasi pelayanan kesehatan"
]
responses['q7'] = st.selectbox("7. Jika memiliki waktu untuk belajar hal baru, kamu paling tertarik belajar tentang…", q7_options)

# ---------------------------------------------------------
# 3. Analisis AI (Menggunakan Streamlit Secrets & Model Aktif)
# ---------------------------------------------------------
st.divider()

if st.button("🚀 Analisis Rekomendasi Jurusan", type="primary"):
    # Memeriksa apakah GROQ_API_KEY sudah diset di Streamlit Secrets
    if "GROQ_API_KEY" not in st.secrets:
        st.error("GROQ_API_KEY belum ditemukan di Streamlit Secrets.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            prompt_content = f"""
            Kamu adalah konsultan karir dan pendidikan tepercaya bernama SIKUNTUL.
            Analisis pilihan jawaban kuesioner pengguna berikut untuk memberikan rekomendasi jurusan kuliah yang paling cocok.

            Daftar Jurusan yang Tersedia:
            - Manajemen
            - Akuntansi
            - Psikologi
            - Pendidikan Bahasa Inggris
            - Sistem Informasi
            - Teknologi Pangan
            - Manajemen Informasi Kesehatan

            Jawaban Pengguna:
            1. Aktivitas Pilihan: {responses['q1']}
            2. Pekerjaan Pilihan: {responses['q2']}
            3. Penanganan Masalah: {responses['q3']}
            4. Kemampuan Diri: {responses['q4']}
            5. Lingkungan Kerja: {responses['q5']}
            6. Topik Penasaran: {responses['q6']}
            7. Minat Belajar: {responses['q7']}

            Format keluaran:
            1. **Kesimpulan Jurusan Utama**: [Nama Jurusan Teratas]
            2. **Jurusan Alternatif**: [1-2 Jurusan Cadangan]
            3. **Alasan Analysis**: [Penjelasan mengapa pola pilihan A-G pengguna cocok dengan jurusan tersebut]
            4. **Prospek Karir**: [3-5 contoh karir setelah lulus]
            """

            with st.spinner("SIKUNTUL sedang menganalisis pilihanmu..."):
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "Kamu adalah konsultan pendidikan tinggi yang cerdas, solutif, dan analitis."
                        },
                        {
                            "role": "user",
                            "content": prompt_content,
                        }
                    ],
                    model="openai/gpt-oss-120b",  # Model aktif sesuai lisensi Groq Anda
                    temperature=0.3,
                )
                
                result = chat_completion.choices[0].message.content
                st.success("Analisis Selesai!")
                st.markdown(result)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat mengonsultasikan ke AI: {e}")
