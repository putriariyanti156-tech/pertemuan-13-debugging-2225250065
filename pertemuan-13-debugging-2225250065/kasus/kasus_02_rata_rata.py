def hitung_rata_rata(daftar_nilai):
    """Menghitung nilai rata-rata dari list nilai."""
    if not daftar_nilai:
        return 0
    return sum(daftar_nilai) / len(daftar_nilai)


if __name__ == "__main__":
    print("--- Program Hitung Rata-Rata Nilai ---")
    input_str = input(
        "Masukkan daftar nilai dipisahkan dengan koma (contoh: 80,75,90): "
    )
    try:
        # Mengubah string input menjadi list of float
        nilai_list = [float(item.strip()) for item in input_str.split(",")]
        rata_rata = hitung_rata_rata(nilai_list)
        print(f"Daftar Nilai: {nilai_list}")
        print(f"Nilai Rata-rata: {rata_rata:.2f}")
    except ValueError:
        print("Pastikan semua masukan berupa angka dan dipisahkan dengan koma.")