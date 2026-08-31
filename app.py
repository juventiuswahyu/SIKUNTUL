import os
import streamlit as st
from groq import Groq

# ---------------------------------------------------------
# 1. Konfigurasi Halaman & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="SIKUNTUL - Sistem Konsultasi Tujuan Kuliah",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 SIKUNTUL")
st.subheader("Sistem Konsultasi untuk Menentukan Tujuan Kuliah")
st.write("Temukan rekomendasi jurusan kuliah yang paling sesuai dengan minat dan kepribadianmu!")

# Input API Key Groq pada Sidebar
with st.sidebar:
    st.header("⚙️ Konfigurasi API")
    groq_api_key = st.text_input("Masukkan Groq API Key:", type="password")
    selected_model = st.selectbox(
        "Pilih Model Groq:",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "openai/gpt-oss-120b", "openai/gpt-oss-20b"]
    )
    st.info("Kunci API Groq diperlukan untuk memproses analisis AI secara mendalam.")

# ---------------------------------------------------------
# 2. Pemilihan Metode Kuesioner
# ---------------------------------------------------------
metode = st.radio(
    "Pilih Metode Kuesioner:",
    ["Metode 1: Jawaban Isian / Deskriptif", "Metode 2: Pilihan Ganda (Terstruktur)"],
    index=0
)

st.divider()

# ---------------------------------------------------------
# 3. Form Input Berdasarkan Metode
# ---------------------------------------------------------
responses = {}

if "Metode 1" in metode:
    st.markdown("### 📝 Metode 1: Jawab pertanyaan berikut sesuai pandanganmu")
    
    responses['q1'] = st.text_area("1. Aktivitas seperti apa yang paling kamu nikmati?")
    responses['q2'] = st.text_area("2. Bidang pekerjaan apa yang paling menarik perhatianmu?")
    responses['q3'] = st.text_area("3. Jika kamu diberi sebuah masalah, kamu lebih suka...")
    responses['q4'] = st.text_area("4. Kemampuan apa yang paling menggambarkan dirimu?")
    responses['q5'] = st.text_area("5. Lingkungan kerja seperti apa yang kamu bayangkan?")
    responses['q6'] = st.text_area("6. Topik apa yang paling sering membuatmu penasaran?")
    responses['q7'] = st.text_area("7. Jika memiliki waktu untuk belajar hal baru, kamu paling tertarik belajar tentang?")

else:
    st.markdown("### 🔘 Metode 2: Pilih jawaban yang paling sesuai")

    options_q1 = {
        "A. Mengatur kegiatan atau memimpin sebuah tim": "Manajemen",
        "B. Menghitung dan mengelola keuangan": "Akuntansi",
        "C. Mendengarkan dan membantu orang lain": "Psikologi",
        "D. Berkomunikasi menggunakan bahasa Inggris": "Pendidikan Bahasa Inggris",
        "E. Menggunakan komputer dan teknologi": "Sistem Informasi",
        "F. Bereksperimen dan menciptakan produk makanan": "Teknologi Pangan",
        "G. Mengelola informasi dan data kesehatan": "Manajemen Informasi Kesehatan"
    }
    responses['q1'] = st.selectbox("1. Aktivitas seperti apa yang paling kamu nikmati?", list(options_q1.keys()))

    options_q2 = {
        "A. Pengusaha, manager, atau business development": "Manajemen",
        "B. Akuntan, auditor, atau financial analyst": "Akuntansi",
        "C. HR, konselor, atau bidang pengembangan manusia": "Psikologi",
        "D. Guru, penerjemah, atau profesional bahasa": "Pendidikan Bahasa Inggris",
        "E. Programmer, system analyst, atau IT": "Sistem Informasi",
        "F. Quality control atau pengembangan produk makanan": "Teknologi Pangan",
        "G. Administrasi dan informasi rumah sakit": "Manajemen Informasi Kesehatan"
    }
    responses['q2'] = st.selectbox("2. Bidang pekerjaan mana yang paling menarik perhatianmu?", list(options_q2.keys()))

    options_q3 = {
        "A. Membuat strategi agar tujuan dapat tercapai": "Manajemen",
        "B. Menganalisis angka dan data secara detail": "Akuntansi",
        "C. Memahami orang-orang yang terlibat dalam masalah tersebut": "Psikologi",
        "D. Menjelaskan solusi kepada orang lain dengan komunikasi yang baik": "Pendidikan Bahasa Inggris",
        "E. Mencari solusi menggunakan teknologi": "Sistem Informasi",
        "F. Melakukan penelitian atau percobaan": "Teknologi Pangan",
        "G. Mengorganisasi dan mengelola data/informasi": "Manajemen Informasi Kesehatan"
    }
    responses['q3'] = st.selectbox("3. Jika kamu diberi sebuah masalah, kamu lebih suka…", list(options_q3.keys()))

    options_q4 = {
        "A. Memimpin dan mengambil keputusan": "Manajemen",
        "B. Teliti terhadap angka dan detail": "Akuntansi",
        "C. Mudah memahami perasaan orang lain": "Psikologi",
        "D. Suka berkomunikasi dan belajar bahasa": "Pendidikan Bahasa Inggris",
        "E. Cepat memahami teknologi": "Sistem Informasi",
        "F. Suka eksperimen dan memahami proses": "Teknologi Pangan",
        "G. Suka mengelola data dan informasi": "Manajemen Informasi Kesehatan"
    }
    responses['q4'] = st.selectbox("4. Kemampuan apa yang paling menggambarkan dirimu?", list(options_q4.keys()))

    options_q5 = {
        "A. Perusahaan atau dunia bisnis": "Manajemen",
        "B. Kantor keuangan atau perusahaan": "Akuntansi",
        "C. Lingkungan yang banyak berinteraksi dengan orang": "Psikologi",
        "D. Sekolah atau lingkungan pendidikan": "Pendidikan Bahasa Inggris",
        "E. Perusahaan teknologi atau digital": "Sistem Informasi",
        "F. Laboratorium atau industri makanan": "Teknologi Pangan",
        "G. Rumah sakit atau fasilitas kesehatan": "Manajemen Informasi Kesehatan"
    }
    responses['q5'] = st.selectbox("5. Lingkungan kerja seperti apa yang kamu bayangkan?", list(options_q5.keys()))

    options_q6 = {
        "A. Bagaimana sebuah bisnis bisa sukses": "Manajemen",
        "B. Bagaimana perusahaan mengelola uang": "Akuntansi",
        "C. Mengapa manusia memiliki perilaku yang berbeda": "Psikologi",
        "D. Bagaimana berkomunikasi dengan orang dari berbagai negara": "Pendidikan Bahasa Inggris",
        "E. Bagaimana teknologi dapat membantu kehidupan manusia": "Sistem Informasi",
        "F. Bagaimana makanan dibuat dan dikembangkan": "Teknologi Pangan",
        "G. Bagaimana data kesehatan dapat membantu pelayanan pasien": "Manajemen Informasi Kesehatan"
    }
    responses['q6'] = st.selectbox("6. Topik apa yang paling sering membuatmu penasaran?", list(options_q6.keys()))

    options_q7 = {
        "A. Bisnis dan cara membangun usaha": "Manajemen",
        "B. Investasi, keuangan, dan perpajakan": "Akuntansi",
        "C. Kepribadian dan perilaku manusia": "Psikologi",
        "D. Bahasa dan komunikasi internasional": "Pendidikan Bahasa Inggris",
        "E. Coding dan teknologi digital": "Sistem Informasi",
        "F. Inovasi produk makanan": "Teknologi Pangan",
        "G. Sistem dan informasi pelayanan kesehatan": "Manajemen Informasi Kesehatan"
    }
    responses['q7'] = st.selectbox("7. Jika memiliki waktu untuk belajar hal baru, kamu paling tertarik belajar tentang…", list(options_q7.keys()))

# ---------------------------------------------------------
# 4. Logika Pemrosesan AI dengan Groq
# ---------------------------------------------------------
if st.button("🚀 Analisis Rekomendasi Jurusan", type="primary"):
    if not groq_api_key:
        st.error("Silakan masukkan Groq API Key terlebih dahulu di menu samping (sidebar).")
    else:
        try:
            client = Groq(api_key=groq_api_key)
            
            # Format Prompt
            prompt_content = f"""
            Kamu adalah konsultan karir dan pendidikan tepercaya bernama SIKUNTUL.
            Analisis jawaban kuesioner pengguna di bawah ini untuk menentukan jurusan kuliah yang paling cocok.
            
            Pilihan Jurusan yang Tersedia:
            1. Manajemen
            2. Akuntansi
            3. Psikologi
            4. Pendidikan Bahasa Inggris
            5. Sistem Informasi
            6. Teknologi Pangan
            7. Manajemen Informasi Kesehatan

            Hasil Jawaban Pengguna:
            - Pertanyaan 1: {responses['q1']}
            - Pertanyaan 2: {responses['q2']}
            - Pertanyaan 3: {responses['q3']}
            - Pertanyaan 4: {responses['q4']}
            - Pertanyaan 5: {responses['q5']}
            - Pertanyaan 6: {responses['q6']}
            - Pertanyaan 7: {responses['q7']}

            Berikan output dengan format ringkas:
            1. **Jurusan Utama yang Direkomendasikan**: (Tentukan 1 jurusan paling cocok)
            2. **Jurusan Alternatif**: (1-2 jurusan cadangan yang cocok)
            3. **Analisis Alasan**: (Penjelasan mengapa rekomendasi tersebut sesuai berdasarkan profil jawaban pengguna)
            4. **Peluang Karir**: (Daftar opsi karir setelah lulus)
            """

            with st.spinner("SIKUNTUL sedang menganalisis pilihanmu..."):
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "Kamu adalah konsultan pendidikan tinggi yang ramah, komunikatif, dan solutif."
                        },
                        {
                            "role": "user",
                            "content": prompt_content,
                        }
                    ],
                    model=selected_model,
                    temperature=0.5,
                )
                
                result = chat_completion.choices[0].message.content
                st.success("Analisis Selesai!")
                st.markdown("---")
                st.markdown(result)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat menghubungi API Groq: {e}")
