# Meminta pengguna untuk memasukkan sebuah angka
# Input dari pengguna akan diterima sebagai string, 
# jadi perlu dikonversi menjadi integer
angka = int(input("Masukkan sebuah angka: "))

# Mengevaluasi apakah angka tersebut ganjil atau genap
# Jika hasil bagi angka dengan 2 adalah 0, maka angka tersebut genap
if angka % 2 == 0:
    # Menampilkan hasil jika angka genap
    print(f"Angka {angka} adalah genap")
else:
    # Menampilkan hasil jika angka ganjil
    print(f"Angka {angka} adalah ganjil")