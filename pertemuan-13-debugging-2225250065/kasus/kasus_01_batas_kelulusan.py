def cek_kelulusan(nilai, batas_minimum=60):
    """Menentukan status kelulusan berdasarkan batas minimum nilai."""
    if nilai >= batas_minimum:
        return "Lulus"
    else:
        return "Tidak Lulus"


if __name__ == "__main__":
    print("--- Program Cek Batas Kelulusan ---")
    try:
        input_nilai = float(input("Masukkan nilai siswa: "))
        status = cek_kelulusan(input_nilai)
        print(f"Status: {status}")
    except ValueError:
        print("Mohon masukkan angka yang valid.")