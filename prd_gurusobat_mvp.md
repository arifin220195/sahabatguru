# Product Requirement Document (PRD)
## Nama Sandi Proyek: "GuruSobat" (MVP - Pondasi Awal)
**Versi:** 1.0 (Draf Awal untuk Evaluasi)  
**Tanggal:** 8 September 2026  
**Penulis:** Gemini Notebook & Kolaborator  

---

### 1. Latar Belakang & Masalah (Background & Problem Statement)
Beban kerja guru di berbagai belahan dunia, termasuk Indonesia, telah mencapai tingkat yang mengkhawatirkan [1, 61, 71]. Berdasarkan data penelitian, guru rata-rata bekerja sekitar 53 jam per minggu, dengan 84% di antaranya menyatakan bahwa jam kerja standar sekolah tidak pernah cukup untuk menyelesaikan tugas perencanaan mengajar, koreksi, dan komunikasi [1, 2]. 

Di Indonesia, problematika ini sangat nyata. Tuntutan administratif yang tinggi (terutama terkait pelaporan kurikulum formal seperti Kurikulum Merdeka) sering kali melampaui batas kemampuan waktu guru, sehingga menurunkan fokus mereka pada kegiatan belajar-mengajar (KBM) yang esensial [59, 65, 71]. Kurangnya waktu untuk refleksi diri, keterbatasan dukungan sosial, serta jam mengajar yang padat (sering kali melebihi 24 jam tatap muka per minggu) berkontribusi langsung pada penurunan kesejahteraan psikologis (*psychological well-being*), kelelahan emosional, dan kejenuhan (*burnout*) [71].

**Kesenjangan Produk Saat Ini:**
*   **Aplikasi Sekolah Formal (LMS/Portal Resmi):** Berorientasi pada kepatuhan administrasi (*compliance*) dan birokrasi, bukan dirancang untuk kenyamanan atau efisiensi harian guru [65, 66].
*   **Alat Produktivitas Umum (Notion, Slack, Trello):** Sangat kuat namun memerlukan kemampuan teknis tinggi dan waktu luang untuk dikonfigurasi secara manual, sesuatu yang justru tidak dimiliki oleh guru yang sudah lelah [60, 66].

Oleh karena itu, ada peluang besar untuk membangun **"GuruSobat"**, sebuah pusat kendali pribadi (*Personal Command Center*) yang ramah, fleksibel, mobile-first, dan sepenuhnya independen dari sistem birokrasi sekolah formal [66].

---

### 2. Visi & Tujuan Produk (Product Vision & Objectives)
*   **Visi:** Menjadi sahabat digital harian guru yang meringankan beban administratif dan memulihkan kegembiraan mereka dalam mendidik anak bangsa melalui produktivitas mandiri dan kolaborasi yang hangat.
*   **Tujuan MVP (Minimum Viable Product):**
    1.  Membantu guru memotong waktu perencanaan materi dan koreksi tugas harian secara mandiri [9, 32].
    2.  Menyediakan wadah kolaborasi informal (*gotong royong*) yang instan antar-rekan sejawat tanpa birokrasi institusional [49, 61, 67].
    3.  Meningkatkan rasa percaya diri (*self-efficacy*) dan kesehatan mental guru melalui fitur refleksi harian yang sederhana [51, 62, 71].

---

### 3. Target Pengguna & Persona (Target Audience & Persona)
*   **Primary User:** Guru K-12 (SD, SMP, SMA/SMK) di Indonesia yang merasa kelelahan akibat tugas administratif namun tetap berdedikasi tinggi pada proses belajar siswa mereka [61, 71].
*   **Karakteristik Utama:**
    *   Menginginkan alat yang *langsung pakai* tanpa perlu proses belajar yang rumit.
    *   Lebih sering mengakses internet melalui ponsel pintar daripada komputer (mobile-first).
    *   Secara alami senang berbagi dan berkolaborasi dengan rekan kerja secara informal (misal: lewat WhatsApp grup atau obrolan ruang guru) [49, 61, 67].

---

### 4. Batasan Produk (Product Scope & Out of Scope)
*   **In-Scope (MVP):**
    *   Alat bantu produktivitas personal guru (lesson planning, grading support) [9, 32].
    *   Kolaborasi interpersonal yang bersifat kasual, sukarela, dan peer-to-peer [67].
    *   Penyimpanan berbasis cloud yang fleksibel dan dapat diakses kapan saja [63].
*   **Out of Scope (Fase Selanjutnya):**
    *   Integrasi resmi dengan sistem nilai raport Dapodik atau platform resmi kementerian.
    *   Sistem absensi sekolah atau penilaian resmi kepala sekolah.
    *   Fitur berbayar/e-commerce bahan ajar skala besar (fokus awal adalah gotong royong non-komersial) [67].

---

### 5. Arsitektur MVP & Detail Fitur Utama (MVP Features)

#### Modul A: Asisten Produktivitas Mandiri (Personal Productivity Hub)
Modul ini bertujuan untuk memotong durasi persiapan mengajar dan koreksi yang merupakan penyita waktu terbesar guru [9, 32].

*   **Fitur A.1: Skeletal Planner (Rencana Pembelajaran Ringkas)**
    *   *Deskripsi:* Templat satu halaman terstruktur berbasis "kolom bongkar-pasang" (do-now, penjelasan materi, kegiatan kelompok, exit ticket) untuk menggantikan format administratif naratif panjang yang kaku [32, 33].
    *   *Alur Pengguna:* Guru memilih templat kerangka dasar, memasukkan teks pokok materi, lalu langsung mengekspor menjadi draf presentasi atau dokumen ringkas siap pakai [32, 33].
*   **Fitur A.2: Smart Comment Bank & Quick Grading Rubric**
    *   *Deskripsi:* Penyimpan template umpan balik (*comment banks*) dan rubrik satu kriteria (*single-point rubric*) [9]. Membantu guru fokus menilai kriteria esensial saja alih-alih mengoreksi semua detail draf yang berulang, yang terbukti memangkas waktu menilai secara signifikan [9, 10].
    *   *Alur Pengguna:* Guru menyimpan daftar komentar umpan balik yang sering dipakai, lalu dapat menyalinnya dalam sekali klik untuk dikirimkan ke WhatsApp atau LMS eksternal yang mereka pakai.

#### Modul B: Ruang "Gotong Royong" (Informal Peer Collaboration)
Penelitian membuktikan bahwa kolaborasi informal antar-guru dalam membagi tugas dan menyusun materi pembelajaran adalah strategi coping paling efektif dalam mengurangi stres administratif [49, 61, 67].

*   **Fitur B.1: Berbagi Kasual (Gotong Royong Resource Bank)**
    *   *Deskripsi:* Ruang berbagi modular yang sangat sederhana di mana sekelompok kecil guru (misal, guru kelas 4 di satu wilayah atau sekolah) dapat saling mengunggah, melihat, dan menduplikasi materi ajar, rubrik, atau kuis buatan rekan sejawat mereka [24, 67].
    *   *Alur Pengguna:* Guru dapat menekan tombol "Salin ke Dasbor Saya" pada modul ajar yang dibagikan temannya, lalu menyesuaikannya sedikit untuk digunakan di kelas mereka sendiri [24, 67].

#### Modul C: Teman Sehat Mental (Well-being & Empathy Companion)
Kesejahteraan psikologis guru menurun drastis akibat kurangnya dukungan sosial dan minimnya waktu untuk refleksi psikologis pribadi [71].

*   **Fitur C.1: Refleksi Mikro Harian (Micro-Journaling)**
    *   *Deskripsi:* Prompt harian yang sangat cepat (membutuhkan waktu kurang dari 2 menit) untuk memandu guru mencatat 1 momen positif, keberhasilan kecil, atau ekspresi syukur bersama siswa hari itu untuk membangun kembali rasa keberdayaan diri (*self-efficacy*) [51, 62, 71].
*   **Fitur C.2: Apresiasi Sejawat (Peer Micro-Affirmations)**
    *   *Deskripsi:* Fitur bertukar kartu ucapan terima kasih digital antarguru secara kasual, bertujuan memulihkan hubungan emosional interpersonal yang kerap tergerus oleh stres kerja [62, 68].

---

### 6. Metrik Keberhasilan MVP (Success Metrics)
1.  **Time Saved Metric:** Estimasi waktu persiapan dan koreksi guru berkurang minimal 3-4 jam per minggu [4].
2.  **Product Utility:** Rasio fitur produktivitas (Modul A) yang berhasil diekspor atau disalin oleh pengguna ke aktivitas mengajar mereka yang sesungguhnya.
3.  **Active Collaboration Rate:** Jumlah file/materi yang saling dibagikan dan didekorasi ulang (*remix*) dalam modul Gotong Royong [64].
4.  **Well-being Pulse Check:** Peningkatan skor evaluasi kepuasan diri (*self-efficacy*) guru secara berkala setelah konsisten menggunakan fitur refleksi mikro [62, 71].

---

### 7. Rencana Tindak Lanjut & Evaluasi Iteratif
Dokumen ini dirancang sebagai fondasi awal. Langkah berikutnya adalah:
1.  **Analisis Teknis:** Memilih tumpukan teknologi (*tech stack*) yang ramah pengembangan seluler (seperti Flutter atau React Native).
2.  **Uji Coba Pengguna (Fokus Grup):** Membawa draf PRD dan kawat gambar (*wireframe*) awal ini kepada 5-10 guru lokal untuk menyaring umpan balik langsung sebelum pengodean dimulai.
3.  **Pengembangan Modular:** Memulai pembuatan prototipe dimulai dari Modul A (Asisten Produktivitas Mandiri) karena dampaknya terhadap pengurangan jam kerja langsung adalah yang paling instan dirasakan [4].
