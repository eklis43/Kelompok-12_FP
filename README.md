# Kelompok-12_FP

Tamplate github : https://github.com/thosangs/dibimbing_km_final_project 

Kelompok 12 
1.     Khidlira Arofat Nuciferadha
2.     Ecclesiani
3.     Riski Syahputra
4.     Yuni Dwi Ariyanti
5.     Tiandra Rizkya Pramadhani

How To

Tujuan kami meminimalkan resource , dan kelompok ini menggunakan database cloud gratis di NEON. Setelah kita membuat database di dalamnya, ambil string koneksi dan masukkan ke dalam variabel DW_POSTGRES_URI di .env . 
 
DW_POSTGRES_URI="postgresql://neondb_owner:SCzLXNE3r9YT@ep-icy-silence-a5cwtr8m.us-east-2.aws.neon.tech/neondb?sslmode=require"

Untuk menjalankan container, pertama-tama kita harus membuat semua image Docker yang diperlukan 

make build

Setelah semua gambar dibuat, kita dapat mencoba memutar containernya

make spinup

Setelah semua container siap, kita dapat menggunakannya. 

Akses the Airflow on port 8081
Akses Metabase pada port 3001, untuk username dan passwordnya bisa coba akses file .env . 
Jika tidak menemukan tabel yang dibuat di data Metabase Telusuri, Anda dapat mencoba menyinkronkannya melalui UI admin Metabase. 

Struktur Folder
1. main

Di folder utama, kita dapat menemukan makefile, jika ingin mengotomatiskan skrip apa pun, Anda dapat mencoba memodifikasinya.

Ada juga requirements.txt, jadi jika Anda ingin menambahkan perpustakaan ke wadah Airflow, Anda bisa mencoba menambahkannya di sana. Setelah Anda menambahkan nama perpustakaan dalam file, pastikan Anda membangun kembali gambar sebelum memutar wadahnya.

2. dag

Di sinilah Anda meletakkan file dag Anda. Folder ini sudah terpasang di penampung, sehingga pembaruan apa pun di sini akan otomatis berlaku di sisi penampung. Folder ini juga berisikan data warehouse atau silver dan data mart atau gold dalam bentuk sql. 

3. data

Folder ini berisi data yang diperlukan untuk proyek Anda. Jika Anda ingin membuat atau menambahkan data tambahan, Anda dapat menempatkannya di sini.

4. docker

Di sinilah Anda dapat mengubah atau menambahkan tumpukan buruh pelabuhan baru jika Anda memutuskan untuk memperkenalkan tumpukan data baru di platform data Anda. Anda bebas memodifikasi docker-compose.yml dan Dockerfile.airflow yang diberikan.

5. script

Folder ini berisi skrip yang diperlukan untuk mengotomatisasi proses inisialisasi pada pengaturan docker-container.
