import os
os.system('cls')
from prettytable import PrettyTable

print("=============================================")
print("Nama     : Fitriani                          ")
print("NIM      : 2309116021                        ")
print("Kelas    : Sistem Informasi A23              ")
print("Tema     : Manajemen Inventaris Toko Sepatu  ")
print("=============================================")
print("*****Hallo Selamat Datang Di Toko Sepatu Helen, Selamat Berbelanja:)*****")


class Barang_sepatu:
    def __init__(self, kode, nama, merek, ukuran, harga, stok):
        self.kode = kode
        self.nama = nama
        self.merek = merek
        self.ukuran = ukuran
        self.harga = harga
        self.stok = stok

class Node:
    def __init__(self, barang):
        self.barang = barang
        self.prev = None
        self.next = None

class Inventaris_Sepatu:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_sepatu_di_awal(self, barang):
        new_node = Node(barang)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            print("Berhasil menambahkan barang.")
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            print("Berhasil menambahkan barang.")

    def tambah_sepatu_di_akhir(self, barang):
        new_node = Node(barang)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            print("Berhasil menambahkan barang.")
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            print("Berhasil menambahkan barang.")

    def tambah_sepatu_di_tengah(self, barang, posisi):
        if posisi == 0:
            self.tambah_sepatu_di_awal(barang)
        else:
            new_node = Node(barang)
            current = self.head
            count = 0
            while current and count < posisi - 1:
                current = current.next
                count += 1
            if current:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                print("Berhasil menambahkan barang.")
            else:
                print("Gagal menambahkan barang.")

    def hapus_sepatu_di_awal(self):
        if not self.head:
            print("Linked List sudah kosong")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            print("Berhasil menghapus barang.")
        else:
            self.head = self.head.next
            self.head.prev = None
            print("Berhasil menghapus barang.")

    def hapus_sepatu_di_akhir(self):
        if not self.head:
            print("Linked List sudah kosong")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            print("Berhasil menghapus barang.")
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            print("Berhasil menghapus barang.")

    def hapus_sepatu_di_tengah(self, posisi):
        if not self.head:
            print("Linked List sudah kosong")
            return
        if posisi == 0:
            self.hapus_sepatu_di_awal()
        else:
            current = self.head
            count = 0
            while current and count < posisi:
                current = current.next
                count += 1
            if current == self.tail:
                self.hapus_sepatu_di_akhir()
            elif current:
                current.prev.next = current.next
                current.next.prev = current.prev
                print("Berhasil menghapus barang.")
            else:
                print("Gagal menghapus barang.")

    def update_barang(self, kode, nama_baru, merek_baru, ukuran_baru, harga_baru, stok_baru):
        current = self.head
        while current:
            if current.barang.kode == kode:
                current.barang.nama = nama_baru
                current.barang.merek = merek_baru
                current.barang.ukuran = ukuran_baru
                current.barang.harga = harga_baru
                current.barang.stok = stok_baru
                print("Barang berhasil diperbarui.")
                return
            current = current.next
        print("Barang dengan kode tersebut tidak ditemukan.")

    def tampilkan_inventaris(self):
        if not self.head:
            print("Inventaris kosong")
            return
        table = PrettyTable(["Kode", "Nama", "Merek", "Ukuran", "Harga", "Stok"])
        current = self.head
        while current:
            barang = current.barang
            table.add_row([barang.kode, barang.nama, barang.merek, barang.ukuran, barang.harga, barang.stok])
            current = current.next
        print(table)

def main():
    inventaris = Inventaris_Sepatu()
    while True:
        print("============================================")
        print("                   Menu:                    ")
        print("1. Tambah Sepatu Baru di Awal               ")
        print("2. Tambah Sepatu Baru di Akhir              ")
        print("3. Tambah Sepatu Baru di Tengah             ")
        print("4. Hapus Sepatu di Awal                     ")
        print("5. Hapus Sepatu di Akhir                    ")
        print("6. Hapus Sepatu di Tengah                   ")
        print("7. Update Data Sepatu                       ")
        print("8. Tampilkan Inventaris/Daftar Sepatu       ")
        print("9. Keluar                                   ")
        print("============================================")
        opsi = input("Masukkan Opsi Anda: ")

        if opsi == "1":
            kode = input("Masukkan Kode Sepatu: ")
            nama = input("Masukkan Nama Sepatu: ")
            merek = input("Masukkan Merek Sepatu: ")
            ukuran = input("Masukkan Ukuran Sepatu: ")
            harga = input("Masukkan Harga Sepatu: ")
            stok = input("Masukkan Stok Sepatu: ")
            barang_baru = Barang_sepatu(kode, nama, merek, ukuran, harga, stok)
            inventaris.tambah_sepatu_di_awal(barang_baru)

        elif opsi == "2":
            kode = input("Masukkan Kode Sepatu: ")
            nama = input("Masukkan Nama Sepatu: ")
            merek = input("Masukkan Merek Sepatu: ")
            ukuran = input("Masukkan Ukuran Sepatu: ")
            harga = input("Masukkan Harga Sepatu: ")
            stok = input("Masukkan Stok Sepatu: ")
            barang_baru = Barang_sepatu(kode, nama, merek, ukuran, harga, stok)
            inventaris.tambah_sepatu_di_akhir(barang_baru)

        elif opsi == "3":
            posisi = int(input("Masukkan posisi untuk menambahkan sepatu: "))
            kode = input("Masukkan Kode Sepatu: ")
            nama = input("Masukkan Nama Sepatu: ")
            merek = input("Masukkan Merek Sepatu: ")
            ukuran = input("Masukkan Ukuran Sepatu: ")
            harga = input("Masukkan Harga Sepatu: ")
            stok = input("Masukkan Stok Sepatu: ")
            barang_baru = Barang_sepatu(kode, nama, merek, ukuran, harga, stok)
            inventaris.tambah_sepatu_di_tengah(barang_baru, posisi)

        elif opsi == "4":
            inventaris.hapus_sepatu_di_awal()

        elif opsi == "5":
            inventaris.hapus_sepatu_di_akhir()

        elif opsi == "6":
            posisi = int(input("Masukkan posisi untuk menghapus sepatu: "))
            inventaris.hapus_sepatu_di_tengah(posisi)

        elif opsi == "7":
            kode = input("Masukkan Kode Sepatu yang akan diperbarui: ")
            nama_baru = input("Masukkan Nama Baru: ")
            merek_baru = input("Masukkan Merek Baru: ")
            ukuran_baru = input("Masukkan Ukuran Baru: ")
            harga_baru = input("Masukkan Harga Baru: ")
            stok_baru = input("Masukkan Stok Baru: ")
            inventaris.update_barang(kode, nama_baru, merek_baru, ukuran_baru, harga_baru, stok_baru)

        elif opsi == "8":
            inventaris.tampilkan_inventaris()

        elif opsi == "9":
            print("Terimakasih Telah Berbelanja")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
