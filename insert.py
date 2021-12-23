import sqlite3
from datetime import date

conn = sqlite3.connect('scolarite.db')
c = conn.cursor()

# insert users

c.execute(
    "insert into etudiants(CIN, nom, email_ensam, prenom, filiere, image, date_naissance, lieu_naissance, telephone, adresse, pays, email_perso, tele_urgence, niveau, code_apogee) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
    ("AB1234", "SMITH", "userloging@ensam-casa.ma", "JOHN", "IAGI", "john.png", "12-12-2000",
     "CASABLANCA", "0612345678", "CASABLANCA", "Maroc", "john3333@gmail.com", "0687654321", "CI1",
     "12232334"))



# insert a doc type

c.execute("""
INSERT INTO documents (intitule) VALUES ("Attestation d'inscription")
""")
c.execute("""
INSERT INTO documents (intitule) VALUES ('Certificat de scolarité')
""")
c.execute("""
INSERT INTO documents (intitule) VALUES ('Mon baccalauréat')
""")
c.execute("""
INSERT INTO documents (intitule) VALUES ('Relevé de notes')
""")
c.execute("""
INSERT INTO documents (intitule) VALUES ("Ma carte d'étudiant")
""")
c.execute("""
INSERT INTO documents (intitule) VALUES ('Attestation de réussite')
""")
c.execute("""
INSERT INTO documents (intitule) VALUES ("Bac provisoire")
""")
c.execute("""
INSERT INTO documents (intitule) VALUES ("Bac permanent")
""")
conn.commit()


