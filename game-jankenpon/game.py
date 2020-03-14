# Inisialisasi variabel untuk user memasukkan pilihan pada menu
pilihan = 0

# Kemudian user memilih pilihan dengan input string yang tertera pada menu
print("|===============================|")
print("ExitSELAMAT DATANG DI GAME JANKENPON")
print("|===============================|")
print("|========== Game Menu ==========|")
print("|===============================|")
print("|============ Mulai ============|")
print("|============ Exit =============|")
print("|===============================|")
pilihan = str(input("ketikkan pilihanmu => "))

# Fungsi untuk membuat game dan aturan pada game Batu Gunting Kertas 
def game():
    pemain1 = str(input("Silahkan pilih -> Gunting, Batu, atau Kertas => "))
    pemain2 = str(input("Silahkan pilih -> Gunting, Batu, atau Kertas => "))

    if(pemain1 == pemain2):
        print("SERI")
        print("Yok Main Lagi")
    elif(pemain1 == "Batu"):
        if(pemain2 == "Kertas"):
            print("Pemain 1 KAlah")
            print("Yok Main Lagi")
        else:
            print("Pemain 2 Menang")
            print("Yok Main Lagi")
    elif(pemain1 == "Kertas"):
        if(pemain2 == "Gunting"):
            print("Pemain 1 KAlah")
            print("Yok Main Lagi")
        else:
            print("Pemain 2 Menang")
            print("Yok Main Lagi")
    elif(pemain1 == "Gunting"):
        if(pemain2 == "Batu"):
            print("Pemain 1 KAlah")
            print("Yok Main Lagi")
        else:
            print("Pemain 2 Menang")
            print("Yok Main Lagi")
    else:
        print("Pilihan yang dimasukkan salah....")
        
# Kondisi jika pemain mebgetikkan pilihan Mulai
if pilihan != "Exit":
    game()   
    # Perulangan While digunakan untuk menampilkan pilihan bermain lagi ketika user
    # Sudah menyelesaikan permainan sebelumnya
    while True: 
        print("Masih Mau main? Y/N : ")
        pilihan = str(input("Masukkan Pilihanmu => ")) 
        if pilihan == "Y":
            game()
        else:
            break
# Ketika user mengetikkan Exit pada pilihan menu maka program akan berhenti
else:
    exit