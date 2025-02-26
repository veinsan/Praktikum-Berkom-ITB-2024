# NIM/Nama : 19624156/Riantama Putra
# Tanggal : 17/10/2024
# Deskripsi : Problem 01

#Program NilaiAkhir
#Menhitung nilai akhir dari rata-rata kuis 1, kuis 2, kuis 3

#KAMUS
# A, B, C : int

#ALGORITMA
A = int(input("Masukkan nilai kuis pertama: "))
B = int(input("Masukkan nilai kuis kedua: "))
C = int(input("Masukkan nilai kuis ketiga: "))

N = (A+B+C)/3

if (N >= 80):
    print ("Tuan Leo mendapatkan nilai Lulus Memuaskan.")
elif (N>=70):
    print ("Tuan Leo mendapatkan nilai Lulus.")
else:
    print("Tuan Leo mendapatkan nilai Tidak Lulus.")