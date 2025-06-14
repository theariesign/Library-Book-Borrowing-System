import sys
from datetime import datetime
import time
from tabulate import tabulate
import os

print()
program = "PERPUSTAKAAN DIGITAL"
univ = "UNIVERSITAS JENDERAL ACHMAD YANI"
pr_program = program.center(100)
un_univ = univ.center(100)

print("=" * 100)
print(pr_program)
print(un_univ)
print("=" * 100)
localtime = time.asctime(time.localtime(time.time()))
print("SELAMAT DATANG!", localtime.center(143))


daftarbuku = [
    ["Kode Buku", "Judul Buku", "Penulis", "Penerbit", "Tahun Terbit"],
    ["01", "Pedoman penulisan karya ilmiah", "hery", "sleman", 2019],
    ["02", "Pemrograman dasar", "wenty", "sleman", 2018],
    ["03", "Psikologi kepribadian", "anton", "yogyakarta", 2015],
    ["04", "Logika pemrograman", "abdul kadir", "jakarta", 2020],
    ["05", "Belajar dasar accurate", "alwisol", "jakarta", 2014],
]


class admin:
    def __init__(self, kodebuku, judul, penulis, penerbit, tahunterbit):
        self.kodebuku = kodebuku
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahunterbit = tahunterbit

    def __tambahbuku(self):
        t = "TAMBAH BUKU"
        str_t = t.center(100)
        print()
        print("=" * 100)
        print(str_t)
        print("=" * 100)
        print()
        x = input("Kode Buku    : ")
        y = input("Judul Buku   : ")
        w = input("Penulis      : ")
        z = input("Penerbit     : ")
        s = input("Tahun Terbit : ")
        daftarbuku.append([x, y, w, z, s])
        print(
            """
                                +-------------------------------------+
                                |                                     |
                                | SELAMAT BUKU ANDA TELAH DITAMBAHKAN |
                                |       DI PERPUSTAKAAN DIGITAL       |
                                |                                     |
                                +-------------------------------------+
            """
        )

    def tampiltambahbuku(self):
        self.__tambahbuku()

    def tampilanggota(self):
        t = "TAMPIL ANGGOTA"
        str_t = t.center(100)
        print()
        print("=" * 100)
        print(str_t)
        print("=" * 100)
        print()
        for i in range(len(namapeminjam)):
            print("Waktu                        :", localtime)
            print("nama peminjam                :", namapeminjam[i])
            print("judul buku                   :", pinjambuku[i])
            print("Kode Buku                    :", kode[i])
            print("penulis buku                 :", tulisbuku[i])
            print("penerbit buku                :", terbitbuku[i])
            print("tahun terbit                 :", terbittahun[i])
            print("Tanggal Pinjam               :", tanggal[i])
            print("Tanggal Kembali              :", kembali[i])
            print()

    def pinjam_buku():
        pass

    def pengembalian_buku():
        pass


class Buku:
    def __init__(self, kodebuku, judul, penulis, penerbit, tahun_terbit):
        self.kodebuku = kodebuku
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit

    def tampil_daftar_buku():
        a = "DAFTAR BUKU PERPUSTAKAAN"
        str_a = a.center(100)
        print()
        print("=" * 100)
        print(str_a)
        print("=" * 100)
        print()
        print(tabulate(daftarbuku, headers="firstrow", tablefmt="fancy_grid"))
        print()


kode = []
namapeminjam = []
pinjambuku = []
tulisbuku = []
terbitbuku = []
terbittahun = []
tanggal = []
kembali = []


class anggota(admin, Buku):
    def __init__(self, nama_peminjam, judul, tanggal_pinjam):
        self.nama_peminjam = nama_peminjam
        self.judul = judul
        self.tanggal_pinjam = tanggal_pinjam

    def pinjambuku(self):
        x = "PINJAM BUKU"
        str_x = x.center(100)
        print()
        print("=" * 100)
        print(str_x)
        print("=" * 100)
        print()
        while True:
            peminjam = input("Nama Peminjam               : ")
            namapeminjam.append(peminjam)
            judulbuku = input("Judul Buku                  : ")
            pinjambuku.append(judulbuku)
            try:
                kode_buku = int(input("Kode Buku                   : "))
                kode.append(kode_buku)
                daftarbuku.pop(kode_buku)
                break
            except IndexError:
                print()
                print("Kode Buku tidak ada dalam daftar")
                print()
        tulis = input("Penulis Buku                : ")
        tulisbuku.append(tulis)
        terbit = input("Penerbit Buku               : ")
        terbitbuku.append(terbit)
        tahun = input("Tahun Terbit                : ")
        terbittahun.append(tahun)
        tanggal_pinjam = input("Tanggal Pinjam (DD-MM-YYYY) : ")
        tanggal.append(tanggal_pinjam)
        print()
        print()
        print(
            """
                                +------------------------------------+
                                | NOTE :                             |
                                |------------------------------------|
                                | TOLONG KEMBALIKAN BUKU TEPAT WAKTU |
                                | DAN DALAM KEADAAN BAIK!            |
                                +------------------------------------+
            """
        )

    def pengembalianbuku(self):
        c = "PENGEMBALIAN BUKU"
        str_c = c.center(100)
        print()
        print("=" * 100)
        print(str_c)
        print("=" * 100)
        print()
        while True:
            nama = input("nama peminjam                : ")
            judul = input("judul buku                   : ")
            try:
                kodebuku = int(input("Kode Buku                    : "))
                if kodebuku == 1:
                    daftarbuku.insert(
                        kodebuku,
                        [
                            "01",
                            "pedoman penulisan karya ilmiah",
                            "hery",
                            "sleman",
                            "2019",
                        ],
                    )
                    break
                elif kodebuku == 2:
                    daftarbuku.insert(
                        kodebuku, ["02", "pemrograman dasar", "wenty", "sleman", "2018"]
                    )
                    break
                elif kodebuku == 3:
                    daftarbuku.insert(
                        kodebuku,
                        ["03", "psikologi kepribadian", "anton", "yogyakarta", "2015"],
                    )
                    break
                elif kodebuku == 4:
                    daftarbuku.insert(
                        kodebuku,
                        ["04", "logika pemrograman", "abdul kadir", "jakarta", "2015"],
                    )
                    break
                elif kodebuku == 5:
                    daftarbuku.insert(
                        kodebuku,
                        ["05", "belajar dasar accurate", "alwisol", "jakarta", "2014"],
                    )
                    break
                elif kodebuku == 6:
                    daftarbuku.insert(
                        kodebuku,
                        [
                            "06",
                            "astrologi",
                            "van dier",
                            "germany",
                            "2014",
                        ],
                    )
                    break
                elif kodebuku == 7:
                    daftarbuku.insert(
                        kodebuku,
                        [
                            "07",
                            "folklore",
                            "jack antonof",
                            "nashville",
                            "2020",
                        ],
                    )
                    break
            except ValueError:
                print()
                print("INPUTAN HARUS BERUPA ANGKA!!!")
                print()
            else:
                print()
                print("Maaf Buku Tidak Ada Sebelumnya")
                print()
        tulis = input("penulis buku                 : ")
        terbit = input("penerbit buku                : ")
        tahun = input("tahun terbit                 : ")
        tanggalpinjam = input("Tanggal Pinjam (DD-MM-YYYY)  : ")
        tanggalkembali = input("Tanggal Kembali (DD-MM-YYYY) : ")
        kembali.append(tanggalkembali)
        tanggal_pinjam = datetime.strptime(tanggalpinjam, "%d-%m-%Y")
        tanggal_kembali = datetime.strptime(tanggalkembali, "%d-%m-%Y")
        selisih_hari = (tanggal_kembali - tanggal_pinjam).days
        if selisih_hari > 7:
            denda_per_hari = 1000
            total_denda = selisih_hari * denda_per_hari
            print()
            print(
                f"Anda terlambat mengembalikan buku {selisih_hari} hari, Total denda: {total_denda} rupiah."
            )
            print()
            print(
                """
                                +-----------------------------------+
                                |                                   |
                                |  TERIMAKASIH TELAH MEMINJAM BUKU  |
                                |      DI PERPUSTAKAAN DIGITAL      |
                                |                                   |
                                +-----------------------------------+
                """
            )
        else:
            print()
            print("Tidak ada denda.")
            print()
            print(
                """
                                +-----------------------------------+
                                |                                   |
                                |  TERIMAKASIH TELAH MEMINJAM BUKU  |
                                |      DI PERPUSTAKAAN DIGITAL      |
                                |                                   |
                                +-----------------------------------+
                """
            )


# =============================================================================
# =============================== MAIN UTAMA ==================================
# =============================================================================


def mainutama():
    print(
        """
                                +------------------------------+
                                |            LOGIN             |
                                |------------------------------|
                                | [1] Petugas                  |
                                | [2] Anggota                  |
                                | [3] Exit                     |
                                +------------------------------+
            """
    )
    pilih = int(input("Pilih Akses: "))
    os.system("cls")
    print()
    if pilih == 1:
        petugas()
        print()
    elif pilih == 2:
        masuk()
    elif pilih == 3:
        sys.exit()


# ========================================================================
# ======================= LOGIN UNTUK PETUGAS ============================
# ========================================================================


def petugas():
    print()
    program = "PERPUSTAKAAN DIGITAL"
    univ = "UNIVERSITAS JENDERAL ACHMAD YANI"
    pr_program = program.center(100)
    un_univ = univ.center(100)
    print("=" * 100)
    print(pr_program)
    print(un_univ)
    print("=" * 100)
    localtime = time.asctime(time.localtime(time.time()))
    print("SELAMAT DATANG!", localtime.center(143))
    x = 2
    while x >= 2:
        try:
            username = input("\nmasukan username : ")
            password = int(input("masukan password : "))
            if password == 123:
                print()
                print("-" * 100)
                print(" " * 30, "Selamat", username, "Kamu Berhasil Login", " " * 28)
                print("-" * 100)
                os.system("cls")
                mainmenu()
                break
            else:
                print("\npasword salah !")
        except ValueError:
            print()
            print(
                "kesalahan dalam inputan \nSilahkan ulang kembali pasword dengan angka !"
            )


def tanya2():
    print("=" * 100)
    tanyain = input("Kembali ke Menu Utama? ")
    os.system("cls")
    mainmenu()


def tambahlagi():
    b = admin(None, None, None, None, None)
    tambah = input("Ingin Tambah buku lagi ? ")
    while True:
        if tambah == "Y" or tambah == "y":
            b.tampiltambahbuku()
            tambahlagi()
        elif tambah == "N" or tambah == "n":
            tanya2()


def mainmenu():
    h = admin(None, None, None, None, None)
    done = False
    while not done:
        print(
            """
                                +------------------------------+
                                |          MENU UTAMA          |
                                |------------------------------|
                                | [1] Tambah Buku              |
                                | [2] Tampil Anggota           |
                                | [3] Kembali                  |  
                                | [4] Exit                     |
                                +------------------------------+
            """
        )
        pilih = int(input("Pilih Menu: "))
        os.system("cls")
        if pilih == 1:
            h.tampiltambahbuku()
            tambahlagi()
            tanya2()
        elif pilih == 2:
            h.tampilanggota()
            tanya2()
        elif pilih == 3:
            mainutama()
        elif pilih == 4:
            print(
                """
                                +-------------------------------+
                                |          TERIMA KASIH         |
                                |    SILAHKAN DATANG KEMBALI    |
                                +-------------------------------+
                """
            )
            sys.exit()


# =========================================================================
# ======================== LOGIN UNTUK ANGGOTA ============================
# =========================================================================


def tanya1():
    print("=" * 100)
    tanya = input("Kembali ke Menu Utama? ")
    os.system("cls")
    main2()


def pinjamlagi():
    n = anggota(None, None, None)
    tambah = input("Ingin pinjam buku lagi ? ")
    while True:
        if tambah == "Y" or tambah == "y":
            n.pinjambuku()
            pinjamlagi()
        elif tambah == "N" or tambah == "n":
            tanya1()


def balikbuku():
    a = anggota(None, None, None)
    tambah = input("ada lagi ? ")
    while True:
        if tambah == "Y" or tambah == "y":
            a.pengembalianbuku()
            balikbuku()
        elif tambah == "N" or tambah == "n":
            tanya1()


def masuk():
    print()
    program = "PERPUSTAKAAN DIGITAL"
    univ = "UNIVERSITAS JENDERAL ACHMAD YANI"
    pr_program = program.center(100)
    un_univ = univ.center(100)
    print("=" * 100)
    print(pr_program)
    print(un_univ)
    print("=" * 100)
    localtime = time.asctime(time.localtime(time.time()))
    print("SELAMAT DATANG!", localtime.center(143))
    print()
    while True:
        try:
            o = int(input("Masukan NIM    : "))
            break
        except:
            print()
            print("Inputan harus berupa angka! silahkan input kembali")
            print()
    print()
    print("-" * 100)
    print(" " * 30, "Selamat", o, "Kamu Berhasil Login", " " * 28)
    print("-" * 100)
    os.system("cls")
    main2()


def main2():
    a = anggota(None, None, None)
    b = admin(None, None, None, None, None)
    done = False
    while not done:
        print(
            """
                                +------------------------------+
                                |          MENU UTAMA          |
                                |------------------------------|
                                | [1] Tampilan Daftar Buku     |
                                | [2] Pinjam Buku              |
                                | [3] Tambah Buku              |
                                | [4] Kembalikan Buku          | 
                                | [5] Kembali                  | 
                                | [6] Exit                     |
                                +------------------------------+
            """
        )

        pilih = int(input("Pilih Menu: "))
        os.system("cls")
        if pilih == 1:
            Buku.tampil_daftar_buku()
            tanya1()
        elif pilih == 2:
            a.pinjambuku()
            pinjamlagi()
            tanya1()
        elif pilih == 3:
            print(
                """
                                +--------------------------------+
                                |         HUBUNGI PETUGAS        |
                                |          PERPUSTAKAAN          |
                                +--------------------------------+
                """
            )
            tanya1()
        elif pilih == 4:
            a.pengembalianbuku()
            balikbuku()
            tanya1()
        elif pilih == 5:
            mainutama()
        elif pilih == 6:
            print(
                """
                                +-------------------------------+
                                |          TERIMA KASIH         |
                                |    SILAHKAN DATANG KEMBALI    |
                                +-------------------------------+
                """
            )
            sys.exit()


mainutama()
mainmenu()
masuk()
main2()
