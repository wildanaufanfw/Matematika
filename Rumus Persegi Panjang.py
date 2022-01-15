import os

def clear():
    os.system('cls')

def garis():
    print('-'*45)

def EP():
    clear()
    garis()
    print('''
    MENCARI LUAS SUATU PERSEGI PANJANG
    ''')
    garis()
    print('')
    print('L = Panjang X Lebar')
    print('')
    p = int(input('Masukkan Panjang Sisi Persegi Panjang (cm) : '))
    l = int(input('Masukkan Lebar Sisi Persegi Panjang (cm) : '))
    L = p*l
    print('')
    print(f'Luas Persegi Tersebut {L}cm persegi dengan panjang sisi {p}cm dan lebar sisi {l}cm')
    print('')
    input('Tekan [Enter] Untuk Kembali Ke Menu ')
    menu()

def login():
    clear()
    garis()
    print('''
                SELAMAT DATANG 
        DI OPERASI MATEMATIKA SEDERHANA
             LUAS PERSEGI PANJANG
    ''')
    garis()
    while True:
        user = 'admin'
        pas = 'admin'
        
        username = input('Masukkan Username : ')
        password = input('Masukkan Password : ')
        
        if username == user :
            if password == pas :
                garis()
                input('Selamat Anda Telah Berhasil Login, Tekan [Enter] Untuk Melanjutkan ')
                menu()
            else : 
                print('')
                print('Password Yang Anda Masukkan Salah, Silahkan Login Kembali')
                print('')
                input('Tekan [Enter] Untuk Login Kembali')
                clear()
                login()
        else :
            print('')
            print('Username Yang Anda Masukkan Salah, Silahkan Login Kembali')
            print('')
            input('Tekan [Enter] Untuk Login Kembali')
            clear()
            login()

def menu():
    clear()
    garis()
    print('''
        MENU OPERASI MATEMATIKA
         LUAS PERSEGI PANJANG
    ''')
    garis()
    print('''       
1. Mencari Luas Persegi Panjang
2. Exit
    ''')
    pilih = int(input('Silahkan Pilih Salah Satu Menu Di Atas : '))
    if pilih == 1 :
        EP()
    elif pilih == 2 :
        exit()
    else :
        print('')
        input('Pilihan Menu Tidak Ada, Tekan [Enter] Untuk Memilih Kembali ')
        menu()

def exit():
    clear()
    garis()
    print('                TERIMA KASIH')
    garis()
    input()

login()

