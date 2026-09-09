import streamlit as st
import json
import datetime

# Page Config
st.set_page_config(
    page_title="GuruSobat MVP Prototype",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling for Warm & Clean Educator Vibe
st.markdown("""
<style>
    .main-header {
        font-size: 2rem;
        color: #1E3A8A;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: #F3F4F6;
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 5px solid #3B82F6;
    }
    .tag {
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 3px 8px;
        border-radius: 5px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .card h3, .card h4, .card p, .card small {
        overflow-wrap: anywhere;
        word-break: break-word;
    }
    @media (max-width: 700px) {
        [data-testid="stAppViewContainer"] .main .block-container {
            padding: 1rem 0.75rem 3rem;
        }
        .main-header {
            font-size: 1.35rem;
            line-height: 1.25;
        }
        .sub-header {
            font-size: 0.9rem;
            line-height: 1.4;
            margin-bottom: 1rem;
        }
        .card {
            padding: 0.9rem;
        }
        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] h3,
        [data-testid="stMarkdownContainer"] h4 {
            overflow-wrap: anywhere;
            word-break: break-word;
        }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://img.icons8.com/illustrations/100/teacher.png", width=80)
st.sidebar.title("GuruSobat 📚")
st.sidebar.caption("Teman Setia & Produktivitas Guru")

menu = st.sidebar.radio(
    "Navigasi Fitur:",
    ["✨ Skeletal Planner (RPP 1-Hal)", "🤝 Gotong Royong Hub", "🌱 Refleksi Mikro Harian"]
)

st.sidebar.divider()
st.sidebar.info("💡 **Mode Demo Wawancara**: Tunjukkan antarmuka ini kepada 3-5 guru target untuk menguji alur kerja mereka.")

# ---------------------------------------------------------
# FITUR 1: SKELETAL PLANNER
# ---------------------------------------------------------
if menu == "✨ Skeletal Planner (RPP 1-Hal)":
    st.markdown("<div class='main-header'>✨ Skeletal Planner</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Buat draf rangka pembelajaran 1-halaman dalam kurun waktu kurang dari 3 menit!</div>", unsafe_allow_html=True)

    with st.form("planner_form"):
        col1, col2 = st.columns(2)
        with col1:
            mapel = st.selectbox("Mata Pelajaran", ["IPA", "Bahasa Indonesia", "Matematika", "IPS", "Bahasa Inggris", "Guru Kelas (SD)"])
            kelas = st.selectbox("Kelas / Jenjang", ["Kelas 4 (SD)", "Kelas 7 (SMP)", "Kelas 10 (SMA)"])
        with col2:
            topik = st.text_input("Topik Materi", value="Ekosistem & Pemanasan Global")
            durasi = st.selectbox("Alokasi Waktu", ["2 x 45 Menit", "3 x 40 Menit", "2 x 35 Menit"])

        st.markdown("---")
        st.subheader("🧩 Bongkar-Pasang Komponen Pembelajaran")

        apersepsi = st.selectbox(
            "1. Pembukaan / Apersepsi (5-10 Menit)",
            [
                "Kuis Singkat Retrieval (3 Soal ingatan materi lalu)",
                "Pematik Video Singkat & Pertanyaan Pemantik",
                "Diskusi Gambar Momen Nyata",
                "Brainstorming Curah Pendapat Papan Tulis"
            ]
        )

        inti = st.selectbox(
            "2. Kegiatan Inti (30-40 Menit)",
            [
                "Diskusi Kelompok Kecil + Lembar Kerja Singkat",
                "Praktik / Eksperimen Sederhana Berpasangan",
                "Studi Kasus & Presentasi Kilat 2 Menit",
                "Jigsaw / Kelompok Ahli"
            ]
        )

        penutup = st.selectbox(
            "3. Penutup & Evaluasi (10 Menit)",
            [
                "Exit Ticket (1 Pertanyaan Pemahaman di Kertas)",
                "Refleksi 1 Kata Kunci Masing-Masing Siswa",
                "Umpan Balik Kelas (Whole-Class Feedback)",
                "Kuis Otomatis 5 Soal"
            ]
        )

        submitted = st.form_submit_button("🚀 Buat Rangka Pembelajaran Sekarang", use_container_width=True)

    if submitted:
        st.success("🎉 Rangka Pembelajaran Berhasil Dibuat!")
        st.markdown(f"""
        <div class='card'>
            <h3>📄 {mapel} - {topik} ({kelas})</h3>
            <p><b>Alokasi Waktu:</b> {durasi}</p>
            <hr>
            <p><b>1. Pembukaan (Apersepsi):</b> {apersepsi}</p>
            <p><b>2. Kegiatan Inti:</b> {inti}</p>
            <p><b>3. Penutup & Asesmen:</b> {penutup}</p>
            <hr>
            <small><i>Format terstandar 1-halaman siap cetak / disimpan tanpa narasi berbelit-belit.</i></small>
        </div>
        """, unsafe_allow_html=True)
        st.download_button(
            label="📥 Unduh RPP 1-Halaman (.txt)",
            data=f"RPP 1-HALAMAN GURUSOBAT\nMapel: {mapel}\nTopik: {topik}\nKelas: {kelas}\n\n1. Buka: {apersepsi}\n2. Inti: {inti}\n3. Penutup: {penutup}",
            file_name=f"RPP_{topik}.txt",
            mime="text/plain"
        )

# ---------------------------------------------------------
# FITUR 2: GOTONG ROYONG HUB
# ---------------------------------------------------------
elif menu == "🤝 Gotong Royong Hub":
    st.markdown("<div class='main-header'>🤝 Gotong Royong Resource Hub</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Saling berbagi, menyalin (remix), dan menghemat waktu antar-sesama rekan guru.</div>", unsafe_allow_html=True)

    st.text_input("🔍 Cari rubrik, kuis, atau RPP dari rekan guru lain...", placeholder="Contoh: Rubrik Esai, Kuis IPA Kelas 7...")

    tab1, tab2 = st.tabs(["🔥 Terpopuler Minggu Ini", "📤 Bagikan Materi Saya"])

    with tab1:
        resources = [
            {
                "title": "Single-Point Rubric Penilaian Esai / Karangan",
                "author": "Bu Ratna (Guru Bahasa Indonesia)",
                "desc": "Hanya menilai kriteria profisiensi utama. Berhasil memotong waktu koreksi 120 esai siswa hingga 60%.",
                "tag": "Rubrik Penilaian",
                "likes": 142,
                "remix": 38
            },
            {
                "title": "Bank Kuis Retrieval: Ekosistem (5 Soal Pilihan Ganda)",
                "author": "Pak Agus (Guru IPA SMP)",
                "desc": "Kuis pematik awal kelas untuk menguji ingatan materi minggu lalu. Siap pakai.",
                "tag": "Kuis Retrieval",
                "likes": 98,
                "remix": 25
            },
            {
                "title": "Rangka RPP Praktis Pembelajaran Berbasis Proyek (PJBL)",
                "author": "Bu Maya (Guru SD Kelas 5)",
                "desc": "Rangka 1-halaman proyek daur ulang sampah kelas 5.",
                "tag": "Rangka RPP",
                "likes": 215,
                "remix": 64
            }
        ]

        for r in resources:
            st.markdown(f"""
            <div class='card'>
                <span class='tag'>{r['tag']}</span>
                <h4 style='margin-top:0.5rem; margin-bottom:0.2rem;'>{r['title']}</h4>
                <p style='color:#6B7280; font-size:0.85rem; margin-bottom:0.5rem;'>Oleh: <b>{r['author']}</b></p>
                <p style='font-size:0.95rem;'>{r['desc']}</p>
                <p style='font-size:0.85rem; color:#1D4ED8;'>❤️ {r['likes']} Menyukai | 🔄 {r['remix']} Guru Telah Menyalin (Remix)</p>
            </div>
            """, unsafe_allow_html=True)
            col_a, col_b = st.columns([1, 4])
            with col_a:
                if st.button("📥 Remix / Gunakan", key=r['title']):
                    st.success(f"Materi '{r['title']}' berhasil disalin ke koleksi pribadi Anda!")

    with tab2:
        st.subheader("Bagikan Modul Ajar / Rubrik Anda")
        res_title = st.text_input("Judul Materi")
        res_type = st.selectbox("Jenis Materi", ["Rubrik Penilaian", "Kuis Retrieval", "Rangka RPP", "Lembar Kerja"])
        res_desc = st.text_area("Deskripsi Singkat & Ringkasan")
        if st.button("🚀 Publish ke Gotong Royong Hub"):
            st.success("Materi Anda berhasil dibagikan! Terima kasih sudah membantu rekan guru lain.")

# ---------------------------------------------------------
# FITUR 3: REFLEKSI MIKRO HARIAN
# ---------------------------------------------------------
elif menu == "🌱 Refleksi Mikro Harian":
    st.markdown("<div class='main-header'>🌱 Refleksi Mikro & Ruang Bahagia</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Apresiasi diri dan catat keberhasilan kecil Anda hari ini.</div>", unsafe_allow_html=True)

    st.subheader("Bagaimana perasaan Anda mengajar hari ini?")
    mood = st.select_slider(
        "Skala Energi & Mood:",
        options=["🪫 Sangat Lelah", "🙁 Agak Berat", "😐 Cukup Baik", "🙂 Semangat", "🌟 Sangat Memuaskan"]
    )

    st.subheader("🎉 1 Keberhasilan Kecil Hari Ini (Small Win)")
    win = st.text_area(
        "Apa momen positif bersama murid atau rekan guru yang membuat Anda tersenyum hari ini?",
        placeholder="Contoh: Budi yang biasanya diam hari ini berhasil menjawab kuis dengan percaya diri!"
    )

    if st.button("💾 Simpan Refleksi Hari Ini"):
        st.balloons()
        st.success("Refleksi Anda tersimpan! Ingat, dedikasi Anda sangat berarti bagi masa depan murid-murid Anda.")
