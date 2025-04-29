import time
import os
from tabulate import tabulate

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for chemical-themed loading animation
def chemical_loading_animation():
    bubbles = [
        "         ( )",
        "        (   )",
        "       (     )",
        "        (   )",
        "         ( )",
        "          .",
        "         . .",
        "        . . .",
        "       . . . .",
        "      . . . . .",
        "[ CHEMICAL REACTION INITIATED ]"
    ]

    for _ in range(2):  # Repeat the animation
        for frame in bubbles:
            clear_screen()
            print("\n" * 5)
            print(frame.center(80))
            time.sleep(0.2)

# Function to calculate Total Plate Count
def calculate_tpc(colony_counts, dilution_factors, volume_plated):
    total_cfu = 0
    for count, dilution in zip(colony_counts, dilution_factors):
        total_cfu += count / dilution

    average_cfu = total_cfu / len(colony_counts)
    tpc = average_cfu / volume_plated
    return tpc

# Main program
def main():
    clear_screen()
    print("="*80)
    print("WELCOME TO THE TOTAL PLATE COUNT (TPC) CALCULATOR".center(80))
    print("="*80)
    print("\nPreparing virtual lab environment...\n")
    time.sleep(1)

    # Run the animation
    chemical_loading_animation()

    print("\nSystem Ready! Let's start your experiment...")
    time.sleep(1.5)
    clear_screen()

    # Begin TPC Calculator
    print("="*50)
    print("        TOTAL PLATE COUNT (TPC) CALCULATOR")
    print("="*50)

    # Input number of plates
    while True:
        try:
            num_plates = int(input("\nEnter the number of plates counted: "))
            if num_plates <= 0:
                print("Number of plates must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    colony_counts = []
    dilution_factors = []

    # Input data for each plate
    for i in range(num_plates):
        print(f"\n--- Plate {i+1} ---")
        while True:
            try:
                count = int(input("Enter colony count: "))
                if count < 0:
                    print("Colony count cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                dilution = float(input("Enter dilution factor (e.g., for 10^-3 enter 0.001): "))
                if dilution <= 0 or dilution >= 1:
                    print("Dilution factor must be between 0 and 1.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a decimal number.")

        colony_counts.append(count)
        dilution_factors.append(dilution)

    # Input volume plated
    while True:
        try:
            volume_plated = float(input("\nEnter the volume plated (in mL, e.g., 0.1): "))
            if volume_plated <= 0:
                print("Volume must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a decimal number.")

    # Display entered data as a table
    table = []
    for i in range(num_plates):
        table.append([f"Plate {i+1}", colony_counts[i], dilution_factors[i]])

    print("\nData Summary:")
    print(tabulate(table, headers=["Plate", "Colony Count", "Dilution Factor"], tablefmt="fancy_grid"))

    # Calculate and display TPC
    tpc_result = calculate_tpc(colony_counts, dilution_factors, volume_plated)

    print("\n" + "="*50)
    print(f"Estimated Total Plate Count (TPC): {tpc_result:.2e} CFU/mL")
    print("="*50)

if _name_ == "_main_":
    main()



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
