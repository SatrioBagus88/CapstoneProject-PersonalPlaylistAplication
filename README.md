
##### *Disclaimer*:
1. *This program was created to fulfill an assignment in the Python learning module at Purwadhika Digital Technology School.*
2. *This program is written in the Python programming language and is created in Indonesian Language. The available ReadMe file is also written in Indonesian*
3. *The naming of the program 'Sound-Check' is merely a designation and is not intended to infringe on any copyright or intellectual property rights of anyone. This program is also created not for commercial purposes.*
4. *The data used is dummy data, referencing real-world artists without utilizing any master files or derivative materials from the respective artists. All rights associated with the names of the artists, album titles, song titles, and other related elements belong to the relevant parties and are fully attributed to them.*


# SOUND-CHECK

Sebuah program sederhana yang berfokus untuk pengelolaan data pemutaran musik. Ditujukan layaknya *digital streaming platform* dengan fungsi yang lebih sederhana. Terdapat fitur pengelolaan Bank Lagu, Playlist, Daftar Antrian Lagu, dan Play/Stop lagu agar pengguna bisa membuat daftar musik yang disuka secara personal.

### Struktur Data
Struktur data adalah hal-hal yang berkaitan dengan data-dataa yang ditampilkan dan digunakan di dalam program. Data di program ini menggunakan data-data *dummy* yang tidak nyata dengan struktu sebagai berikut.

1. **Index** (Int): Sebuah penomoran unik, digunakan untuk pemanggilan baris yang ingin digunakan dalam sistem
2. **Nama Artis** (String): Pengelompokan nama-nama artis yang lagunya dimasukan dalam data ini.
3. Nama Album (String): Pengelompokan nama album dari artis sehingga tampilan bisa lebih rapi
4. **Judul Lagu** (String): Penamaan judul lagu sehingga setiap lagu memiliki nama yang spesifik untuk ditampilkan
5. **Durasi** (String): Merujuk pada jumlah waktu tiap lagunya
6. **Status** (String): berfungsi untuk menampilkan lagu-lagu jika ada yang sedang diputar.


### Penjelasan Program
Program ini utamanya bertujuan untuk mengorganisir data-data lagu yang dipunya oleh pengguna. Pada fase pertama ini, program dijalankan masih belum bisa memutar lagu secara *real*. Hanya saja sudah disiapkan fitur `now_playing` yang memungkinkan pengguna untuk *tracking* lagu yang sedang dimainkan. Program ini juga mempunyai beberapa fitur, antara lain:
1. `BankLagu`: sebuah fitur untuk menyimpan seluruh data lagu yang dimiliki. Data lagu ini nantinya bertujuan sebagai data-data yang akan digunakan dalam program, dimulai dari pembuatan playlist, memutar lagu, juga sebagai referensi daftar antrian lagu saat lagu sedang diputar. User juga bisa menambahkan atau menghapus lagu-lagu dalam `BankLagu` ini melalui perubahan *role* sebagai Admin dengan memasukan password `admin` yaitu `admin123`.
2. `now_playing`: sebuah fitur yang akan diperlihatkan dibawah kolom `status` dalam tabel `BankLagu` ataupun `Playlist` agar menjadi informasi bagi pengguna tentang lagu mana yang sedang diputar.
3. `UserPlaylist`: sebagai fitur utama pada program ini dimana pengguna bisa membuat playlist berisikan lagu-lagu pilihan yang dipilih dari `BankLagu`. Pada fitur ini, pengguna juga bisa menambahkan, mengurangi, atau bahkan menghapus keseluruhan playlist yang sudah dibuat. Selain itu, melalui pemanggilan fungsi `push()` pada program, pengguna dapat mengubah posisi urutan lagu pada `UserPlaylist`.
4. `queue`: fitur ini memungkinkan pengguna melihat lagu-lagu selanjutnya dari apa yang sedang dimainkan. `queue` akan di-*generate* setiap kali pengguna memainkan lagu, baik itu dari `BankLagu` ataupun dari `UserPlaylist`. Jadi setiap urutan lagu akan selalu berbeda berdasarkan darimana pengguna memainkan lagu yang dipilih. Pengguna juga bisa mengatur urutan posisi `queue` dengan fungsi `push_queue`. `queue` juga akan menjadi acuan jika user memilih menu `next_song`.

### Aplikasi CRUD Dalam Program
CRUD adalah sebuah konsep dalam pengembangan aplikasi berbasis data. Singkatan dari *Create*, *Read*, *Update*, *Delete*
1. Create: dalam program ini pengguna dapat membuat sebuah playlst. Ini merupakan implementasi dari fitur *Create*. Penambahan data lagu-lagu dalam `BankLagu` ataupun `UserPlaylist` juga bisa dikatakan sebagai fungsi *Create*.
2. *Read*: `ShowBank`, `ShowPlaylist`, dan `show_queue` adalah fungsi untuk menampilkan data-data Bank Lagu, Playlist ataupun daftar antrian lagu.
3. *Update*: setiap pengguna memutar lagu, `now_playing` akan terlihat pada bagian kolom `status` di tiap lagu yang dimainkan pada tabel `BankLagu` ataupun `UserPlaylist`. Pengubahan urutan posisi lagu  di `queue` ataupun `UserPlaylist` juga merupakan bentuk implementasi fungsi *update*. Termasuk menampilkan pengubahan-pengubahan yang terjadi pada sistem.
4. *Delete*: Menghapus lagu menggunakan `hapus_lagu_dari_bank` (untuk hapus lagu dari `BankLagu`) atau `hapus_lagu_dari_playlist`(untuk hapus lagu dari `UserPlaylist` yang telah dibuat) adalah bentuk pemakaian fitur *Delete*


### Penggunaan Library
Program ini menggunakan beberapa *library* dari python.
1. Tabulate: library Python yang digunakan untuk memformat dan menampilkan data dalam bentuk tabel sehingga mudah dibaca.
2. OS: modul bawaan yang menyediakan fungsi-fungsi untuk berinteraksi dengan sistem operasi (OS). 
3. Platform: (modul platform) dalam Python adalah modul bawaan yang menyediakan fungsi-fungsi untuk mengakses informasi detail tentang sistem operasi, perangkat keras, dan lingkungan runtime Python. Library ini berguna untuk mendapatkan informasi spesifik tentang platform tempat kode Python dijalankan.


### Kekurangan dan Ruang Perbaikan Pada Program
Program ini masih jauh dari kata sempurna. Masih ada beberapa celah kekurangan yang bisa diperbaiki untuk versi lanjutannya. Beberapa kekurangannya adalah:
1. Program menggunakan data *dummy* sehingga keabsahannya harus diteliti lebih lanjut.
2. Ini merupakan program demo pembuatan aplikasi *streaming* musik. Jika ingin dikembangkan, ada baiknya melibatkan artis-artis atau musisi-musisi sebagai bentuk riset dan izin penggunaan data-data terkait, karena pada hal-hal tersebut melekat hak cipta dan hak kekayaan intelektual yang dimiliki oleh pihak terkait.
3. Karena ini adalah fase awal, program ini belum bisa dijalankan dengan memutar file lagu yang bisa didengarkan secara nyata.
4. Pada fase kali ini, program memiliki keterbatasan yaitu hanya dapat membuat satu playlist saja. Belum bisa menambah playlist lain dengan menyimpan playlist sebelumnya yang sudah dibuat.
5. Sistem daftar antrian juga masih sangat terbatas. Pengguna masih belum bisa menambahkan secara manual lagu-lagu mana yang ingin didengarkan selanjutnya.
6. Segala bentuk perubahan dalam sistem program belum bisa disimpan secara lokal. Hal ini membuat program akan ter-*reset* setiap kali program ditutup.

### Kesimpulan
Program ini bertujuan untuk membantu pengguna membuat playlist personal dari kumpulan lagu yang ada secara sederhana dan mudah dimengerti. Ruang perbaikan juga dapat menjadi acuan untuk pengembangan program, atau bisa juga menjadi referensi program-program lain yang sejenis.

---


Dibuat oleh Satrio Bagus Prabowo

JCDS 2602, Purwadhika Digital Technology School, BSD

2025
