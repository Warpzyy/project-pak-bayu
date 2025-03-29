import queue

# Fungsi untuk menambahkan pelanggan ke dalam antrian
def tambah_pelanggan(antrian, nama):
    antrian.put(nama)
    print(f"{nama} telah ditambahkan ke antrian.")

# Fungsi untuk memanggil pelanggan sesuai urutan FIFO
def panggil_pelanggan(antrian):
    if antrian.empty():
        print("Tidak ada pelanggan dalam antrian.")
    else:
        print(f"Memanggil {antrian.get()}.")

# Fungsi untuk melihat daftar pelanggan dalam antrian
def lihat_antrian(antrian):
    if antrian.empty():
        print("Antrian kosong.")
    else:
        print("Daftar antrian saat ini:")
        list_antrian = list(antrian.queue)
        for i, nama in enumerate(list_antrian, start=1):
            print(f"{i}. {nama}")

# Fungsi utama untuk menjalankan program
def main():
    antrian = queue.Queue()  # Membuat objek antrian
    while True:
        # Menampilkan menu utama
        print("\nMenu:")
        print("1. Tambah pelanggan")
        print("2. Panggil pelanggan")
        print("3. Lihat antrian")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        
        # Eksekusi berdasarkan pilihan pengguna
        if pilihan == "1":
            nama = input("Masukkan nama pelanggan: ")
            tambah_pelanggan(antrian, nama)
        elif pilihan == "2":
            panggil_pelanggan(antrian)
        elif pilihan == "3":
            lihat_antrian(antrian)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan layanan bank.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program jika dijalankan sebagai skrip utama
if __name__ == "__main__":
    main()
