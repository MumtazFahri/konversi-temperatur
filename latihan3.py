#  buka file dengan mode w (write)
file = open('data-baru.txt', 'w')
username = input("Masukkan nama anda: ")
email = input("Masukkan alamat email anda: ")

file.write(username)
file.write("\n")
file.write(email)



# tulis data baru ke file
#file.write('Ini adalah garis pertama.\n')
#file.write('Ini adalah garis kedua.\n')
file.close()