#Nama Adosetiawan
#NIM 201111101
#Prodi Informatika

#array asli
datasaya = ['nama:ado setiawan','umur:20']
print(datasaya)

#array elemen tambah
datasaya.append('Hobi:ngoding')
print(datasaya)

#ubah elemen array 
datasaya[1] = '21'

#array hapus
datasaya.pop(1)
print(datasaya)

#array dimensi
matrix = [
          [1,0,1,],
          [0,1,0,],
          [1,0,1,],
        ]

for baris in matrix:
  for kolom in baris:
    print(kolom, end = "")
  print()
