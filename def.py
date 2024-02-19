#def halo_python():
 #   print('Halo Python')

# Panggil fungsi
#halo_python()

###

#def sapa_nama(nama_panggilan):
#    print(f'Halo {nama_panggilan}, Selamat Datang!')
#
#sapa_nama('Jamal')
#sapa_nama('Firmansyah')

###

#def luas_persegi (sisi):
#    return sisi * sisi

# Tidak menghasilkan output dalam CLI
#print(luas_persegi(10))

# output fungsi luas_persegi, dimasukkan ke parameter fungsi print
#print('Luas persegi dengan sisi 4 adalah:', luas_persegi(4))

# kita juga bisa simpan di variabel
# persegi_besar = luas_persegi(100)
#persegi_kecil = luas_persegi(50)

#print('Total luas persegi besar dan kecil adalah:', persegi_besar + persegi_kecil)

###

#kota = 'Bandung'

#def cetak_kota() :
#    print(kota)

#print('[Panggil secara langsung]',kota)
#print('[Panggil fungsi cetak_kota]', end=' ')

#cetak_kota()

###

#kota, provinsi = 'Bandung', ' Jawa Barat'

#def contoh_var_lokal():
#    kota = 'Madura'
#    provinsi = 'Jawa Timur'
#    print(kota, provinsi)

#print('[Panggil fungsi contoh_var_loakl()]')
#contoh_var_lokal()

#print('\n[Panggil variabel secara langsung]')
#print(kota, provinsi)

###

"""
Modul matematika yang berisi variabel pi dengan nilai hasil bagi dari 22/7 dan dua buah fungsi, yaitu luas_persegi dan luas_lingkaran.
"""

pi = 22 / 7

def luas_persegi (sisi):
    return sisi * sisi

def luas_lingkaran (radius):
    return pi * radius * radius