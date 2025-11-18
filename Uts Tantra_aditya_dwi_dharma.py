# Mengambil 4 input harga barang dari user lalu dimasukkan ke list
harga = [int(input('masukkan harga barang :')) for x in range(4)]

# Input jumlah uang (budget)
budget = int(input('masukkan budget : '))

# Variabel untuk menghitung berapa barang terbeli dan berapa total biaya
barang_terbeli = 0
total_biaya = 0

# Loop pertama untuk memilih indeks j
for j in range(len(harga)):
    # Loop kedua untuk membandingkan harga[j] dengan semua elemen setelahnya
    for k in range(j + 1, len(harga)):
        # Jika elemen di posisi j lebih besar dari k, maka ditukar
        if harga[j] > harga[k]:
            harga[j], harga[k] = harga[k], harga[j]

# Menampilkan daftar harga yang sudah diurutkan
print(f"harga barang yang sudah di urutkan : {harga} \n")

# PROSES GREEDY: AMBIL BARANG DARI YANG PALING MURAH

for i in range(len(harga)):

    # Jika harga barang masih bisa dibeli sesuai budget
    if harga[i] <= budget:
        
        # Kurangi budget dengan harga barang
        budget -= harga[i]

        # Tampilkan barang yang diambil dan sisa uang
        print(f"ambil {harga[i]} sisa {budget}")

        # Tambah jumlah barang yang terbeli
        barang_terbeli += 1

        # Tambah total biaya yang dikeluarkan
        total_biaya += harga[i]

# OUTPUT AKHIR
print(f"\nTotal barang terbeli : {barang_terbeli}")
print(f"Total biaya : {total_biaya}")
