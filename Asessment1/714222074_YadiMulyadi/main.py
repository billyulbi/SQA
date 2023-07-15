import os

print("+----------------------------------------+")
print("\tSelamat Datang")
print("\tYuk Cek Gejala Covid-19 Kamu Disini!")
print("+----------------------------------------+")
nama = input("Nama\t: ")

pilihan = input("Hai "+nama+",\nApakah kamu mau Diagnosa? (y/n)")

os.system("cls")

while pilihan == "y":
    print("\nApakah kamu merasakan gejala berikut ini?")
    print("1. Demam/Suhu Badan Tinggi")
    print("2. Sakit Kepala")
    print("3. Hidung Berair")
    print("4. Batuk dan Pilek")
    print("5. Sakit Tenggorokan")
    print("6. Hilang Penciuman/Terasa Pahit")
    diag1 = input("Jawab (y/n) : ")

    if diag1 == "y":
        print("\nApakah kamu juga merasakan gejala berikut ini? :")
        print("1. Demam yang mungkin cukup tinggi bila pengidap mengidap pneumonia")
        print("2. Batuk dengan lendir")
        print("3. Sesak Napas")
        print("4. Nyeri Dada atau Sesak saat bernapas atau batuk")
        diag2 = input("Jawab (y/n) : ")

        if diag2 == "y":
            print("\nHai, " + nama + " hasil awal diagnosa kamu adalah :")
            print("Teridentifikasi kamu terpapar Covid-19, segera lakukan pengecekan ke Rumah Sakit/Puskesmas terdekat")
        elif diag2 == "n":
            print("\nApakah kamu juga merasakan gejala berikut ini? :")
            print("1. Merasa pegal dan linu pada sendi dan tulang")
            print("2. Diare")
            diag3 = input("Jawab (y/n) :")

            if diag3 == "y":
                print("\nHai, " + nama + " hasil diagnosa kamu adalah :")
                print("Bisa dipastikan Terkena Covid-19, segera periksakan")
            elif diag3 == "n":
                print("\nHai, " + nama + " Sepertinya ada indikasi Penyakit lain. Coba Cek")
            else:
                print("\nHai, " + nama + " Sepertinya Kamu kelelahan")

        else:
            print("\nHai, " + nama + " Sepertinya Kamu kelelahan")

    elif diag1 == "n":
        print("\nHai, " + nama + " Sepertinya Kamu Khawatir Terpapar Covid-19")
    else:
        print("\nHai, " + nama + " Perintah yang kamu masukkan Salah, Coba Lagi ")
    print("+----------------------------------------+")
    pilihan = input("Hai " + nama + ",\nApakah kamu mau Cek Ulang? (y/n)")

    if pilihan == "y":
        os.system("cls")
        print("+----------------------------------------+")
        print("\tCek Gejala Covid")
        print("\tCek Gejala Covid-19 Kamu Disini")
        print("+----------------------------------------+")
    else:
        print("+----------- Terima Kasih ---------------+")
