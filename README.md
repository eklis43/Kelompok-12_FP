# Kelompok-12_FP

Tamplate github : https://github.com/thosangs/dibimbing_km_final_project 

Kelompok 12 
1.     Khidlira Arofat Nuciferadha
2.     Ecclesiani
3.     Riski Syahputra
4.     Yuni Dwi Ariyanti
5.     Tiandra Rizkya Pramadhani

How To

Tujuan kami meminimalkan resource , dan kelompok ini menggunakan database cloud gratis di NEON. Setelah kita membuat database di dalamnya, ambil string koneksi dan masukkan ke dalam variabel DW_POSTGRES_URI di .env
 
DW_POSTGRES_URI="postgresql://neondb_owner:SCzLXNE3r9YT@ep-icy-silence-a5cwtr8m.us-east-2.aws.neon.tech/neondb?sslmode=require"

Untuk menjalankan container, pertama-tama kita harus membuat semua image Docker yang diperlukan 

make build

Setelah semua gambar dibuat, kita dapat mencoba memutar containernya

make spinup

Setelah semua container siap, kita dapat menggunakannya

Akses the Airflow on port 8081
Akses Metabase pada port 3001, untuk username dan passwordnya bisa coba akses file .env
Jika tidak menemukan tabel yang dibuat di data Metabase Telusuri, Anda dapat mencoba menyinkronkannya melalui UI admin Metabase
