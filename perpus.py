from datetime import date, datetime, timedelta
import mysql.connector

print("======[ APLIKASI DATABASE PERPUSTAKAAN ]======\n")
usr = input("masukkan user: ")
pw = input("masukkan password: ")
cnx = mysql.connector.connect(user=usr, passwd=pw, database='perpustakaan')
if cnx.is_connected():
    print("\n<<<<< Berhasil terhubung ke database >>>>>")
cursor = cnx.cursor()
menu = '0'
def show_tables():
    cursor.execute("show tables")
    for (table_name,) in cursor:
        print("- "+table_name)
    print("---------------------------------------------")
    
while menu == '0':
    print("\n===================[ MENU ]===================")
    print("1. Select\n2. Insert\n3. Update\n4. Delete\n0. Menu\nq. Keluar")
    print("---------------------------------------------")
    menu = input("> Input: ").upper()
    while menu == '1' or menu == 'SELECT':
        print("\n==================[ SELECT ]==================")
        show_tables()
        tabel = input("> Masukkan nama tabel: ")
        if tabel != '0':
            query = ("select * from "+tabel)
            cursor.execute(query)
            print("\n===============[ Tabel "+tabel+" ]===============")
            print(cursor.column_names)
            print("---------------------------------------------")
            results = cursor.fetchall()
            for data in results:
                print(data)
        else:
            menu = '0'
            print("\n<<<<< Keluar dari menu view >>>>>")
    while menu == '2' or menu == 'INSERT':
        print("\n==================[ INSERT ]==================")
        show_tables()
        tabel = input("> Masukkan nama tabel: ")
        if tabel != '0':
            query = ("select * from "+tabel)
            cursor.execute(query)
            cursor.fetchall()
            cn = cursor.column_names
            v = "%s,"*len(cn)
            l = ['']*len(cn)
            for i in range(len(cn)):
                l[i] = input(cn[i]+": ")
            isrt = ("insert into "+tabel+" values ("+v[:-1]+")")
            isrt2 = tuple(l)
            cursor.execute(isrt, isrt2)
            cnx.commit()
            print("\n<<<<< Data berhasil ditambahkan >>>>>")
        else:
            menu = '0'
            print("\n<<<<< Keluar dari menu insert >>>>>")
    while menu == '3' or menu == 'UPDATE':
        print("\n==================[ UPDATE ]==================")
        show_tables()
        tabel = input("> Masukkan nama tabel: ")
        if tabel != '0':
            query = ("select * from "+tabel)
            cursor.execute(query)
            cursor.fetchall()
            cn = cursor.column_names
            s = ""
            l = ['']*(len(cn))
            l[-1] = input(cn[0]+": ")
            for i in range(len(cn)-1):
                l[i] = input(cn[i+1]+": ")
                s = s+cn[i+1]+"=%s,"
            updt = ("update "+tabel+" set "+s[:-1]+" where "+cn[0]+"=%s")
            updt2 = tuple(l)
            cursor.execute(updt, updt2)
            cnx.commit()
            print("\n<<<<< Data berhasil diperbarui >>>>>")
        else:
            menu = '0'
            print("\n<<<<< Keluar dari menu update >>>>>")
    while menu == '4' or menu == 'DELETE':
        print("\n==================[ DELETE ]==================")
        show_tables()
        tabel = input("> Masukkan nama tabel: ")
        if tabel != '0':
            query = ("select * from "+tabel)
            cursor.execute(query)
            cursor.fetchall()
            cn = cursor.column_names
            dlt = ("delete from "+tabel+" where "+cn[0]+"=%s")
            dlt2 = tuple([input(cn[0]+": ")])
            cursor.execute(dlt, dlt2)
            cnx.commit()
            print("\n<<<<< Data berhasil dihapus >>>>>")
        else:
            menu = '0'
            print("\n<<<<< Keluar dari menu delete >>>>>")
    if menu == 'Q' or menu == 'KELUAR':
        break
    elif menu != '0':
        menu = '0'
cursor.close()
cnx.close()


