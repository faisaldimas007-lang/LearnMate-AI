import streamlit as st


def render_home():
    st.markdown("👋 Apa yang ingin kamu pelajari hari ini?")

    st.caption(
        "Pilih salah satu menu cepat atau tuliskan pertanyaanmu langsung."
    )

    col1, col2, col3 = st.columns(3)

    quick_prompt = None

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-title">📖 Penjelasan Materi</div>
                <div class="feature-description">
                    Pelajari konsep dengan penjelasan bertahap dan contoh sederhana.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Mulai belajar",
            key="explain_action",
            use_container_width=True,
        ):
            quick_prompt = "Jelaskan materi tentang "

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-title">💻 Belajar Python</div>
                <div class="feature-description">
                    Pelajari coding dari dasar disertai contoh dan latihan.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Belajar Python",
            key="python_action",
            use_container_width=True,
        ):
            quick_prompt = "Ajarkan saya dasar-dasar Python."

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-title">📝 Ringkasan Materi</div>
                <div class="feature-description">
                    Ubah materi panjang menjadi rangkuman yang ringkas dan terstruktur.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Buat ringkasan",
            key="summary_action",
            use_container_width=True,
        ):
            quick_prompt = "Ringkas materi tentang "

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-title">📊 Statistika</div>
                <div class="feature-description">
                    Pelajari statistika dan data science dengan bahasa yang mudah.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Belajar statistika",
            key="statistics_action",
            use_container_width=True,
        ):
            quick_prompt = "Jelaskan konsep dasar statistika."

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-title">❓ Quiz Generator</div>
                <div class="feature-description">
                    Buat latihan soal beserta jawaban dan pembahasannya.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Buat quiz",
            key="quiz_action",
            use_container_width=True,
        ):
            quick_prompt = "Buatkan quiz tentang "

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-title">📅 Study Planner</div>
                <div class="feature-description">
                    Susun jadwal belajar berdasarkan target dan waktu yang tersedia.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Buat study planner",
            key="planner_action",
            use_container_width=True,
        ):
            quick_prompt = "Buatkan rencana belajar untuk "

    return quick_prompt