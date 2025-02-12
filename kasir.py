# Program Kasir Sederhana dengan Struk Pembelian

def tampilkan_menu():
    print("\nMenu Kasir:")
    print("1. Tambah Barang")
    print("2. Tampilkan Daftar Belanja")
    print("3. Hitung Total Belanja")
    print("4. Cetak Struk Pembelian")
    print("5. Keluar")

def tambah_barang(daftar_barang):
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = float(input("Masukkan harga barang (Rp): "))
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    total_harga = harga_barang * jumlah_barang
    daftar_barang.append({"nama": nama_barang, "harga": harga_barang, "jumlah": jumlah_barang, "total": total_harga})

def tampilkan_daftar_belanja(daftar_barang):
    if not daftar_barang:
        print("Daftar belanja kosong!")
    else:
        print("\nDaftar Belanja:")
        for idx, barang in enumerate(daftar_barang, 1):
            print(f"{idx}. {barang['nama']} - {barang['jumlah']} x Rp{barang['harga']:.2f} = Rp{barang['total']:.2f}")
        print()

def hitung_total(daftar_barang):
    total = sum(barang['total'] for barang in daftar_barang)
    print(f"Total Belanja: Rp{total:.2f}")
    return total

def cetak_struk(daftar_barang, total):
    print("\n========== STRUK PEMBELIAN ==========")
    print("Toko Kasir Sederhana")
    print("-------------------------------------")
    for barang in daftar_barang:
        print(f"{barang['nama']} ({barang['jumlah']} x Rp{barang['harga']:.2f}) = Rp{barang['total']:.2f}")
    print("-------------------------------------")
    print(f"Total Belanja: Rp{total:.2f}")
    print("Terima kasih telah berbelanja!")
    print("=====================================")

def main():
    daftar_barang = []
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_barang(daftar_barang)
        elif pilihan == "2":
            tampilkan_daftar_belanja(daftar_barang)
        elif pilihan == "3":
            hitung_total(daftar_barang)
        elif pilihan == "4":
            total = hitung_total(daftar_barang)
            cetak_struk(daftar_barang, total)
            break  # Keluar setelah mencetak struk
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program kasir!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
