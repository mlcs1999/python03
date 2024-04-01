import sqlite3, csv

# kreiranje baze podataka
# kreira se konekcija sa bazom
# kad specificiram tip, daje mi funkcije nad ovim tipom
def kreiranje(conn: sqlite3.Connection):
    cur = conn.cursor()
    # trostrukti string - da ne pišemo sve u jednom redu; DOCSTRING
    query = """
    CREATE TABLE Studenti(
        ime VARCHAR(255) NOT NULL,
        prezime VARCHAR(255) NOT NULL,
        indeks VARCHAR(255) PRIMARY  KEY NOT NULL,
        smer VARCHAR(255) NOT NULL
    );
    """
    # izvršavanje upita
    cur.execute(query)
    # modifikacija nad bazom - mora commit
    conn.commit()
    cur.close()

    pass

# kreiranje reda u bp
# tuple - uvek u tom formatu kad prosleđujemo podatke za query
def create(conn: sqlite3.Connection, student: tuple):
    cur = conn.cursor()
    query = "INSERT INTO Studenti VALUES (?,?,?,?)"
    cur.execute(query, student)
    conn.commit()
    cur.close()
    pass

# čitanje reda u bp
def read(conn: sqlite3.Connection):
    cur = conn.cursor()
    query = "SELECT * from Studenti"
    cur.execute(query)
    studenti = cur.fetchall()
    
    # vratiće sledeći red (i to samo 1 red, vraća None ako nema dalje)
    # c.fetchone()

    # prima parametar u vidu broja (vraća broj redova kao listu, a kad ne bude više bilo redova vratiće praznu listu)
    # c.fetchmany(5)

    # vratiće sve preostale redove i staviće ih u listu, a kad ne bude više bilo redova vratiće praznu listu
    # c.fetchall()
    return studenti

    # student = cur.fetchmany(4)
    # return student

    pass

# brisanje reda u bp
def delete(conn: sqlite3.Connection, indeks: str):
    print("uso u delete")
    cur = conn.cursor()
    query = f"DELETE FROM Studenti WHERE indeks = '{indeks}'"
    cur.execute(query)
    conn.commit()
    cur.close()

# testiranje 
def test():
    # print("Izvršavanje main funkcije")
    # kad ovo pokrenemo, kreiraće se fajl studenti.db u kome ćemo da čuvamo podatke
    conn = sqlite3.connect("studenti.db")
    # kreiranje(conn)
    lista_studenata = []

    # pravi listu rečnika, a mi hoćemo tuplove
    with open("studenti.csv", mode="r", encoding="utf-8", newline="") as std_fajl:
        reader = csv.DictReader(std_fajl)
        for row in reader:
            lista_studenata.append(row)

    # i upisivanje u listu studenata 
    lista_tuplova = [tuple(student.values()) for student in lista_studenata]

    # create(conn, lista_tuplova[2])
    # print(read(conn))

    # pošto smo već upisali lista_tuplova[2], moramo da pokrenemo od 3. indeksa
    # for std in lista_tuplova[3:]:
    #     create(conn, std)
    # print(read(conn))

    # delete(conn, '2019/1122')

    print(read(conn))
    
    conn.close()

# __name__ - specifična promenljiva koja sadrži naziv trenutne py skripte
# Izraz if __name__ == '__main__': obično se koristi kako bi se omogućilo pokretanje 
# određenih delova koda samo ako se datoteka direktno izvršava, a ne ako je uvezena 
# kao modul u drugu datoteku.
# Ovo se koristi kako bi se omogućila modularnost i reusability koda u Pythonu.
    
if __name__ == '__main__':
    test()
    print(__name__)
    # odradi test.py