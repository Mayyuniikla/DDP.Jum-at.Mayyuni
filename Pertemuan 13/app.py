import streamlit as st

#Sidebar Directory
dashboard = st.Page("dashboard.py", title="Dashboard")
nabung = st.Page("nabung.py", title="Nabung")

pg = st.navigation(
    {
        "Menu Utama": [dashboard],
        "Transaksi": [nabung]
    }
)


if'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()