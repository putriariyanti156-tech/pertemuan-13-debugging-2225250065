import os


def proses_file_nilai(nama_file):
    """Membaca data nilai dari file teks dan menghitung rata-rata serta statusnya."""
    if not os.path.exists(nama_file):
        print(
            f"File '{nama_file}' tidak ditemukan. Membuat file contoh otomatis..."
        )
        # Membuat file contoh jika belum ada
        with open(nama_file, "w", encoding="utf-8") as f:
            f.write("Andi: 75\nBudi: 50\nCici: 85\nDedi: 60\n")

    print(f"\n--- Membaca Data dari {nama_file} ---")
    total = 0
    jumlah_data = 0

    with open(nama_file, "r", encoding="utf-8") as f:
        for baris in f:
            baris = baris.strip()
            if baris and ":" in baris:
                nama, nilai_str = baris.split(":")
                nilai = float(nilai_str.strip())
                status = "Lulus" if nilai >= 60 else "Tidak Lulus"
                print(
                    f"Siswa: {nama.strip()} | Nilai: {nilai} | Status: {status}"
                )
                total += nilai
                jumlah_data += 1

    if jumlah_data > 0:
        rata_rata = total / jumlah_data
        print(f"\nRata-rata kelas: {rata_rata:.2f}")


if __name__ == "__main__":
    file_target = "data_nilai.txt"
    proses_file_nilai(file_target)