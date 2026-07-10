import streamlit as st

def render_home():

    st.markdown("## 👋 Selamat Datang!")

    st.write(
        "Silakan pilih salah satu fitur di bawah atau langsung tulis pertanyaanmu."
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📚 Jelaskan Materi", use_container_width=True):
            return "Jelaskan materi tentang"

        if st.button("❓ Buat Quiz", use_container_width=True):
            return "Buatkan quiz mengenai"

        if st.button("🐍 Belajar Python", use_container_width=True):
            return "Ajarkan saya dasar-dasar Python"

    with col2:

        if st.button("📝 Ringkasan", use_container_width=True):
            return "Ringkas materi tentang"

        if st.button("📅 Study Planner", use_container_width=True):
            return "Buatkan jadwal belajar"

        if st.button("📊 Belajar Statistika", use_container_width=True):
            return "Ajarkan saya Statistika Dasar"

    return None