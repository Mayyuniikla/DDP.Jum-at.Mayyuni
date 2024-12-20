import streamlit as st

st.title("Halaman Menabung")

with st.form("Menabung"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("Waktu")
    button = st.form_submit_button(label="Menabung")
    
    if button and jumlah >= 50000:
        st.session_state['total_semua'].append({
            "Tipe" : "Menabung",
            "Jumlah" : jumlah
        })
        st.success("Anda Berhasil Menabung")
    else:
        st.error("kamu Gagal Menabung, Nominal Kurang daro 50000")