import streamlit as st
import json
import datetime
import textwrap

# Page Config
st.set_page_config(
    page_title="GuruSobat - Visual Block Planner",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Interactive Blocks / Visual Cards
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
    .badge-time {
        background-color: #FEF3C7;
        color: #92400E;
        padding: 3px 8px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
    }
    .badge-type {
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 3px 8px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
    }
    .preview-box {
        background-color: #F8FAFC;
        border-left: 6px solid #10B981;
        padding: 1.2rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://img.icons8.com/illustrations/100/teacher.png", width=80)
st.sidebar.title("GuruSobat 📚")
st.sidebar.caption("Teman Personal & Gotong Royong Guru")

menu = st.sidebar.radio(
    "Navigasi Fitur:",
    ["🧩 Visual Block Planner (Bongkar-Pasang)", "🤝 Gotong Royong Hub", "🌱 Refleksi Mikro Harian"]
)

st.sidebar.divider()
st.sidebar.info("💡 **Mode Demo Wawancara**: Ketuk balok-balok kegiatan di bawah untuk mempraktikkan bongkar-pasang RPP 1-Halaman secara visual!")

# ---------------------------------------------------------
# DATA BALOK RUBIK / KOMPONEN PEMBELAJARAN
# ---------------------------------------------------------
BALOK_OPENING = [
    {
        "id": "op_1",
        "icon": "⚡",
        "name": "Kuis Retrieval 3 Soal",
        "time": "5 Menit",
        "tag": "Individu / Otomatis",
        "desc": "Menguji ingatan materi pertemuan lalu dengan 3 pertanyaan singkat di awal kelas."
    },
    {
        "id": "op_2",
        "icon": "🎬",
        "name": "Video & Pertanyaan Pemantik",
        "time": "7 Menit",
        "tag": "Diskusi Kelas",
        "desc": "Menayangkan klip pendek 2 menit lalu mengajukan 1 pertanyaan pemancing rasa ingin tahu."
    },
    {
        "id": "op_3",
        "icon": "📸",
        "name": "Diskusi Gambar Momen Nyata",
        "time": "5 Menit",
        "tag": "Visual",
        "desc": "Menampilkan foto/isu terkini yang berkaitan erat dengan kehidupan sehari-hari siswa."
    },
    {
        "id": "op_4",
        "icon": "💡",
        "name": "Curah Pendapat Papan Tulis",
        "time": "10 Menit",
        "tag": "Interaktif",
        "desc": "Siswa menuliskan 1 kata yang mereka tahu tentang topik hari ini di papan tulis."
    }
]

BALOK_INTI = [
    {
        "id": "in_1",
        "icon": "👥",
        "name": "Diskusi Kelompok + Lembar Kerja",
        "time": "30 Menit",
        "tag": "Kolaboratif",
        "desc": "Siswa dibagi menjadi kelompok 4 orang untuk menyelesaikan studi kasus di lembar kerja ringkas."
    },
    {
        "id": "in_2",
        "icon": "🧪",
        "name": "Praktik / Eksperimen Berpasangan",
        "time": "35 Menit",
        "tag": "Praktik Langsung",
        "desc": "Siswa mencoba simulasi/alat peraga sederhana berdua untuk membuktikan konsep materi."
    },
    {
        "id": "in_3",
        "icon": "🎤",
        "name": "Studi Kasus & Presentasi Kilat 2 Menit",
        "time": "30 Menit",
        "tag": "Public Speaking",
        "desc": "Setiap kelompok menganalisis masalah nyata dan menyajikan solusinya dalam 2 menit."
    },
    {
        "id": "in_4",
        "icon": "🧩",
        "name": "Jigsaw / Kelompok Ahli",
        "time": "40 Menit",
        "tag": "Tipe Koperatif",
        "desc": "Siswa mendalami 1 sub-topik spesifik di kelompok ahli lalu mengajarkannya ke kelompok asal."
    }
]

BALOK_CLOSING = [
    {
        "id": "cl_1",
        "icon": "🎟️",
        "name": "Exit Ticket 1 Pertanyaan",
        "time": "5 Menit",
        "tag": "Evaluasi Cepat",
        "desc": "Siswa menuliskan 1 jawaban pemahaman di secarik kertas sebelum keluar kelas."
    },
    {
        "id": "cl_2",
        "icon": "💬",
        "name": "Refleksi 1 Kata Kunci",
        "time": "5 Menit",
        "tag": "Reflektif",
        "desc": "Setiap siswa bergantian menyebutkan 1 kata yang paling menggambarkan apa yang mereka pelajari."
    },
    {
        "id": "cl_3",
        "icon": "📢",
        "name": "Whole-Class Feedback (Umpan Balik Kelas)",
        "time": "10 Menit",
        "tag": "Evaluasi Bersama",
        "desc": "Guru merangkum 3 poin pemahaman terbaik dan 2 kekeliruan umum siswa hari itu."
    },
    {
        "id": "cl_4",
        "icon": "📲",
        "name": "Kuis Otomatis 5 Soal",
        "time": "8 Menit",
        "tag": "Formatif / Digital",
        "desc": "Kuis singkat seru di HP/kertas yang langsung dinilai tanpa perlu mengoreksi manual."
    }
]

# Initialize Session States for Active Blocks
def ensure_selected_block(state_key, blocks):
    selected_block = st.session_state.get(state_key)
    if not isinstance(selected_block, dict) or "id" not in selected_block:
        st.session_state[state_key] = blocks[0]


ensure_selected_block("sel_op", BALOK_OPENING)
ensure_selected_block("sel_in", BALOK_INTI)
ensure_selected_block("sel_cl", BALOK_CLOSING)

# ---------------------------------------------------------
# FITUR 1: VISUAL BLOCK PLANNER (BONGKAR-PASANG INTERAKTIF)
# ---------------------------------------------------------
if menu == "🧩 Visual Block Planner (Bongkar-Pasang)":
    st.markdown("<div class='main-header'>🧩 Visual Block Planner (RPP Bongkar-Pasang)</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Pilih dan pasang balok-balok kegiatan di bawah untuk menyusun RPP 1-Halaman secara instan!</div>", unsafe_allow_html=True)

    # Informational Recipe Presets
    st.markdown("#### ⚡ Pilih Resep Cepat Pembelajaran (Opsional):")
    p_col1, p_col2, p_col3 = st.columns(3)
    with p_col1:
        if st.button("🎯 Resep Evaluasi Kilat", use_container_width=True):
            st.session_state.sel_op = BALOK_OPENING[0]
            st.session_state.sel_in = BALOK_INTI[0]
            st.session_state.sel_cl = BALOK_CLOSING[0]
            st.toast("Resep 'Evaluasi Kilat' diterapkan!")
    with p_col2:
        if st.button("🗣️ Resep Kelas Diskusi Seru", use_container_width=True):
            st.session_state.sel_op = BALOK_OPENING[1]
            st.session_state.sel_in = BALOK_INTI[2]
            st.session_state.sel_cl = BALOK_CLOSING[1]
            st.toast("Resep 'Kelas Diskusi Seru' diterapkan!")
    with p_col3:
        if st.button("🧪 Resep Praktik & Eksperimen", use_container_width=True):
            st.session_state.sel_op = BALOK_OPENING[2]
            st.session_state.sel_in = BALOK_INTI[1]
            st.session_state.sel_cl = BALOK_CLOSING[3]
            st.toast("Resep 'Praktik & Eksperimen' diterapkan!")

    st.divider()

    # Form metadata
    col_meta1, col_meta2, col_meta3 = st.columns(3)
    with col_meta1:
        mapel = st.selectbox("Mata Pelajaran", ["IPA", "Bahasa Indonesia", "Matematika", "IPS", "Bahasa Inggris", "Guru Kelas (SD)"])
    with col_meta2:
        kelas = st.selectbox("Kelas / Jenjang", ["Kelas 4 (SD)", "Kelas 7 (SMP)", "Kelas 10 (SMA)"])
    with col_meta3:
        topik = st.text_input("Topik Pembelajaran", value="Ekosistem & Pemanasan Global")

    st.markdown("---")
    st.subheader("🎨 Papan Bongkar-Pasang Balok Kegiatan")

    # SLOT 1: PEMBUKAAN
    st.markdown("##### 📍 Slot 1: Balok Pembukaan / Apersepsi")
    cols_op = st.columns(4)
    for idx, item in enumerate(BALOK_OPENING):
        with cols_op[idx]:
            is_selected = (st.session_state.sel_op["id"] == item["id"])
            border_color = "2.5px solid #2563EB" if is_selected else "1px solid #E5E7EB"
            bg_color = "#EFF6FF" if is_selected else "#FFFFFF"

            st.markdown(textwrap.dedent(f"""
            <div style="border:{border_color}; background-color:{bg_color}; padding:0.8rem; border-radius:10px; height:170px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.3rem;">
                    <span style="font-size:1.3rem;">{item['icon']}</span>
                    <span class="badge-time">{item['time']}</span>
                </div>
                <div style="font-weight:700; font-size:0.9rem; color:#1E293B;">{item['name']}</div>
                <div style="font-size:0.75rem; color:#64748B; margin-top:0.3rem;">{item['desc']}</div>
            </div>
            """), unsafe_allow_html=True)
            if st.button(f"{'✅ Terpasang' if is_selected else '➕ Pasang Balok'}", key=f"btn_op_{item['id']}", use_container_width=True):
                st.session_state.sel_op = item
                st.rerun()

    # SLOT 2: INTI
    st.markdown("##### 📍 Slot 2: Balok Kegiatan Inti")
    cols_in = st.columns(4)
    for idx, item in enumerate(BALOK_INTI):
        with cols_in[idx]:
            is_selected = (st.session_state.sel_in["id"] == item["id"])
            border_color = "2.5px solid #2563EB" if is_selected else "1px solid #E5E7EB"
            bg_color = "#EFF6FF" if is_selected else "#FFFFFF"

            st.markdown(textwrap.dedent(f"""
            <div style="border:{border_color}; background-color:{bg_color}; padding:0.8rem; border-radius:10px; height:170px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.3rem;">
                    <span style="font-size:1.3rem;">{item['icon']}</span>
                    <span class="badge-time">{item['time']}</span>
                </div>
                <div style="font-weight:700; font-size:0.9rem; color:#1E293B;">{item['name']}</div>
                <div style="font-size:0.75rem; color:#64748B; margin-top:0.3rem;">{item['desc']}</div>
            </div>
            """), unsafe_allow_html=True)
            if st.button(f"{'✅ Terpasang' if is_selected else '➕ Pasang Balok'}", key=f"btn_in_{item['id']}", use_container_width=True):
                st.session_state.sel_in = item
                st.rerun()

    # SLOT 3: PENUTUP
    st.markdown("##### 📍 Slot 3: Balok Penutup & Evaluasi")
    cols_cl = st.columns(4)
    for idx, item in enumerate(BALOK_CLOSING):
        with cols_cl[idx]:
            is_selected = (st.session_state.sel_cl["id"] == item["id"])
            border_color = "2.5px solid #2563EB" if is_selected else "1px solid #E5E7EB"
            bg_color = "#EFF6FF" if is_selected else "#FFFFFF"

            st.markdown(textwrap.dedent(f"""
            <div style="border:{border_color}; background-color:{bg_color}; padding:0.8rem; border-radius:10px; height:170px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.3rem;">
                    <span style="font-size:1.3rem;">{item['icon']}</span>
                    <span class="badge-time">{item['time']}</span>
                </div>
                <div style="font-weight:700; font-size:0.9rem; color:#1E293B;">{item['name']}</div>
                <div style="font-size:0.75rem; color:#64748B; margin-top:0.3rem;">{item['desc']}</div>
            </div>
            """), unsafe_allow_html=True)
            if st.button(f"{'✅ Terpasang' if is_selected else '➕ Pasang Balok'}", key=f"btn_cl_{item['id']}", use_container_width=True):
                st.session_state.sel_cl = item
                st.rerun()

    # LIVE PREVIEW OF ASSEMBLED RPP
    st.markdown("---")
    st.subheader("📄 Hasil Rangka Pembelajaran (Live Preview)")

    op_sel = st.session_state.sel_op
    in_sel = st.session_state.sel_in
    cl_sel = st.session_state.sel_cl

    st.markdown(textwrap.dedent(f"""
    <div class='preview-box'>
        <h3 style='margin-top:0; color:#0F172A;'>📄 RPP 1-HALAMAN: {mapel} - {topik} ({kelas})</h3>
        <p style='color:#475569;'><b>Estimasi Total Waktu:</b> 45-60 Menit | <b>Format:</b> Modular Ringkas</p>
        <hr style='border-top: 1px solid #CBD5E1;'>
        <p><b>1. PEMBUKAAN ({op_sel['time']}):</b> {op_sel['icon']} <b>{op_sel['name']}</b><br>
        <span style='color:#64748B; font-size:0.9rem;'>{op_sel['desc']}</span></p>

        <p><b>2. KEGIATAN INTI ({in_sel['time']}):</b> {in_sel['icon']} <b>{in_sel['name']}</b><br>
        <span style='color:#64748B; font-size:0.9rem;'>{in_sel['desc']}</span></p>

        <p><b>3. PENUTUP & ASESMEN ({cl_sel['time']}):</b> {cl_sel['icon']} <b>{cl_sel['name']}</b><br>
        <span style='color:#64748B; font-size:0.9rem;'>{cl_sel['desc']}</span></p>
        <hr style='border-top: 1px solid #CBD5E1;'>
        <small style='color:#059669;'><b>✓ Siap Mengajar:</b> Rangka ini siap langsung dipakai mengajar tanpa narasi administratif berbelit-belit.</small>
    </div>
    """), unsafe_allow_html=True)

    rpp_text = f"""==================================================
RPP 1-HALAMAN GURUSOBAT (BONGKAR-PASANG)
==================================================
Mata Pelajaran : {mapel}
Kelas / Jenjang : {kelas}
Topik          : {topik}
Tanggal        : {datetime.date.today().strftime('%d %B %Y')}

1. PEMBUKAAN ({op_sel['time']}):
   {op_sel['icon']} {op_sel['name']}
   Detail: {op_sel['desc']}

2. KEGIATAN INTI ({in_sel['time']}):
   {in_sel['icon']} {in_sel['name']}
   Detail: {in_sel['desc']}

3. PENUTUP & EVALUASI ({cl_sel['time']}):
   {cl_sel['icon']} {cl_sel['name']}
   Detail: {cl_sel['desc']}

==================================================
Dibuat dengan GuruSobat - Teman Personal & Gotong Royong Guru
"""

    st.download_button(
        label="📥 Unduh RPP 1-Halaman (.txt)",
        data=rpp_text,
        file_name=f"RPP_BongkarPasang_{topik.replace(' ', '_')}.txt",
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
                "title": "Balok RPP Praktis Pembelajaran Berbasis Proyek (PJBL)",
                "author": "Bu Maya (Guru SD Kelas 5)",
                "desc": "Rangka 1-halaman proyek daur ulang sampah kelas 5.",
                "tag": "Rangka RPP",
                "likes": 215,
                "remix": 64
            }
        ]

        for r in resources:
            st.markdown(textwrap.dedent(f"""
            <div style='background-color:#F8FAFC; border:1px solid #E2E8F0; padding:1.2rem; border-radius:10px; margin-bottom:1rem;'>
                <span class='badge-type'>{r['tag']}</span>
                <h4 style='margin-top:0.5rem; margin-bottom:0.2rem;'>{r['title']}</h4>
                <p style='color:#6B7280; font-size:0.85rem; margin-bottom:0.5rem;'>Oleh: <b>{r['author']}</b></p>
                <p style='font-size:0.95rem;'>{r['desc']}</p>
                <p style='font-size:0.85rem; color:#1D4ED8;'>❤️ {r['likes']} Menyukai | 🔄 {r['remix']} Guru Telah Menyalin (Remix)</p>
            </div>
            """), unsafe_allow_html=True)
            if st.button(f"📥 Remix / Gunakan '{r['title']}'", key=r['title']):
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
