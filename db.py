import sqlite3

conn = sqlite3.connect('scolarite.db')
c = conn.cursor()

# Table: bacalureat
c.execute("""
CREATE TABLE IF NOT EXISTS bacalureat (
    bac_id int(50) NOT NULL,
    type varchar(255) NOT NULL,
    CONSTRAINT bacalureat_pk PRIMARY KEY(bac_id)
)
""")
# Table: demandes

c.execute("""
CREATE TABLE IF NOT EXISTS demandes (
    demande_id INTEGER PRIMARY KEY AUTOINCREMENT,
    etudiant_id varchar(8) NOT NULL,
    doc_id INTEGER,
    annee_universitaire varchar(9) NOT NULL,
    etat varchar(255) NOT NULL,
    date datetime NOT NULL,
    bac_id varchar(50),
    CONSTRAINT demandes_documents FOREIGN KEY (doc_id) REFERENCES documents (doc_id),
    CONSTRAINT etudiants_demandes FOREIGN KEY (etudiant_id) REFERENCES etudiants (CIN)
    ON DELETE CASCADE 
    ON UPDATE CASCADE,
    CONSTRAINT demandes_bacalureat FOREIGN KEY (bac_id) REFERENCES bacalureat (bac_id)
)
""")

# -- Table: documents

c.execute("""
CREATE TABLE IF NOT EXISTS documents (
    doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    intitule varchar(255) NOT NULL
)
""")
# -- Table: etudiants

c.execute("""
CREATE TABLE IF NOT EXISTS etudiants (
    CIN varchar(10) NOT NULL,
    nom varchar(100) NOT NULL,
    prenom varchar(100) NOT NULL,
    email_ensam varchar(255) NOT NULL,
    niveau varchar(10) NOT NULL,
    filiere varchar(255) NOT NULL,
    date_naissance date NOT NULL,
    lieu_naissance varchar(255) NOT NULL,
    telephone varchar(10),
    adresse varchar(255) NOT NULL,
    pays varchar(50) NOT NULL,
    email_perso varchar(255),
    tele_urgence varchar(10) NOT NULL,
    code_apogee varchar(8) NOT NULL,
    image text,
    password varchar(35),
    CONSTRAINT etudiants_pk PRIMARY KEY (CIN)
)
""")


conn.commit()


