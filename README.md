# Jatuh Suka 
Program Python sederhana yang menampilkan lirik lagu "Jatuh Suka" dengan efek mesin ketik di terminal. Setiap karakter muncul satu per satu dengan jeda waktu sehingga memberikan pengalaman seperti sedang mengetik lirik secara langsung.

## Fitur

- Efek mesin ketik untuk setiap karakter.
- Jeda antar baris agar mengikuti alur lagu.
- Tampilan terminal menggunakan warna ANSI.
- Menampilkan bagian instrumental.
- Dapat dihentikan kapan saja menggunakan `Ctrl + C`.

## Persyaratan

- Python 3.8 atau lebih baru.
- Terminal yang mendukung ANSI Escape Code.

## Cara Menjalankan

1. Clone repository.

```bash
git clone https://github.com/username/jatuh-suka-typewriter.git
```

2. Masuk ke folder proyek.

```bash
cd jatuh-suka
```

3. Jalankan program.

```bash
python main.py
```

atau

```bash
python3 main.py
```

## Struktur Proyek

```text
jatuh-suka/
│
├── main.py
└── README.md
```

## Cara Kerja

1. Program mengaktifkan dukungan ANSI pada terminal Windows.
2. Menampilkan judul lagu.
3. Membaca daftar lirik yang telah disimpan.
4. Menampilkan setiap karakter dengan efek mesin ketik.
5. Memberikan jeda antar baris sesuai waktu yang ditentukan.
6. Menampilkan pesan penutup setelah seluruh lirik selesai.

## Konfigurasi

Setiap baris lirik memiliki tiga parameter.

```python
("Teks Lirik", delay_karakter, jeda_baris)
```

Contoh:

```python
("Sungguh ku tidak memiliki daya", 0.08, 1.2)
```

Keterangan:

- `delay_karakter` mengatur kecepatan munculnya setiap karakter.
- `jeda_baris` mengatur waktu tunggu sebelum masuk ke baris berikutnya.

## Library yang Digunakan

Program hanya menggunakan library bawaan Python.

- sys
- time
- os

Tidak memerlukan instalasi package tambahan.
