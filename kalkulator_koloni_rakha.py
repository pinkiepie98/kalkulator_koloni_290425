import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Total Plate Count Calculator", layout="centered")

# Judul
st.title("Total Plate Count (TPC) Calculator")

st.markdown("""
### Rumus TPC (CFU/mL)  
*TPC = (Jumlah Koloni × Faktor Pengenceran) / Volume yang Ditabur*
""")

# Input data
with st.form("form_tpc"):
    koloni = st.number_input("Jumlah Koloni (CFU)", min_value=0, value=0)
    pengenceran = st.number_input("Faktor Pengenceran (misal: 10000 untuk 10⁴)", min_value=1, value=10000)
    volume = st.number_input("Volume yang Ditabur (mL)", min_value=0.01, value=1.00, format="%.2f")
    submit = st.form_submit_button("Hitung TPC")

# Perhitungan TPC
if submit:
    try:
        tpc = (koloni * pengenceran) / volume
        st.success(f"*Hasil TPC: {tpc:.2e} CFU/mL*")
    except ZeroDivisionError:
        st.error("Volume tidak boleh nol!")

# Upload gambar mikroskop
st.markdown("### Upload Gambar Mikroskop (Opsional)")
uploaded_file = st.file_uploader("Pilih gambar (.jpg, .jpeg, .png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar Mikroskop", use_column_width=True)
    st.info("Analisis otomatis gambar belum tersedia. Fitur ini bisa dikembangkan ke depannya.")