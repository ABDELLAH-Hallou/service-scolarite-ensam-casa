import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
from tkinter.ttk import *
from datetime import date
import sqlite3
import sys
import shutil
import io
import os
import random
import string
from tkinter.messagebox import *
import smtplib

from os import chdir, getcwd, listdir, path
def home(login, db, racine):

    # all user fields---------------------------------------------------------------------

    fields = (
        'image', 'Nom de famille', 'Prénom', 'date de naissance', 'lieu de naissance', 'téléphone', 'Code apogée',
        'Filière',
        'niveau',
        'Email académique', 'Numéro CIN', 'Adresse', 'Pays', 'Adresse email', 'Téléphone en cas d\'urgence', 'password')

    # connection with database-------------------------------------------------------------

    def connectDataBase():
        db = sqlite3.connect("scolarite.db")
        db.row_factory = sqlite3.Row
        return db

    # get bacalureat----------------------------------------------------------------------

    def send_bac(root, conn, login):
        c = conn.cursor()
        win = tk.Toplevel(root)
        win.title("Demander mon bac")
        win.geometry("400x300")
        win.configure(background="#B5F1F0")

        # style object/frames
        s = Style()
        s.configure('My.TFrame', background='#B5F1F0')

        frame0 = Frame(win, style='My.TFrame')
        frame0.pack()

        frame = Frame(win)
        frame.pack()

        frame2 = Frame(win, style='My.TFrame')
        frame2.pack()

        style = Style()
        style.configure('W.TButton', font=
        ('calibri', 11, 'bold'), foreground='blue')

        # Get the doc names--------------------------------------

        c.execute("select * from documents")
        fichier = []
        for i in c.fetchall():
            fichier.append(i[1])

        # get user id
        student_info = c.execute("select * from etudiants where email_ensam=?", (login,))
        for student in student_info:
            etudiant_id = student[-3]
        conn.commit()
        annee_universitaire = '2021/2022'
        etat = 'En cours de traitement'

        def get_id():
            if var.get() == 1:
                id = 7
            else:
                id = 8
            return id

        def envoyer():
            id = get_id()
            c.execute("select * from demandes where doc_id=?", (id,))
            Row = c.fetchall()
            c.execute("select intitule from documents where doc_id=?", (id,))
            Row2 = c.fetchall()
            try:
                if Row[0][2] == id:
                    msg = "Ce fichier est déja demandé : " + Row2[0][0]
                    messagebox.showwarning(title="Attention", message=msg)
            except:
                c.execute(
                    "INSERT INTO demandes(etudiant_id,doc_id,annee_universitaire,etat,date,bac_id) values(?,?,?,?,?,?)",
                    (etudiant_id, id, annee_universitaire, etat, date.today(), "bac-" + etudiant_id))
                messagebox.showinfo(title="Succès", message='Demande bien envoyé')
                conn.commit()

        # the window
        text_label = Label(frame0, text='Veuillez selectionner le type de demande de bac : ', font=("Roboto", 12))
        text_label.grid(column=0, row=0, sticky='W', pady=25)
        text_label.config(background="#B5F1F0")

        # the doc names part
        var = tk.IntVar()
        chk_btn = Radiobutton(frame, text=fichier[6], variable=var, value='1')
        chk_btn.grid(column=0, row=1, sticky=tk.W, pady=10, padx=50)

        chk_btn = Radiobutton(frame, text=fichier[7], variable=var, value='2')
        chk_btn.grid(column=0, row=2, sticky=tk.W, pady=10, padx=50)

        # the buttons part
        btn_quiter = Button(frame2, text='Quiter', command=win.destroy, width=15, style='W.TButton')
        btn_quiter.grid(column=0, row=1, padx=10, pady=30)
        btn_send = Button(frame2, text='Envoyer', command=envoyer, width=15, style='W.TButton')
        btn_send.grid(column=1, row=1, padx=10, pady=30)
        win.mainloop()

    def send_com(root, conn, login):

        c = conn.cursor()
        win = tk.Toplevel(root)
        win.title("Demander un fichier")

        win.geometry("400x400")
        win.configure(background="#B5F1F0")

        # style object/frames
        s = Style()
        s.configure('My.TFrame', background='#B5F1F0')

        frame0 = Frame(win, style='My.TFrame')
        frame0.pack()

        frame = Frame(win)
        frame.pack()

        frame2 = Frame(win, style='My.TFrame')
        frame2.pack()

        style = Style()
        style.configure('W.TButton', font=
        ('calibri', 11, 'bold'), foreground='blue')

        # Get the doc names
        c.execute("select * from documents")
        fichier = []
        for i in c.fetchall():
            fichier.append(i[1])

        # get user id
        student_info = c.execute("select * from etudiants where email_ensam=?",(login,))
        for student in student_info:
            etudiant_id = student[-3]
        conn.commit()
        annee_universitaire = '2021/2022'
        etat = 'En cours de traitement'

        def envoyer():
            var = {"1": var1.get(), "2": var2.get(), "3": var3.get(), "4": var4.get(), "5": var5.get(), "6": var6.get()}
            for key, value in var.items():
                if value == 1:
                    c.execute("select * from demandes where doc_id=?", (int(key),))
                    Row = c.fetchall()
                    c.execute("select intitule from documents where doc_id=?", (int(key),))
                    Row2 = c.fetchall()
                    try:
                        if Row[0][2] == int(key):
                            msg = "Ce fichier est déja demandé : " + Row2[0][0]
                            messagebox.showwarning(title="Attention", message=msg)
                    except:
                        c.execute("INSERT INTO demandes(etudiant_id,doc_id,annee_universitaire,etat,date) values(?,?,?,?,?)",
                                  (etudiant_id, int(key), annee_universitaire, etat, date.today()))
                        messagebox.showinfo(title="Succès", message='Demande bien envoyé')
                        conn.commit()


        # the window
        text_label = Label(frame0, text='Veuillez selectionner les fichiers à demander :', font=("Roboto", 12))
        text_label.grid(column=0, row=0, sticky='W', pady=25)
        text_label.config(background="#B5F1F0")

        # the doc names part
        var1 = tk.IntVar()
        chk_btn = Checkbutton(frame, text=fichier[0], variable=var1)
        chk_btn.grid(column=0, row=1, sticky=tk.W, pady=10, padx=50)

        var2 = tk.IntVar()
        chk_btn = Checkbutton(frame, text=fichier[1], variable=var2)
        chk_btn.grid(column=0, row=2, sticky=tk.W, pady=10, padx=50)

        var3 = tk.IntVar()
        chk_btn = Checkbutton(frame, text=fichier[2], variable=var3)
        chk_btn.grid(column=0, row=3, sticky=tk.W, pady=10, padx=50)

        var4 = tk.IntVar()
        chk_btn = Checkbutton(frame, text=fichier[3], variable=var4)
        chk_btn.grid(column=0, row=4, sticky=tk.W, pady=10, padx=50)

        var5 = tk.IntVar()
        chk_btn = Checkbutton(frame, text=fichier[4], variable=var5)
        chk_btn.grid(column=0, row=5, sticky=tk.W, pady=10, padx=50)

        var6 = tk.IntVar()
        chk_btn = Checkbutton(frame, text=fichier[5], variable=var6)
        chk_btn.grid(column=0, row=6, sticky=tk.W, pady=10, padx=50)

        # the buttons part
        btn_quiter = Button(frame2, text='Quiter', command=win.destroy, width=15, style='W.TButton')
        btn_quiter.grid(column=0, row=1, padx=10, pady=30)
        btn_send = Button(frame2, text='Envoyer', command=envoyer, width=15, style='W.TButton')
        btn_send.grid(column=1, row=1, padx=10, pady=30)
        win.mainloop()

    # update user informations-------------------------------------------------------------

    def put(info_win, entries, db):

        # getting entries values -------------------------------------------------------

        image = (entries['image'].get())
        prenom = (entries['Prénom'].get())
        nom = (entries['Nom de famille'].get())
        dateDeNaissance = (entries['date de naissance'].get())
        lieuDeNaissance = (entries['lieu de naissance'].get())
        tele = (entries['téléphone'].get())
        codeApogee = (entries['Code apogée'].get())
        filiere = (entries['Filière'].get())
        niveau = (entries['niveau'].get())
        email_aca = (entries['Email académique'].get())
        CIN = (entries['Numéro CIN'].get())
        adresse = (entries['Adresse'].get())
        pays = (entries['Pays'].get())
        email_perso = (entries['Adresse email'].get())
        tele_urgencee = (entries['Téléphone en cas d\'urgence'].get())
        password = (entries['password'].get())

        # update request-------------------------------------------------------------------

        db.execute(
            "update etudiants set nom = ?, prenom = ?, image = ?, date_naissance = ?, lieu_naissance = ?, telephone = ?, adresse = ?, pays = ?, email_perso = ?, tele_urgence = ?, password = ? where email_ensam = ?",
            (
                nom, prenom, image, dateDeNaissance, lieuDeNaissance, tele, adresse, pays, email_perso, tele_urgencee,
                password,
                email_aca))
        db.commit()

        # message de succes-----------------------------------------------------------------

        messagebox.showinfo(title="Succès", message='Vos informations sont à jour')

        # close window-----------------------------------------------------------------

        info_win.destroy()

    # get user informations ------------------------------------------------------------

    def get(login, db):

        # get request ------------------------------------------------------------

        student_info = db.execute("select * from etudiants where email_ensam=?", (login,))

        # create list that contains all user informations and return it-----------------------------------

        list = {}
        for student in student_info:
            list['CIN'] = student['CIN']
            list['nom'] = student['nom']
            list['email_ensam'] = student['email_ensam']
            list['prenom'] = student['prenom']
            list['filiere'] = student['filiere']
            list['image'] = student['image']
            list['date_naissance'] = student['date_naissance']
            list['lieu_naissance'] = student['lieu_naissance']
            list['telephone'] = student['telephone']
            list['adresse'] = student['adresse']
            list['pays'] = student['pays']
            list['email_perso'] = student['email_perso']
            list['tele_urgence'] = student['tele_urgence']
            list['niveau'] = student['niveau']
            list['code_apogee'] = student['code_apogee']
            list['password'] = student['password']

        return list

    # function to put user informations inside the entries------------------------------------

    def studentinfo(login, entries, db):

        # call the get user infos function----------------------------------------------------

        student = get(login, db)

        # insert values into entries---------------------------------------------------------

        entries['image'].insert(0, student['image'])
        entries['Nom de famille'].insert(0, student['nom'])
        entries['Prénom'].insert(0, student['prenom'])
        entries['date de naissance'].insert(0, student['date_naissance'])
        entries['lieu de naissance'].insert(0, student['lieu_naissance'])
        entries['téléphone'].insert(0, student['telephone'])
        entries['Code apogée'].insert(0, student['code_apogee'])
        entries['Code apogée'].config(state='disabled')
        entries['Filière'].insert(0, student['filiere'])
        entries['niveau'].insert(0, student['niveau'])
        entries['Email académique'].insert(0, student['email_ensam'])
        entries['Numéro CIN'].insert(0, student['CIN'])
        entries['Adresse'].insert(0, student['adresse'])
        entries['Pays'].insert(0, student['pays'])
        entries['Adresse email'].insert(0, student['email_perso'])
        entries['Téléphone en cas d\'urgence'].insert(0, student['tele_urgence'])
        entries['password'].insert(0, student['password'])

        # desactivate academic entries -------------------------------------

        entries['Filière'].config(state='disabled')
        entries['niveau'].config(state='disabled')
        entries['Email académique'].config(state='disabled')
        entries['Numéro CIN'].config(state='disabled')

        # make password invisible -------------------------------------

        entries['password'].config(show='*')

    # function remove a text from an entry-----------------------------------------

    def clear_text(text):
        text.delete(0, 255)

    # function to upload personal photo of users ------------------------------------

    def upload(root, ent):

        # select an image from the computer---------------------------------------

        root.filename = filedialog.askopenfilename(title="Select An Image")

        # make sure that the file name is not empty

        if root.filename == '':
            pass
        else:

            # make sure that the file is already exists

            if path.exists('./media/' + root.filename.split("/")[-1]):
                clear_text(ent['image'])
                ent['image'].insert(0, root.filename.split("/")[-1])
            else:

                # if the file is not exist in media then the following instruction will copy it and past it in media---------

                ImagePath = shutil.copy(root.filename, './media')

                # update the path of the personal photo---------------------------------------------------------

                clear_text(ent['image'])

                # get just the name of the file and not the all path--------------------------------------------

                ent['image'].insert(0, root.filename.split("/")[-1])

    # two function in order to show or hide the password---------------------------------------------------

    def show(entries):
        entries['password'].config(show="")

    def hidep(entries):
        entries['password'].config(show="*")

    # create all entries for user information --------------------------------------

    def makeform(root, login, fields, bg, db):

        # dict of entries-----------------------------------------------------------

        entries = {}

        # loop to create all entries depending on fields---------------------------

        for field in fields:

            # define a frame to orgnaze the design---------------------------------

            row = tk.Frame(root)

            lab = tk.Label(row,
                           bd=4,
                           width=22,
                           text=field + " : ",
                           anchor='w',
                           bg=bg)

            # button style--------------------------------------------------------

            style = Style()
            style.configure('W.TButton', font=('calibri', 10, 'bold'), foreground='blue')

            # upload image button----------------------------------------------------------------------------
            bt = Button(row, width=2, text='>', style='W.TButton', command=lambda: upload(root, entries),
                        cursor="hand2")
            # show password button----------------------------------------------------------------------------
            shw = Button(row, width=2, text='(o)', style='W.TButton', command=lambda: show(entries), cursor="hand2")
            # hide password button----------------------------------------------------------------------------
            hide = Button(row, width=2, text='(x)', style='W.TButton', command=lambda: hidep(entries),
                          cursor="hand2")

            # specific design for the frame that contains image field----------------------------

            if field == 'image':
                ent = tk.Entry(row,
                               bd=2,
                               font='Helvetica',
                               relief='flat',
                               width=28)

                bt.pack(side=tk.RIGHT,
                        expand=tk.YES)

            elif field == 'password':
                # specific design for the frame that contains password field----------------------------
                ent = tk.Entry(row,
                               bd=2,
                               font='Helvetica',
                               relief='flat',
                               width=25)

                hide.pack(side=tk.RIGHT,
                          expand=tk.YES)
                shw.pack(side=tk.RIGHT,
                         expand=tk.YES)
            else:
                # the design for the frame that contain the rest of the fields----------------------------
                ent = tk.Entry(row,
                               bd=2,
                               font='Helvetica',
                               relief='flat',
                               width=30)

            row.pack(side=tk.TOP,
                     fill=tk.Y,
                     padx=5,
                     pady=5)

            lab.pack(side=tk.LEFT)

            ent.pack(side=tk.RIGHT,
                     expand=tk.YES)

            # put the entries into the entries dict------------------------------------------

            entries[field] = ent

        # call the function that fill all the entries with users infos------------------------

        studentinfo(login, entries, db)

        return entries

    # window that contains all the user infos--------------------------------------------

    def infoWin(root, login, bg, db):

        # create the window(child)--------------------------------------------------------------
        info_win = tk.Toplevel(root)
        # window configurations--------------------------------------------------------------------
        info_win.title("Les informations personels")
        info_win.configure(bg=bg)

        # getting the entries----------------------------------------------------------------------
        ents = makeform(info_win, login, fields, bg, db)

        # button style--------------------------------------------------------
        style = Style()
        style.configure('W.TButton', font=('calibri', 10, 'bold'), foreground='blue')

        # buttons--------------------------------------------------------------------------------
        submit = Button(info_win, text='Envoyer', style='W.TButton', command=lambda: put(info_win, ents, db),
                        cursor="hand2")
        submit.pack(side=tk.RIGHT, padx=5, pady=5)
        cancel = Button(info_win, text='Quiter', style='W.TButton', command=lambda: info_win.destroy(), cursor="hand2")
        cancel.pack(side=tk.RIGHT, padx=5, pady=5)

    # la fonction qui fait la gestion des bottons pour la fenetre des emplois------------------------------------

    def which_button(emploi_win, name):
        # getting the image of a certain major--------------------------------------------------------------------
        img = Image.open("./emploi/" + name + ".png")
        # image config ------------------------------------------------------------------------------------------
        img = img.resize((800, 500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        # place it on the window --------------------------------------------------------------------------------
        imgt = tk.Label(emploi_win, image=img, bg=bg)
        imgt.place(x=10, y=40)

        emploi_win.mainloop()

    # creation de la fenetre des emplois-------------------------------------------------------------------------

    def emploif(root, bg):

        # craete window (child)----------------------------------------------------------------------------------
        emploi_win = tk.Toplevel(root)
        # window config----------------------------------------------------------------------------------
        emploi_win.title("Les emploi de temps")
        emploi_win.configure(bg=bg)
        emploi_win.geometry("824x600")

        # buttons API---------------------------------------------------------------------------------------
        API1 = tk.Button(emploi_win, width=5, text='API1', command=lambda m="MSEI1": which_button(emploi_win, m),
                         cursor="hand2")
        API1.place(x=0, y=0)
        API2 = tk.Button(emploi_win, width=5, text='API2', command=lambda m="GM1": which_button(emploi_win, m),
                         cursor="hand2")
        API2.place(x=45, y=0)

        # buttons CI1---------------------------------------------------------------------------------------
        GI1 = tk.Button(emploi_win, width=5, text='GI1', command=lambda m="GI1": which_button(emploi_win, m),
                        cursor="hand2")
        GI1.place(x=90, y=0)
        GE1 = tk.Button(emploi_win, width=5, text='GE1', command=lambda m="GE1": which_button(emploi_win, m),
                        cursor="hand2")
        GE1.place(x=135, y=0)
        GM1 = tk.Button(emploi_win, width=5, text='GM1', command=lambda m="GM1": which_button(emploi_win, m),
                        cursor="hand2")
        GM1.place(x=180, y=0)
        MSEI1 = tk.Button(emploi_win, width=5, text='MSEI1', command=lambda m="MSEI1": which_button(emploi_win, m),
                          cursor="hand2")
        MSEI1.place(x=225, y=0)
        IAGI1 = tk.Button(emploi_win, width=5, text='IAGI1', command=lambda m="IAGI1": which_button(emploi_win, m),
                          cursor="hand2")
        IAGI1.place(x=270, y=0)

        # buttons CI2---------------------------------------------------------------------------------------
        GI2 = tk.Button(emploi_win, width=5, text='GI2', command=lambda m="GI1": which_button(emploi_win, m),
                        cursor="hand2")
        GI2.place(x=315, y=0)
        GE2 = tk.Button(emploi_win, width=5, text='GE2', command=lambda m="GE1": which_button(emploi_win, m),
                        cursor="hand2")
        GE2.place(x=360, y=0)
        GM2 = tk.Button(emploi_win, width=5, text='GM2', command=lambda m="GM1": which_button(emploi_win, m),
                        cursor="hand2")
        GM2.place(x=405, y=0)
        MSEI2 = tk.Button(emploi_win, width=5, text='MSEI2', command=lambda m="MSEI1": which_button(emploi_win, m),
                          cursor="hand2")
        MSEI2.place(x=450, y=0)
        IAGI2 = tk.Button(emploi_win, width=5, text='IAGI2', command=lambda m="IAGI1": which_button(emploi_win, m),
                          cursor="hand2")
        IAGI2.place(x=495, y=0)

        # buttons CI3---------------------------------------------------------------------------------------
        GI3 = tk.Button(emploi_win, width=5, text='GI3', command=lambda m="GI1": which_button(emploi_win, m),
                        cursor="hand2")
        GI3.place(x=540, y=0)
        GE3 = tk.Button(emploi_win, width=5, text='GE3', command=lambda m="GE1": which_button(emploi_win, m),
                        cursor="hand2")
        GE3.place(x=585, y=0)
        GM3 = tk.Button(emploi_win, width=5, text='GM3', command=lambda m="GM1": which_button(emploi_win, m),
                        cursor="hand2")
        GM3.place(x=630, y=0)
        MSEI3 = tk.Button(emploi_win, width=5, text='MSEI3', command=lambda m="MSEI1": which_button(emploi_win, m),
                          cursor="hand2")
        MSEI3.place(x=675, y=0)
        IAGI3 = tk.Button(emploi_win, width=5, text='IAGI3', command=lambda m="IAGI1": which_button(emploi_win, m),
                          cursor="hand2")
        IAGI3.place(x=720, y=0)

        # button style-----------------------------------------------------------------------------------
        style = Style()
        style.configure('W.TButton', font=('calibri', 11, 'bold'), foreground='red')

        # exit button------------------------------------------------------------------------------------
        quitter = Button(emploi_win, width=7, text='quitter', style='W.TButton', command=emploi_win.destroy,
                         cursor="hand2")
        quitter.place(x=765, y=0)

    # connecting to database----------------------------------------------------------------------

    db = connectDataBase()

    # close the login window-----------------------------------------------------------------------
    racine.destroy()

    # create home window--------------------------------------------------------------------------
    root = tk.Tk()
    # window configuration--------------------------------------------------------------------------
    left1 = int((root.winfo_screenwidth() - 500) / 2)
    top1 = int((root.winfo_screenheight() - 450) / 2)
    root.geometry(f"420x500+{left1}+{top1}")
    root.title("Service Scolarité")
    bg = '#B5F1F0'
    root.configure(bg=bg)

    # getting user informations-------------------------------------------------------------------
    infos = get(login, db)

    # get the personal image------------------------------------------------------------------------------
    try:
        pic = Image.open("media/"+infos['image'])
        pic = pic.resize((100, 140), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(pic)
        pict = tk.Label(image=pic, bg=bg)
        pict.place(x=70, y=20)
    except IOError:
        pass

    # icons (personal informations)-----------------------------------------------------
    imginfoperso = Image.open("images/personalinfo.png")
    imginfoperso = imginfoperso.resize((70, 70), Image.ANTIALIAS)
    imginfoperso = ImageTk.PhotoImage(imginfoperso)

    # icons (demande something)-----------------------------------------------------
    imgdemande = Image.open('images/demande.png')
    imgdemande = imgdemande.resize((70, 70), Image.ANTIALIAS)
    imgdemande = ImageTk.PhotoImage(imgdemande)

    # icons (get bac)-----------------------------------------------------
    imgbac = Image.open('images/bac.png')
    imgbac = imgbac.resize((70, 70), Image.ANTIALIAS)
    imgbac = ImageTk.PhotoImage(imgbac)

    # icons (emploi)-----------------------------------------------------
    imgempl = Image.open('images/emploi.png')
    imgempl = imgempl.resize((70, 70), Image.ANTIALIAS)
    imgempl = ImageTk.PhotoImage(imgempl)

    # buttons inocs-----------------------------------------------------
    infoperso = tk.Button(root, image=imginfoperso, bg=bg, command=lambda: infoWin(root, login, bg, db), borderwidth=0,cursor="hand2")
    infoperso.place(x=70, y=200)
    demande = tk.Button(root, image=imgdemande, bg=bg, command=lambda:send_com(root, db, login), borderwidth=0, cursor="hand2")
    demande.place(x=260, y=200)
    bac = tk.Button(root, image=imgbac, bg=bg, command=lambda: send_bac(root, db, login), borderwidth=0, cursor="hand2")
    bac.place(x=70, y=350)
    emploi = tk.Button(root, image=imgempl, bg=bg, command=lambda: emploif(root, bg), borderwidth=0, cursor="hand2")
    emploi.place(x=260, y=350)

    # personal infos ----------------------------------------------------------------------------------------------
    full_name_label = tk.Label(root, text=infos['nom'] + ' ' + infos['prenom'], bg=bg, width=20, font=100)
    full_name_label.place(x=200, y=30)

    major_label = tk.Label(root, text=infos['filiere'], bg=bg, width=20, font=100)
    major_label.place(x=200, y=60)

    code_apogee_label = tk.Label(root, text=infos['code_apogee'], bg=bg, width=20, font=100)
    code_apogee_label.place(x=200, y=90)
    cin_label = tk.Label(root, text=infos['CIN'], bg=bg, width=20, font=100)
    cin_label.place(x=200, y=120)

    personal_info_label = tk.Label(root, text="les information personnel", bg=bg)
    personal_info_label.place(x=40, y=280)

    # text label under the button-------------------------------------------------------------------------
    demande_label = tk.Label(root, text="demande une certificats/\nattestation ...", bg=bg)
    demande_label.place(x=230, y=280)

    bacalureat_label = tk.Label(root, text="demande de bac", bg=bg)
    bacalureat_label.place(x=60, y=430)

    emploi_label = tk.Label(root, text="les emplois de temps", bg=bg)
    emploi_label.place(x=240, y=430)

    root.mainloop()



#-----------------------------------------------------------------------------------------------------------------------

def check_in(wind):


    db = sqlite3.connect('scolarite.db')
    sql="select email_ensam,password from etudiants where email_ensam='"+str(user.get())+"'"
    a=list(db.execute(sql))
    if(len(a)!=0):
        if (a[0][0] == user.get() and a[0][1] == password.get()):
            home(user.get(),db,wind)

        else:
            showerror("Erreur", "mots de passe incorrect")
    else:
        showerror("Erreur", "mots de passe ou email incorrect")

#------------------------------activation_compte_window-----------------------------------------------------------------


def activate_account():
    def get_mail(mail):
        db = sqlite3.connect('scolarite.db')
        sql = "select email_ensam,password from etudiants where email_ensam='" + str(mail) + "'"
        a = list(db.execute(sql))

        if (len(a) != 0):
            if (a[0][0] == mail and a[0][1] == None):
                passwd = nbr = ''
                for i in range(4):
                    passwd += random.choice(string.ascii_uppercase)
                    nbr += str(random.randrange(1, 9))
                passwd += nbr
                db.execute("update etudiants set password='" + passwd + "' where email_ensam='" +mail+ "'")
                db.commit()

                #----------

                sender_email = "service.scolaire.ensam@gmail.com"
                password = 'IAGI2024' #make sure you put your email password here !!!!
                message = f"Bonjour cher etudiant, \n\nutilisez ce code : \t{passwd} \tpour activer votre compte "
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                # server.sendmail(sender_email, rec_email, message.encode('utf-8'))
                subject = "Activation du Compte "
                fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n{}'
                server.sendmail(sender_email, mail, fmt.format(sender_email, mail, subject, message))
                showinfo("Information","Votre mots de passe a été envoyer à vos email.\nvous pouvez consulté l'application maintenent")
                window1.destroy()

            else:
                showwarning("Information", "Vous avez déja un compte ")
                window1.destroy()
        else:
            showerror("Erreur", "E-mail incorrect")
            window1.destroy()


    window1 = tk.Toplevel(window)
    left1 = int((window1.winfo_screenwidth() - 500) / 2)
    top1 = int((window1.winfo_screenheight() - 250) / 2)
    window1.geometry(f"500x200+{left1}+{top1}")
    window1.title('Activation du compte')

    l1 = tk.Label(window1, text="Bienvenue chez nous ", fg='black')
    l1.place(x=180, y=10)

    l2 = tk.Label(window1, text="pour activer votre compte entrer E-mail institutionnel :", fg='black')
    l2.place(x=100, y=50)

    label_3 = tk.Label(window1, text="E-mail institutionnel : ")
    label_3.place(x=50, y=100)
    mail = tk.StringVar()
    mail_institu = tk.Entry(window1, width=30, textvariable=mail)
    mail_institu.focus_set()
    mail_institu.place(x=190, y=100)

    btn_env = tk.Button(window1, text="Envoyer", command=lambda :get_mail(mail.get()), width=10)
    btn_env.place(x=220, y=140)
    window1.mainloop()


#------------------------------/activation_compte_window----------------------------------------------------------------


#--------------------------------------------Login----------------------------------------------------------------------
window=tk.Tk()
left=int( (window.winfo_screenwidth()-500) / 2)
top=int( (window.winfo_screenheight()-600) / 2)
window.geometry(f"500x500+{left}+{top}")
#window.configure(background='black')
window.title('Services de Scolarité')



#--------------------------------------Image----------------------------------------------------
img_src=Image.open("images/ensam.png")
resize=img_src.resize((280,90),Image.ANTIALIAS)
new_img=ImageTk.PhotoImage(resize)

img_=Label(window,image=new_img)
img_.place(x=100 , y=45)




#--------------------------------------Login----------------------------------------------------
label_2=Label(window,text="E-mail : ")
label_2.place(x=80 , y=170)

user=tk.StringVar()
u=Entry(window, textvariable=user , width=35)
u.focus_set()
u.place(x=180 , y=170)


#--------------------------------------Password----------------------------------------------------
label_3=Label(window,text="Mots de passe : ")
label_3.place(x=80 , y=200)

password=tk.StringVar()

ps=Entry(window, textvariable=password ,show="*",width=35)
ps.focus_set()
ps.place(x=180 , y=200)
from tkinter.ttk import *
#--------------------------------------forget password----------------------------------------------------
forget_password = tk.Label(window, text="mots de passe oublié ?",font=('Helveticabold', 8), fg="blue" , cursor="hand2")
forget_password.place(x=185 , y=225)
forget_password.bind("<Button-1>")

#--------------------------------------button send----------------------------------------------------
btn=Button(window,text="Login" ,command=lambda :check_in(window),width=13 )
btn.place(x=240 , y=250)



#--------------------------------------activate account----------------------------------------------------

btn2=tk.Button(window,text="Activé mon compte" ,command=activate_account ,width=24 , bg='green' )
btn2.place(x=195 , y=290)


window.mainloop()
#--------------------------------------------/Login----------------------------------------------------------------------

