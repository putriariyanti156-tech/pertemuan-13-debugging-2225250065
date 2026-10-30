def rata_rata(data):
    # Penanganan list kosong agar tidak terjadi error pembagian dengan nol
    if not data:
        return 0  # Bisa mengembalikan 0 atau None sesuai kebutuhan

    total = sum(data)
    # Pembagi disesuaikan secara dinamis dengan jumlah data menggunakan len(data)
    return total / len(data)


# Menjalankan test case dengan berbagai panjang list
if __name__ == "__main__":
    test_cases = [
        [80, 90, 70],  # Panjang 3
        [80, 90, 70, 60, 100],  # Panjang 5
        [75, 85],  # Panjang 2
        [],  # List kosong
    ]

    print("--- Hasil Pengujian Fungsi Rata-Rata ---")
    for i, tc in enumerate(test_cases, 1):
        hasil = rata_rata(tc)
        print(f"Test Case {i} (Data: {tc}) -> Rata-rata: {hasil}")