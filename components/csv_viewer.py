import streamlit as st


def render_csv_viewer(dataframe):
    if dataframe is None:
        return

    st.subheader("📊 Preview Dataset")
    st.dataframe(dataframe.head(), use_container_width=True)

    st.subheader("📈 Statistik Deskriptif")
    st.dataframe(
        dataframe.describe(include="all"),
        use_container_width=True,
    )