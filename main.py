print('##  Program Python Menghitung Gaji Karyawan  ##')
print('===============================================')
print()
#input
nama = input('Nama Karyawan:')
golongan = input('Masukan golongan:')
jam_kerja = int(input('masukan Jam kerja:'))

# Menggunakan ElseIf karena agar kompatible di python versi sebelumnya
if golongan == "A":
  upah_per_jam = 5000
elif golongan == "B":
  upah_per_jam = 7000
elif golongan == "C":
  upah_per_jam = 8000
elif golongan == "D":
  upah_per_jam = 10000
 
total_upah = jam_kerja * upah_per_jam

#cek kerja >48jam
if (jam_kerja-48) > 0:
  total_upah = total_upah + ((jam_kerja - 48)*4000)

# proses output
print(nama,'menerima upah Rp.',total_upah,'per minggu')  