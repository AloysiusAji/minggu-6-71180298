#Aloysius Gonzaga Ardhian Krisna Aji
#71180298

# Di suatu malam Danto sedang berusaha membuat sebuah program kelipatan bilangan asli,
# sebagai teman baiknya kamu harus menolong danto. 

#inputan
#bilangan asli
#kelipatannya sesuai keinginan user

#output 
#menunjukan bilangan tersebut adalah kelipatan atau bukan kelipatan.

loop = True
while loop:
    print("\n<=== Program Kelipatan Bilangan Asli ===>")
    bilangan = int(input("Masukan bilangan asli: "))
    kelipatan = int(input("Masukan kelipatan yang diinginkan: "))
    if bilangan > 0:
        for i in range (0,1,bilangan+1):
            if(bilangan % kelipatan) == 0:
                print(bilangan,"Merupakan kelipatan",kelipatan)
            else:
                print(bilangan,"Bukan kelipatan",kelipatan)
    else:
        masukan = str(input("Masukan angka harus lebih dari nol, lanjut(Y/T)"))
        if masukan == "T":
            loop = False
            print("Program Selesai")
        elif masukan == "Y":
            loop = True
        else:
            print("Inputan anda tidak sesuai, kembali ke menu awal")

