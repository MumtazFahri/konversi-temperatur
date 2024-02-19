# buka & baca file
file = open('data.txt', 'r')

# baca per baris
line1 = file.readline()
line2 = file.readline()

# cetak data
print(line1)
print(line2)

# tutup data
file.close()