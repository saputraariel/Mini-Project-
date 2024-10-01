print("----------------------------")
Nama = input("Masukan Nama = ")
Nim = input("Masukan Nim = ")
print("----------------------------")
print("Selamat Datang,{},Dengan Nim = {}.Sekarang inputkan data kerja dan juga tarif kerja anda".format(Nama, Nim))
print("----------------------------")

#PENGULANGAN
Pengulangan = "iya"

while(Pengulangan == "iya"):
    jamkerja = float(input("Masukan Data Jam Kerja = "))
    tarifkerja = float(input("Masukan Tarif Kerja = Rp. "))
    
    #menghitung gaji dari tarif kerja di kali jamkerja
    gaji = jamkerja * tarifkerja

    if jamkerja > 160:
        bonus = gaji * 0.1
        gajitotal = gaji + bonus
        print("anda mendapatkan bonus 10%")
        print("Jadi total Gaji Anda Adalah = ", gajitotal)
    else:
        print("Anda tidak mendapatkan bonus")
        print("Jadi Total Gaji Anda Adalah = ", gaji)
    
    while True:
        Pengulangan = input("Apakah ingin melanjutkan iya/tidak = ")
        if(Pengulangan == "iya"):
            print("Anda Memilih untuk Melanjutkan")
            break #untuk keluar dari while true(pengulangan)
        elif(Pengulangan == "tidak"):
            print("Anda Memilih Untuk Tidak Melanjutkan")
            exit() #berhenti
        else:
            print("Kata yang anda input salah/data hanya memakai huruf kecil. 'iya' atau 'tidak'.")