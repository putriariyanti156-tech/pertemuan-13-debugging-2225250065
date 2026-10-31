def status_lulus(nilai):
    # Memperbaiki operator dari '>' menjadi '>='
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


# Menjalankan kembali seluruh test case
if __name__ == "__main__":
    test_cases = [59, 60, 61]

    print("--- Hasil Pengujian (Test Cases) ---")
    for t in test_cases:
        hasil = status_lulus(t)
        print(f"Nilai: {t} -> Status: {hasil}")