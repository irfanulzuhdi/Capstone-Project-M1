# APLIKASI DATA KARYAWAN PERUSAHAAN

### List Karyawan

listKaryawan = [
    {
        'NIK': 12345,
        'nama': 'Natasha',
        'gender':'Perempuan',
        'alamat': 'Jl.Patin No.22, JakBar',
        'jabatan': 'Junior Digital Marketing'
    },
    {
        'NIK': 14567,
        'nama': 'Diego',
        'gender':'Laki-laki',
        'alamat': 'Jl.Cempaka No.15, JakSel',
        'jabatan': 'Junior Data Scientist'
    },
    {
        'NIK': 19876,
        'nama': 'Jennie',
        'gender':'Perempuang',
        'alamat': 'Jl.Melati No.6, Tangerang',
        'jabatan': 'Junior UI/UX Design'
    }
]

def dataKaryawan():
    if listKaryawan == []:          # isi list kosong
        print()
        print('''
    \t----------* Tidak Ada Data Karyawan *----------''')
    else:
        print('''
    ===============================================================
    ------ Report Data Karyawan -----------------------------------''')
        print('''
    Data Karyawan E-MONEY:
    ======================''')
        print('''
    \tNIK \t| Nama \t\t| Gender  \t| Alamat  \t\t\t| Jabatan''')
        for idx, item in enumerate(listKaryawan):
            print(f"\t{item['NIK']} \t|  {item['nama']} \t|  {item['gender']} \t|  {item['alamat']} \t|  {item['jabatan']}")


### Menampilkan MENU READ DATA (Record Data Karyawan)
### =================================================

def MenudataKaryawan():

    print('''
    ===============================================================
    ---- MENU Report Data Karyawan --------------------------------

    |-- Menu:
        1. Report seluruh data karyawan
        2. Cari data karyawan
        3. Kembali ke Menu Utama

    ===============================================================''')
    inputmenurecord = input('''
    Silahkan pilih Menu (1-3): ''')
    if inputmenurecord == '1':
        dataKaryawan()
    elif inputmenurecord == '2':
        dataTertentu()
    elif inputmenurecord == '3':
        print('''
        -----------* Anda kembali ke Menu Utama *-----------''')
        MenuUtama()
    else:
        print()
        print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
        MenudataKaryawan()


### Menampilkan MENU 2 READ DATA (Search Data)
### =========================================

def dataTertentu():

    dataKaryawan()
    inputNIK = int(input('''
    ===============================================================
    ----| SEARCH Data Karyawan

    Masukkan Nomor Induk Karyawan (NIK) yang dicari: '''))

    for i in range(len(listKaryawan)):
        if inputNIK == listKaryawan[i]['NIK']:
            print(f'''
    Data Karyawan 'DITEMUKAN' dengan NIK: {inputNIK}''')
            print('''
    Data Karyawan E-MONEY
    ======================''')
            print('''
    \tNIK \t| Nama \t\t| Gender  \t| Alamat  \t\t\t| Jabatan''')

            print(f"\t{listKaryawan[i]['NIK']} \t|  {listKaryawan[i]['nama']} \t|  {listKaryawan[i]['gender']} \t|  {listKaryawan[i]['alamat']} \t| {listKaryawan[i]['jabatan']}")
            break

    if inputNIK != listKaryawan[i]['NIK']:
        print('''
    \t-------* Data Karyawan Tidak Ditemukan *-------''')

    MenudataKaryawan()


### Menambahkan data karyawan (MENU CREATE DATA)
### ============================================

def inputData():

    NIK_kryn = int(input('\t1. Nomor Induk Karyawan (NIK): '))
    for i in range(len(listKaryawan)):
        if NIK_kryn == listKaryawan[i]['NIK']:
            print('''
            -----* Maaf, Data Sudah Ada *-----''')
            print('''
            ---* Silahkan Masukkan Kembali *---''')
            print()

            tambahData()

        else:
            nama_kryn = input('\t2. Nama karyawan: ')
            gender_kryn = input('\t3. Gender karyawan (Laki-laki/Perempuan): ')
            alamat_kryn = input('\t4. Alamat karyawan: ')
            jabatan_kryn = input('\t5. Jabatan karyawan: ')
            break

    pemberitahuan = input('''
    ------| Apakah data akan disimpan (Y/N)? ''')
    if pemberitahuan == 'Y' or pemberitahuan == 'y':
        listKaryawan.append({
                'NIK': NIK_kryn,
                'nama': nama_kryn,
                'gender': gender_kryn,
                'alamat': alamat_kryn,
                'jabatan': jabatan_kryn
            })
        print('''
    --------------* Data Karyawan Berhasil Ditambahkan *-----------
    ===============================================================''')
    elif pemberitahuan == 'N' or pemberitahuan == 'n':
        print('''
    \t-------* Data Karyawan Tidak Ditambahkan *-------''')
    else:
        print()
        print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')

    dataKaryawan()


def tambahData():

    while True:
        tambahKaryawan = input('''
    ===============================================================
    ---- MENU Penambahan Data Karyawan ----------------------------
    |-- Menu:
        1. Tambah Data Karyawan
        2. Kembali ke Menu Utama
    ===============================================================
    Silahkan pilih Sub Menu Create Data (1-2): ''')

        if tambahKaryawan == '1':
            print()
            print('''
    -------------- Silahkan Masukkan Data Karyawan  ---------------
    ===============================================================''')
            print('''
    --| Masukkan Informasi Karyawan : ''')
            inputData()
        elif tambahKaryawan == '2':
            print('''
        -----------* Anda kembali ke Menu Utama *-----------''')
            MenuUtama()
        else:
            print()
            print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
            tambahData()


### Mengubah Data Karyawan (Menu Update Data)
### =========================================

def updateData():

    while True:
        editdataKaryawan = input('''
    ===============================================================
    ---- MENU Update Data Karyawan --------------------------------

    |-- Menu:
        1. Update Data Karyawan
        2. Kembali ke Menu Utama

    ===============================================================
    Silahkan pilih Sub Menu Update Data (1-2): ''')

        if editdataKaryawan == '1':
            dataKaryawan()
            print('\t=====================================')
            NIK_kryn = int(input('\t| Masukkan Nomor Induk Karyawan (NIK): '))
            for i in range(len(listKaryawan)):
                if NIK_kryn == listKaryawan[i]['NIK']:
                    print('''
            -----* Data karyawan ditemukan *-----''')
                    kondisi = input('''
        ---| Pilih (Y) jika ingin melanjutkan update data
        ---| Pilih (N) untuk cancel update data (Y/N): ''')
                    print()
                    if kondisi == "Y" or kondisi == 'y':
                        print('''
            -----* Lanjutkan Update Data *-----''')
                        keterangan = input('''
        ---| Pilihlah keterangan yang mau diubah:
                1. Nomor Induk Karyawan
                2. Nama Karyawan
                3. Gender Karyawan
                4. Alamat Karyawan
                5. Jabatan Karyawan

            Masukkan pilihan (1-5): ''')
                        if keterangan == '1':
                            NIK_baru = int(input('''
            ---| Masukkan Nomor Induk Karyawan (NIK) yang baru: '''))
                            kondisiketerangan = input('''
                ---- Apakah data yakin akan diubah (Y/N)? ''')
                            if kondisiketerangan == 'Y' or kondisiketerangan == 'y':
                                listKaryawan[i]['NIK'] = NIK_baru
                                print('''
    ===============================================================
    --------------* Data Karyawan BERHASIL di-update *--------------''')
                                dataKaryawan()
                            elif kondisiketerangan == 'N' or kondisiketerangan == 'n':
                                print('''
                ----* CANCEL update data *----''')
                                updateData()
                            else:
                                print()
                                print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
                                break

                        elif keterangan == '2':
                            Nama_baru = input('''
            ---| Masukkan Nama karyawan yang baru: ''')
                            kondisiketerangan = input('''
                ---- Apakah data yakin akan diubah (Y/N)? ''')
                            if kondisiketerangan == 'Y' or kondisiketerangan == 'y':
                                listKaryawan[i]['nama'] = Nama_baru
                                print('''
    ===============================================================
    --------------* Data Karyawan BERHASIL di-update *--------------''')
                                dataKaryawan()

                            elif kondisiketerangan == 'N' or kondisiketerangan == 'n':
                                print('''
                ----* CANCEL update data *----''')
                                updateData()
                            else:
                                print()
                                print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
                                break

                        elif keterangan == '3':
                            Gender_baru = input('''
            ---| Masukkan Gender karyawan yang baru: ''')
                            kondisiketerangan = input('''
                ---- Apakah data yakin akan diubah (Y/N)? ''')
                            if kondisiketerangan == 'Y' or kondisiketerangan == 'y':
                                listKaryawan[i]['gender'] = Gender_baru
                                print('''
    ===============================================================
    --------------* Data Karyawan BERHASIL di-update *--------------''')
                                dataKaryawan()

                            elif kondisiketerangan == 'N' or kondisiketerangan == 'n':
                                print('''
                ----* CANCEL update data *----''')
                                updateData()
                            else:
                                print()
                                print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
                                break

                        elif keterangan == '4':
                            Alamat_baru = input('''
            ---| Masukkan alamat karyawan yang baru: ''')
                            kondisiketerangan = input('''
                ---- Apakah data yakin akan diubah (Y/N)? ''')
                            if kondisiketerangan == 'Y' or kondisiketerangan == 'y':
                                listKaryawan[i]['alamat'] = Alamat_baru
                                print('''
    ===============================================================
    --------------* Data Karyawan BERHASIL di-update *--------------''')
                                dataKaryawan()

                            elif kondisiketerangan == 'N' or kondisiketerangan == 'n':
                                print('''
                ----* CANCEL update data *----''')
                                updateData()
                            else:
                                print()
                                print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
                                break

                        elif keterangan == '5':
                            Jabatan_baru = input('''
            ---| Masukkan Jabatan karyawan yang baru: ''')
                            kondisiketerangan = input('''
                ---- Apakah data yakin akan diubah (Y/N)? ''')
                            if kondisiketerangan == 'Y' or kondisiketerangan == 'y':
                                listKaryawan[i]['jabatan'] = Jabatan_baru
                                print('''
    ===============================================================
    --------------* Data Karyawan BERHASIL di-update *--------------''')
                                dataKaryawan()
                            elif kondisiketerangan == 'N' or kondisiketerangan == 'n':
                                print('''
                ----* CANCEL update data *----''')
                                updateData()
                            else:
                                print()
                                print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
                                break

                    elif kondisi == "N" or kondisi == 'n':
                        print('''
                ---* Cancel Update Data *---''')
                        updateData()
                    else:
                        print()
                        print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
                        break

        elif editdataKaryawan == '2':
            print('''
        -----------* Anda kembali ke Menu Utama *-----------''')
            MenuUtama()
        else:
            print()
            print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
            updateData()



### Menghapus Data Karyawan (Menu Delete Data)
### ==========================================

def deleteData():

    dataKaryawan()

    while True:
        hapusdataKaryawan = input('''
    ===============================================================
    ---- MENU Delete Data Karyawan --------------------------------

    |-- Menu:
        1. Delete Data Karyawan
        2. Kembali ke Menu Utama

    ===============================================================
    Silahkan pilih Sub Menu Delete Data (1-2): ''')

        if hapusdataKaryawan == '1':
            NIKkaryawan = int(input('''
    ---| Masukkan NIK karyawan yang ingin dihapus: '''))
            for i in range(len(listKaryawan)):
                if NIKkaryawan == listKaryawan[i]['NIK']:
                    print('''
        -----* Data Karyawan DITEMUKAN *-----''')
                    kondisihapusdata = input('''
        ---| Apakah Data yakin dihapus (Y/N)? ''')
                    if kondisihapusdata == 'Y' or kondisihapusdata == 'y':
                        NIKkaryawan == listKaryawan [i]['NIK']
                        del listKaryawan[i]
                        print(f'''
    ----* Data Karyawan NIK: {NIKkaryawan} BERHASIL dihapus *----''')
                        break

                    elif kondisihapusdata == 'N' or kondisihapusdata == 'n':
                        print('''
        ----* Data Karyawan GAGAL dihapus *----''')
                        break
                    else:
                        print()
                        print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
                        break

        elif hapusdataKaryawan == '2':
            print('''
        -----------* Anda kembali ke Menu Utama *-----------''')
            MenuUtama()

        else:
            print()
            print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
        deleteData()


### Main Menu
### =========

def MenuUtama():

    PilihMenu = input('''
    ===============================================================
    ------------------- Data Karyawan E-MONEY ---------------------
    ===============================================================

    --| Pilihan Menu:
    -----------------
        1. Report Data Karyawan
        2. Penambahan Data Karyawan
        3. Update Data Karyawan
        4. Delete Data Karyawan
        5. Exit

    ===============================================================
    Silahkan pilih Menu (1-5): ''')

    while True:

        if PilihMenu == '1':
            MenudataKaryawan()
        elif PilihMenu == '2':
            tambahData()
        elif PilihMenu == '3':
            updateData()
        elif PilihMenu == '4':
            deleteData()
        elif PilihMenu == '5':
            print()
            print('''
    ===============================================================
    -----------------------* TERIMA KASIH *------------------------
    ===============================================================''')
            quit()                 # keluar dari looping
        else:
            print()
            print('\t--------* Pilihan yang Anda masukkan SALAH *-------- \n\t--------* Silahkan masukkan kembali pilihan *-------')
            MenuUtama()

print(MenuUtama())
