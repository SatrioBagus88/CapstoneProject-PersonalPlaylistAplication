#DIBUAT OLEH SATRIO BAGUS - JCDS2602
#CAPSTONE MODULE 1: PYTHON
#PURWADHIKA DIGITAL TECHNOLOGY SCHOOOL
#BSD


#PERHATIAN:
#PROGRAM INI MEMBUTUHKAN ANDA UNTUK MENG-INSTALL LIBRARY TABULATE
#TABULATE AKAN DIGUNAKAN DALAM BERBAGAI FUNGSI YANG BERKAITAN UNTUK MENJALANKAN PROGRAM INI
#DIPERLUKAN INSTALASI LIBRARY TABULATE PADA PYTHON


from tabulate import tabulate

# Data Awal
BankLagu = {
    "Mad Madmen":{
        "Ego Friendly": [("Mad Mad Woman", "4:45"), ("Cold Turkey", "3:35")],
        "Mental Breakdance": [("The Striker", "4:37"), ("Big 'ol Jazzmaster", "5:08")]},
    "Bernadya":{
        "Sialnya, Hidup Harus Tetap Berjalan": [("Sialnya, Hidup Harus Tetap Berjalan", "2:58"), ("Kata Mereka Ini Berlebihan", "3:02")]},
    "Efek Rumah Kaca":{
        "Efek Rumah Kaca": [("Cinta Melulu", "4:23"), ("Sebelah Mata", "4:29"), ("Desember", "4:16")],
        "Kamar Gelap": [("Menjadi Indonesia", "4:37"), ("Balerina", "4:02")]},
    "The Adams":{
        "Agterplaas": [("Agterplaas", "2:20"), ("Timur","4:59")]}
    }

UserPlaylist = [] #Disiapkan untuk pembuatan playlist
queue = [] #Disiapkan untuk pembuatan daftar antrian lagu
Admin = "admin123" #Password Admin untuk masuk ke menu Admin Only
now_playing = None #Untuk showing lagu mana yang sedang di putar
source_now_playing = None #untuk cek dari mana lagu di putar (Bank atau Playlist)

#Mempersiapkan clear terminal agar lebih rapi. Menggunakan if untuk bisa digunakan MacOS atau Windows
import platform
import os
def clear_terminal():
    osName = platform.system()
    if osName == 'Windows':
        os.system("cls") #ganti parameternya jadi "clear" jika MacOS atau Linux
    else:
        os.system("clear")

#Untuk tahu total jumlah lagu yang ada di bank
def hitung_total_lagu():
    total = 0
    for album in BankLagu.values():  # Loop setiap album dari artis
        for lagu_list in album.values():  # Loop daftar lagu dalam album
            total += len(lagu_list)  # Tambahkan jumlah lagu dalam album
    return total

#Menampilkan Bank Lagu
def ShowBank():
    global now_playing
    data_bank_lagu = []
    index = 0

    for artis, albums in BankLagu.items():
        for album, lagu_list in albums.items():
            for lagu, durasi in lagu_list:
                status = "Now Playing" if now_playing == (lagu, artis) else ""
                data_bank_lagu.append([index, artis, album, lagu, durasi, status])
                index += 1

    headers = ["Index", "Nama Artis", "Nama Album", "Judul Lagu", "Durasi", "Status"]
    print(tabulate(data_bank_lagu, headers=headers, tablefmt="grid"))

#Berguna untuk mencari duplikat nama, untuk tambah lagu
def cari_duplikat(nama, daftar_nama):
    for nama_tersedia in daftar_nama:
        if nama.lower() == nama_tersedia.lower():
            return nama_tersedia 
    return None

#Tambah lagu ke bank lagu
def tambah_lagu_ke_bank():
    print("PERINGATAN")
    print("Perhatikan format penulisan huruf besar dan huruf kecil")
    nama_artis = input("Masukkan nama artis: ").strip()
    artis_terdeteksi = cari_duplikat(nama_artis, BankLagu.keys())
    if artis_terdeteksi:
        pilihan = input(f"Apakah yang Anda maksud '{artis_terdeteksi}'? (y/n): ").strip().lower()
        if pilihan == 'y':
            nama_artis = artis_terdeteksi
        else:
            print("Menambahkan sebagai artis baru.")
    if nama_artis not in BankLagu:
        BankLagu[nama_artis] = {}
    nama_album = input("Masukkan nama album: ").strip()
    album_terdeteksi = cari_duplikat(nama_album, BankLagu[nama_artis].keys())
    if album_terdeteksi:
        pilihan = input(f"Apakah yang Anda maksud album '{album_terdeteksi}'? (y/n): ").strip().lower()
        if pilihan == 'y':
            nama_album = album_terdeteksi
        else:
            print("Menambahkan sebagai album baru.")
    if nama_album not in BankLagu[nama_artis]:
        BankLagu[nama_artis][nama_album] = []
    judul_lagu = input("Masukkan judul lagu: ").strip()
    for item in BankLagu[nama_artis][nama_album]:
        if item[0].lower() == judul_lagu.lower():
            print(f"Lagu '{judul_lagu}' sudah ada dalam album '{nama_album}'.")
            return 
    while True:
        durasi = input("Masukkan durasi lagu (mm:ss): ").strip()
        if ":" in durasi and len(durasi.split(":")) == 2 and all(i.isdigit() for i in durasi.split(":")):
            break
        else:
            print("Format durasi salah! Harap masukkan dalam format mm:ss.")
    BankLagu[nama_artis][nama_album].append((judul_lagu, durasi))

#Hapus lagu dari bank lagu
def hapus_lagu_dari_bank():
    ShowBank()
    if hitung_total_lagu() == 0:
        print("Bank Lagu kosong.")
        return
    while True:
        try:
            index_hapus = int(input("Masukkan index lagu yang ingin dihapus: "))
            index = 0
            for artis, albums in BankLagu.items():
                for album, lagu_list in albums.items():
                    for lagu, durasi in lagu_list:
                        if index == index_hapus:
                            BankLagu[artis][album].remove((lagu, durasi))
                            if not BankLagu[artis][album]:
                                del BankLagu[artis][album]
                            if not BankLagu[artis]:
                                del BankLagu[artis]
                            print(f"Lagu '{lagu}' telah dihapus.")
                            return
                        index += 1
            print("Index tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Harap masukkan angka yang valid.")

#show user playlist
def ShowPlaylist():
    global now_playing
    data_playlist = []

    for index, (lagu, artis, album, durasi) in enumerate(UserPlaylist):
        if now_playing == (lagu, artis):
            status = "Now Playing"
        else:
            status = ""
        data_playlist.append([index, lagu, artis, album, durasi, status]) #biar keliatan status

    headers = ["Index", "Judul Lagu", "Nama Artis", "Nama Album", "Durasi", "Status"]
    print(tabulate(data_playlist, headers=headers, tablefmt="grid"))

#tambah lagu ke playlist dari bank lagu
def tambah_lagu_ke_playlist():
    ShowBank()
    while True:
        try:
            AddSong = int(input("Masukkan index lagu yang ingin ditambahkan ke playlist: "))
            index = 0
            for artis, albums in BankLagu.items():
                for album, lagu_list in albums.items():
                    for lagu, durasi in lagu_list:
                        if AddSong == index:
                            UserPlaylist.append([lagu, artis, album, durasi])
                            print(f"Lagu '{lagu}' telah ditambahkan ke playlist Anda!")
                            ShowPlaylist()
                            return
                        index += 1
            print("Index tidak ditemukan. Coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")

#Membuat Queue
def generate_queue():
    global queue
    queue = []  # Reset queue
    lagu_saat_ini, artis_saat_ini = now_playing
    index = 0

    if source_now_playing == "Bank Lagu":
        found = False
        for artis, albums in BankLagu.items():
            for album, lagu_list in albums.items():
                for lagu, durasi in lagu_list:
                    if found:
                        queue.append((index, lagu, artis, album, durasi))
                        index += 1
                    if (lagu, artis) == now_playing:
                        found = True

    elif source_now_playing == "Playlist":
        found = False
        for song in UserPlaylist:
            lagu, artis, album, durasi = song
            if found:
                queue.append((index, lagu, artis, album, durasi))
                index += 1
            if (lagu, artis) == now_playing:
                found = True

#mengubah urutan lagu di playlist
def push():
    ShowPlaylist()
    try:
        index_lama = int(input("Masukkan nomor lagu yang ingin dipindahkan: "))
        posisi_baru = int(input("Masukkan posisi baru (0 = teratas): "))

        if 0 <= index_lama < len(UserPlaylist) and 0 <= posisi_baru < len(UserPlaylist):
            lagu = UserPlaylist.pop(index_lama)
            UserPlaylist.insert(posisi_baru, lagu)
            print("Urutan lagu berhasil diubah!")
            ShowPlaylist()
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Harap masukkan angka yang benar.")

#untuk play lagu langsung dari bank
def play_lagu_bank():
    global now_playing, source_now_playing, queue
    ShowBank()

    while True:
        try:
            index_pilih = int(input("Masukkan index lagu yang ingin dimainkan: "))
            index = 0
            for artis, albums in BankLagu.items():
                for album, lagu_list in albums.items():
                    for lagu, durasi in lagu_list:
                        if index == index_pilih:
                            now_playing = (lagu, artis)
                            source_now_playing = "Bank Lagu"
                            queue = []  # Reset queue saat lagu baru dipilih
                            print(f"Now Playing: '{lagu}' oleh {artis}, durasi {durasi}")
                            return  
                        index += 1
            
            print("Index tidak ditemukan! Silakan coba lagi.")

        except ValueError:
            print("Harap masukkan angka yang valid!")

#play lagu dari playlist
def play_lagu():
    global now_playing
    global source_now_playing
    source_now_playing = "Playlist"
    ShowPlaylist()
    try:
        index_play = int(input("Masukkan nomor lagu yang ingin dimainkan: "))

        if 0 <= index_play < len(UserPlaylist):
            now_playing = (UserPlaylist[index_play][0], UserPlaylist[index_play][1])
            # source_now_playing = "Playlist"
            print(f"Sekarang memutar: {now_playing[0]} - {now_playing[1]}")
            # source_now_playing = "Playlist"
            ShowPlaylist()
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Masukkan angka yang benar.")

#Show Queue
def show_queue():
    global queue

    if now_playing is None:
        print("Tidak ada lagu yang sedang diputar.")
        return

    if not queue:
        print("Queue kosong.")
        return

    print("Queue Lagu:")
    print(tabulate(queue, headers=["Index", "Judul Lagu", "Artis", "Album", "Durasi"], tablefmt="grid"))

#mengubah urutan lagu di queue
def push_queue():
    global queue

    if not queue:
        print("Queue kosong.")
        return

    print("Queue sebelum perubahan:")
    print(tabulate(queue, headers=["Index", "Judul Lagu", "Artis", "Album", "Durasi"], tablefmt="grid"))

    try:
        index_lama = int(input("Masukkan nomor lagu yang ingin dipindahkan (0-based index): "))
        posisi_baru = int(input("Masukkan posisi baru (0 = teratas): "))

        # Validasi indeks harus dalam rentang yang benar
        if 0 <= index_lama < len(queue) and 0 <= posisi_baru < len(queue):
            # Ambil lagu dari index lama
            lagu = queue.pop(index_lama)
            # Masukkan ke posisi baru
            queue.insert(posisi_baru, lagu)

            # Perbarui indeks secara manual
            queue = [(i, lagu[1], lagu[2], lagu[3], lagu[4]) for i, lagu in enumerate(queue)]

            print("\nQueue setelah perubahan:")
            print(tabulate(queue, headers=["Index", "Judul Lagu", "Artis", "Album", "Durasi"], tablefmt="grid"))
        else:
            print("Indeks tidak valid. Pastikan angka yang dimasukkan sesuai panjang queue.")
    except ValueError:
        print("Harap masukkan angka yang benar.")

#memainkan lagu berikutnya, berdasarkan queue
def next_song():
    global now_playing, queue
    if not now_playing:
        print("Tidak ada lagu yang sedang diputar.")
        return

    # Cek apakah ada lagu dalam queue
    if queue:
        next_track = queue.pop(0)
        now_playing = (next_track[1], next_track[2])  # (judul lagu, artis)
        print(f"Sekarang memutar: {now_playing[0]} - {now_playing[1]}")
        return
    
    # Jika queue kosong, cek UserPlaylist
    for i in range(len(UserPlaylist)):
        if (UserPlaylist[i][0], UserPlaylist[i][1]) == now_playing:
            if i + 1 < len(UserPlaylist):
                now_playing = (UserPlaylist[i+1][0], UserPlaylist[i+1][1])
                print(f" Sekarang memutar: {now_playing[0]} - {now_playing[1]}")
                ShowPlaylist()
                return

    # Jika tidak ada lagu lagi, reset `now_playing`
    now_playing = None
    print("Sudah mencapai akhir playlist atau queue kosong.")

#Menghentikan lagu yang sedang dimainkan
def stop_lagu():
    global now_playing, source_now_playing
    if now_playing:
        print(f"Lagu '{now_playing[0]}' oleh {now_playing[1]} telah dihentikan.")
        now_playing = None
        source_now_playing = None
    else:
        print("Tidak ada lagu yang sedang diputar.")

#hapus lagu dari playlist
def hapus_lagu_dari_playlist():
    global now_playing

    if not UserPlaylist:
        print("Playlist Anda kosong.")
        return
    ShowPlaylist()  # Menampilkan playlist saat ini
    try:
        index_hapus = int(input("Masukkan index lagu yang ingin dihapus: "))

        if 0 <= index_hapus < len(UserPlaylist):
            lagu, artis, album, durasi = UserPlaylist[index_hapus]
            UserPlaylist.pop(index_hapus)  # Menghapus lagu dari playlist

            # Jika lagu yang dihapus sedang diputar, reset now_playing
            if now_playing == (lagu, artis):
                now_playing = None
                print(f"Lagu '{lagu}' sedang diputar dan telah dihapus. Pemutaran dihentikan.")
            else:
                print(f"Lagu '{lagu}' telah dihapus dari playlist Anda.")

            ShowPlaylist()  # Menampilkan playlist setelah penghapusan
        else:
            print("Index tidak valid. Silakan coba lagi.")
    except ValueError:
        print("Harap masukkan angka yang valid.")

def main_menu():
    while True:
        clear_terminal()
        print("SOUND-CHECK")
        print("Your Personal Playlist Maker")
        print()
        print("MAIN MENU")
        print("1. Lihat Bank Lagu")
        print("2. Menu Play/Stop Lagu + Queue lagu")
        print("3. Menu Bank Lagu (Admin Only)")
        print("4. Menu Playlist")
        print("5. Exit Program")
        print()
        pilihan = input("Pilih menu (1-5): ")
        while pilihan == "1":
            clear_terminal()
            print("Bank Lagu")
            ShowBank()
            print("Menu")
            print("1. Buat Playlist")
            print("2. Kembali ke main menu")
            PilihanMenu1 = input("Pilih menu (1-2): ").strip()
            if PilihanMenu1 == "1":
                if len(UserPlaylist) >= 1:
                    ShowPlaylist()
                    while True:
                        tambah_lagu = input("Mau tambah lagu? (y/n): ").strip().lower()
                        if tambah_lagu == "y":
                            tambah_lagu_ke_playlist()
                        if tambah_lagu == "n":
                            break
                        else:
                            print("Masukkan 'y' atau 'n'!")
                else:
                    clear_terminal()
                    print("Belum ada playlist.")
                    while True:
                        playlistbaru = input("Apakah mau membuat playlist baru? (y/n): ").strip().lower()
                        if playlistbaru == "y":
                            tambah_lagu_ke_playlist()
                        if playlistbaru == "n":
                            break
                        else:
                            print("Masukkan 'y' atau 'n'!") 
            if PilihanMenu1 == "2":
                main_menu()
            else:
                print("Masukkan angka 1 atau 2!")
        while pilihan == "2":
            clear_terminal()
            print("Menu Play Lagu")
            print("1. Putar lagu dari Bank Lagu")
            print("2. Putar lagu dari playlist")
            print("3. Lihat daftar antrian lagu")
            print("4. Edit daftar antrian lagu")
            print("5. Stop lagu yang sedang diputar")
            print("6. Kembali ke main menu")
            PilihanMenu2 = input("Pilih menu (1-6): ").strip()
            if PilihanMenu2 == "1":
                clear_terminal()
                print("Pilih lagu dari bank lagu")
                play_lagu_bank()
                generate_queue()
                show_queue()
                enter = input("Tekan Enter untuk kembali")
            if PilihanMenu2 == "2":
                clear_terminal()
                if len(UserPlaylist) == 0:
                    print("Belum ada playlist.")
                    while True:
                        playlistbaru = input("Apakah mau membuat playlist baru? (y/n): ").strip().lower()
                        if playlistbaru == "y":
                            tambah_lagu_ke_playlist()
                        elif playlistbaru == "n":
                            break 
                if len(UserPlaylist) >= 1:
                    print ("Pilih lagu dari playlist")
                    play_lagu()
                    generate_queue()
                    enter = input("Tekan Enter untuk kembali")
            if PilihanMenu2 == "3":
                clear_terminal()
                if len(queue)==0:
                    print("Queue kosong.")
                    enter = input("Tekan Enter untuk kembali")
                else:
                    clear_terminal()
                    show_queue()
                    print("Menu Queue Lagu")
                    print("1. Play Next Song")
                    print("2. Kembali ke menu sebelumnya")
                    MenuQueue = input("Pilih menu (1-2): ").strip()
                    if MenuQueue == "1":
                        clear_terminal()
                        next_song()
                        show_queue()
                        enter = input("Tekan Enter untuk kembali")
                    if MenuQueue == "2":
                        clear_terminal()
                        continue
            if PilihanMenu2 == "4":
                clear_terminal()
                if len(queue)==0:
                    print("Queue kosong.")
                    enter = input("Tekan Enter untuk kembali")
                if len(queue) >0:
                    push_queue()
                    enter = input("Tekan Enter untuk kembali")
            if PilihanMenu2 == "5":
                clear_terminal()
                stop_lagu()
                enter = input("Tekan Enter untuk kembali")
            if PilihanMenu2 == "6":
                main_menu()
        while pilihan == "3":
            print("Hanya admin yang bisa Mengakses menu Bank Lagu")
            InputPasswordAdmin = input("Masukan Password Admin: ")
            while InputPasswordAdmin == Admin:
                while True:
                    clear_terminal()
                    print("Bank Data Lagu")
                    ShowBank()
                    print()
                    print("Menu Bank Lagu")
                    print("1. Tambahkan Lagu ke Bank Lagu")
                    print("2. Hapus Lagu dari Bank Lagu")
                    print("3. Kembali ke Menu Utama")
                    PilihanMenu3 = int(input("pilih menu (masukan dalam angka): "))
                    if PilihanMenu3 == 1:
                        while True:
                            tambah_lagu_ke_bank()
                            print("Ini adalah daftar lagu terupdate:")
                            ShowBank()
                            lanjut = input("Ingin menambahkan lagu lain? (y/n): ").strip().lower()
                            while lanjut not in ["y", "n"]:
                                print("Input salah")
                                lanjut = input("Masukkan input ulang (y/n): ").strip().lower()
                            if lanjut == "n":
                                break  # Kembali ke menu "Bank Data Lagu"
                    if PilihanMenu3 == 2:
                        clear_terminal()
                        hapus_lagu_dari_bank()
                        print("Ini adalah bank Lagu Terupdate")
                        ShowBank()
                        lanjut = input("Ingin menghapus lagu lain? (y/n): ").strip().lower()
                        if lanjut != "y" and lanjut !="n":
                            print ("Input salah")
                            lanjut = input("Masukan input ulang (y/n): ").strip().lower()
                        if lanjut == "n":
                            print ("Ini adalah Bank Lagu yang terbaru:")
                            print()
                            ShowBank()
                            print("======================================")
                    if PilihanMenu3 == 3:
                        main_menu()
                    break
                continue
            if InputPasswordAdmin != Admin:
                print("password salah, masukan kembali password")
                continue
            break
        while pilihan == "4":
            clear_terminal()
            print("Menu Playlist")
            print("1. Lihat Playlist")
            print("2. Tambahkan Lagu ke Playlist")
            print("3. Edit Urutan Lagu dalam Playlist")
            print("4. Hapus lagu dari daftar playlist")
            print("5. Kembali ke Menu Utama")
            PilihanMenu4 = (input("Pilih menu (1-5): "))
            while PilihanMenu4 == "1":
                if len(UserPlaylist) == 0:
                    clear_terminal()
                    print("Belum ada playlist.")
                    while True:
                        playlistbaru = input("Apakah mau membuat playlist baru? (y/n): ").strip().lower()
                        if playlistbaru == "y":
                            tambah_lagu_ke_playlist()
                        if playlistbaru == "n":
                            break
                        else:
                            print("Masukkan 'y' atau 'n'!")
                    if len(UserPlaylist) >= 1:
                        print ("Ini adalah playlist yang anda buat:")
                        ShowPlaylist()
                        enter = input("Tekan Enter untuk kembali")
                    break
                if len(UserPlaylist) >= 1:
                    clear_terminal()
                    ShowPlaylist()
                    enter = input("Tekan Enter untuk kembali")
                    break
            while PilihanMenu4 == "2":
                if len(UserPlaylist) == 0:
                    clear_terminal()
                    print("Belum ada playlist.")
                    while True:
                        playlistbaru = input("Apakah mau membuat playlist baru? (y/n): ").strip().lower()
                        if playlistbaru == "y":
                            tambah_lagu_ke_playlist()
                        if playlistbaru == "n":
                            break
                        else:
                            print("Masukkan 'y' atau 'n'!")
                    break
                if len(UserPlaylist) > 0:
                    clear_terminal()
                    ShowPlaylist()
                    while True:
                        tambah_lagu = input("Mau tambah lagu? (y/n): ").strip().lower()
                        if tambah_lagu == "y":
                            tambah_lagu_ke_playlist()
                        if tambah_lagu == "n":
                            break
                        else:
                            print("Masukkan 'y' atau 'n'!")
                        break
                    break
            while PilihanMenu4 == "3":
                if len(UserPlaylist) == 0:
                    print("Anda belum punya playlist")
                    BikinPlaylist = input("Apakah anda ingin buat playlist baru?(y/n): ").strip().lower()
                    while BikinPlaylist == "y":
                        tambah_lagu_ke_playlist()
                        BikinPlaylist = input("Ingin menambahkan lagu lain? (y/n): ").strip().lower()
                    if BikinPlaylist == "n":
                        print ("Anda akan kembali ke bagian Menu Playlist")
                    if len(UserPlaylist) >= 1:
                        print ("Ini adalah playlist yang anda buat:")
                        break
                    break
                if len(UserPlaylist) > 0:
                    print ("Ini adalah playlist yang anda buat:")
                    ShowPlaylist()
                    lanjut = input("Ingin mengubah urutan playlist? (y/n): ").strip().lower()
                    while lanjut == "y":
                        push()
                        lanjut = input("Ingin mengubah urutan playlist lagi? (y/n): ").strip().lower()
                    if lanjut == "n":
                        ShowPlaylist()
                        break
                    if lanjut != "y" and lanjut !="n":
                        print ("Input salah")
                        lanjut = input("Masukan input ulang (y/n): ").strip().lower()
                    break
                break
            while PilihanMenu4 == "4":
                if len(UserPlaylist) == 0:
                    print("Anda belum punya playlist")
                    BikinPlaylist = input("Apakah anda ingin buat playlist baru?(y/n): ").strip().lower()
                    while BikinPlaylist == "y":
                        tambah_lagu_ke_playlist()
                        BikinPlaylist = input("Ingin menambahkan lagu lain? (y/n): ").strip().lower()
                    if BikinPlaylist == "n":
                        print ("Anda akan kembali ke bagian Menu Playlist")
                    if len(UserPlaylist) >= 1:
                        print ("Ini adalah playlist yang anda buat:")
                        break
                    break
                while len(UserPlaylist) > 0:
                    print("Menu Hapus Playlist")
                    print("1. Hapus lagu dari playlist")
                    print("2. Hapus semua lagu dari playlist")
                    print("3. Kembali ke menu playlist")
                    hapuslagu = input("Pilih menu (1-3): ").strip()
                    while hapuslagu=="1":
                        hapus_lagu_dari_playlist()
                        hapuslagu1 = input("Ingin menghapus lagu yang lain? (y/n): ").strip().lower()
                        if hapuslagu1== "y":
                            hapus_lagu_dari_playlist()
                            hapuslagu1 = input("Ingin menghapus lagu yang lain? (y/n): ").strip().lower()
                        if hapuslagu1== "n":
                            break
                        break
                    while hapuslagu=="2":
                        konfirmasi = input("Yakin ingin menghapus seluruh playlist? (y/n)")
                        if konfirmasi == "y":
                            clear_terminal()
                            UserPlaylist.clear() #Menghapus semua lagu dalam playlist
                            print("Playlist anda sudah berhasil dihapus")
                            enter = input("Tekan Enter untuk kembali")
                            break
                        if konfirmasi == "n":
                            break
                    while hapuslagu=="3":
                        break
                    break
                break
            while PilihanMenu4 == "5":
                main_menu()
        while pilihan == "5":
            clear_terminal()
            print("Terima kasih sudah menggunakan aplikasi SOUND-CHECK")
            exit()
  
main_menu()

#Program ini dibuat untuk memenuhi syarat kelulusan di institusi Purwadhika School
#Satrio Bagus Prabowo - JCDS2602