# 🎓 LearnMate AI

LearnMate AI adalah aplikasi asisten belajar berbasis Gemini AI yang membantu pengguna memahami materi, membuat ringkasan, menghasilkan quiz, menyusun rencana belajar, dan belajar dari dokumen PDF.

## 🌐 Live Demo

Aplikasi dapat diakses melalui:

https://learnmate-ai-education.streamlit.app/

## ✨ Fitur

- 💬 Chatbot pendidikan berbasis Gemini AI
- 📖 Penjelasan materi
- 📝 Ringkasan materi
- ❓ Quiz Generator
- 📅 Study Planner
- 💻 Mode belajar coding
- 📊 Data Science Assistant
- 📄 Membaca dan memahami materi dari PDF
- 🎓 Penyesuaian tingkat pendidikan
- 🗣️ Pilihan gaya bahasa
- 📏 Pilihan tingkat detail jawaban
- 💾 Riwayat percakapan selama sesi
- 📈 Dashboard aktivitas pengguna

## 🛠️ Teknologi

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- PyPDF
- Python Dotenv
- Git dan GitHub

## 📁 Struktur Proyek

```text
LearnMate-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── components/
│   ├── chat.py
│   ├── home.py
│   ├── sidebar.py
│   └── __init__.py
│
├── prompts/
│   ├── system_prompt.py
│   └── __init__.py
│
├── services/
│   ├── gemini_service.py
│   └── __init__.py
│
└── utils/
    ├── pdf_reader.py
    └── __init__.py
```

## 🚀 Menjalankan Proyek Secara Lokal

### 1. Clone repository

```bash
git clone https://github.com/faisaldimas007-lang/LearnMate-AI.git
```

### 2. Masuk ke folder proyek

```bash
cd LearnMate-AI
```

### 3. Buat atau aktifkan environment

Contoh menggunakan Conda:

```bash
conda create -n learnmate python=3.12
conda activate learnmate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Buat file `.env`

```env
GEMINI_API_KEY=API_KEY_GEMINI_KAMU
```

### 6. Jalankan aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka di:

```text
http://localhost:8501
```

## 🔐 Keamanan

API key disimpan dalam file `.env` dan tidak diunggah ke GitHub.

Untuk deployment Streamlit Community Cloud, API key disimpan melalui fitur Secrets:

```toml
GEMINI_API_KEY = "API_KEY_GEMINI_KAMU"
```

## 📸 Screenshot

Tambahkan screenshot aplikasi ke folder:

```text
screenshots/
```

Kemudian tampilkan di README:

```markdown
![Tampilan LearnMate AI](screenshots/home.png)
```

## 🗺️ Pengembangan Selanjutnya

- Analisis dataset CSV
- Visualisasi data
- Quiz interaktif
- Penyimpanan riwayat belajar
- Sistem skor dan progres belajar
- RAG untuk dokumen PDF berukuran besar

## 👨‍💻 Author

**Dimas Faisal Zulmi**

GitHub: [faisaldimas007-lang](https://github.com/faisaldimas007-lang)

## 📄 License

Proyek ini menggunakan MIT License.