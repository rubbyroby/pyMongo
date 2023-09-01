import pymongo

serveur="mongodb://localhost:27017/"
client=pymongo.MongoClient(serveur)
base=client["curseur2"]

Coll_compte=base["compte"]
Coll_stag=base["stagiaires"]
Coll_class=base["classe"]
Coll_mod=base["module"]


log=input("saisir votre nom utilisateur: ")
pw=input("saisir votre mot de passe: ")

filtre={"Login": log , "Password" : pw }
curseur=Coll_compte.find(filtre , {})
table=list(curseur)

if len(table)==0:
    print("Nom utilisateur ou mot de passe incorrects")
else:
    print("*********** Bienvenu : Gestion stagiaires ***********")

    choix=0
    while int(choix) != 4:
        print("1---------------Gestin de classe")
        print("2---------------Gestin de Modules")
        print("3---------------Gestin de Stagiaires")
        print("4---------------Quitter l'application")
        choix=input("saisir un choix 1 à 3, tappez : 4  pour quitter l'application ")

        if int(choix) == 1:
            choix1=0
            #------------------------Gestion des classes ---------------
            while int(choix1) != 6:
                print("1-----------------Créer une classe")
                print("2-----------------Lister les classes")
                print("3-----------------Rechercher une classe")
                print("4-----------------Modifier une classe")
                print("5-----------------Supprimer une classe")
                print("6-----------------retour au menu global")

                choix1=input("saisir un choix 1 à 5, tappez : 6  pour revenir au menu global: ")
                if int( choix1)==5:

                    #supprimer une classe
                    code=input("saisir le code dela classe à supprimer: ")
                    filtre={"code_classe" : code}
                    curseur=Coll_class.find(filtre , {})
                    table=list(curseur)
                    if len(table)==0:
                        print("Le code saisi ne correspond à aucune classe, dans la base de données")
                    else:
                        reponse=input("Veuillez confirmer la suppression!! O/N: ")
                        if reponse=="O":
                            resultat=Coll_class.delete_one(filtre)
                            if resultat.deleted_count==0:
                                print("La suppression a échoué")
                            else:
                                print("La suppression a réussi")
                        else:
                            print("Vous avez annulé la suppression")

                if int(choix1)==3:
                # ------------------------rechercher une classe------------
                    code=input(" saisir le code de la classe à rechercer: ")
                    filtre={"code_classe": code}
                    cur1 = Coll_class.find(filtre , {})
                    print("***********************************************************")
                    print("code classe \t nom classe \t effectif ")
                    print("***********************************************************")
                    for cla in cur1:
                        print(cla["code_classe"], "\t\t\t", cla["nom_classe"], "\t\t\t", cla["effectif"])
                    print("***********************************************************")


                if int(choix1)==2:
                #----------------Lister les classes-------------------
                    cur1=Coll_class.find()
                    print("***********************************************************")
                    print("code classe \t nom classe \t effectif ")
                    print("***********************************************************")
                    for x in cur1:
                        print(x["code_classe"] , "\t\t\t" , x["nom_classe"] , "\t\t\t" , x["effectif"])
                    print("***********************************************************")


                if int(choix1)==1:
                #------------------------ajouter une classe------------
                    code=input(" saisir le code de la classe à créer: ")
                    nom=input("saisir le nom de la classe: ")
                    eff=input("saisir l'effectif de la classe: ")           
                    Coll_class.insert_one({"code_classe": int(code) , "nom_classe":nom , "effectif":eff})

                if int(choix1) == 4:
                    code = input(" saisir le code de la classe à modifier")
                    filtre = {"code_classe": int(code)}
            
                    nom = input("saisir le nom de la classe: ")
                    eff = input("saisir l'effectif de la classe: ")
                    new_val={ "$set" : { "nom_classe":nom , "effectif": int(eff)}}
            
                    resultat=Coll_class.update_one(filtre , new_val)
                    if(resultat.modified_count==0):
                        print("La modification a échoué, Pensez à vérifier les données saisies")
                    else:
                        print (" La modification a réussi")
        


        if int(choix) == 2:
            choix2=0
            # ------------------------Gestion des Modules ---------------
            while int(choix2) != 6:
                print("1-----------------Créer un Module")
                print("2-----------------Lister les Modules")
                print("3-----------------Rechercher un Module")
                print("4-----------------Modifier un Module")
                print("5-----------------Supprimer un Module")
                print("6-----------------retour au menu global")

                choix2 = input("saisir un choix 1 à 5, tappez : 6  pour revenir au menu global")

                if int( choix2)==5:

                    #supprimer une module
                    code=input("saisir le code dela module à supprimer: ")
                    filtre={"Code_Module" : code}
                    curseur=Coll_mod.find(filtre , {})
                    table=list(curseur)
                    if len(table)==0:
                        print("Le code saisi ne correspond à aucune module, dans la base de données")
                    else:
                        reponse=input("Veuillez confirmer la suppression!! O/N: ")
                        if reponse=="O":
                            resultat=Coll_mod.delete_one(filtre)
                            if resultat.deleted_count==0:
                                print("La suppression a échoué")
                            else:
                                print("La suppression a réussi")
                        else:
                            print("Vous avez annulé la suppression")

                if int(choix2)==3:
                # ------------------------rechercher une module------------
                    code=input(" saisir le code de une modulz à rechercer: ")
                    filtre={"Code_Module": code}
                    cur1 = Coll_mod.find(filtre , {})
                    print("***********************************************************")
                    print("code module \t nom module \t coefficient \t nombre d'heur ")
                    print("***********************************************************")
                    for cla in cur1:
                        print(cla["Code_Module"], "\t\t\t", cla["Nom_Module"], "\t\t\t", cla["coefficient"],"\t\t\t", cla["NbrHeur"])
                    print("***********************************************************")


                if int(choix2)==2:
                #----------------Lister les modules-------------------
                    cur1=Coll_mod.find()
                    print("***********************************************************")
                    print("code module \t nom module \t coffecient \t NBRHeur ")
                    print("***********************************************************")
                    for x in cur1:
                        print(x["Code_Module"], "\t\t\t", x["Nom_Module"], "\t\t\t", x["coefficient"],"\t\t\t", x["NbrHeur"])
                    print("***********************************************************")


                if int(choix2)==1:
                #------------------------ajouter une module-----------
                    code=input(" saisir le code de la module à créer: ")
                    nom=input("saisir le nom de la module: ")
                    coff=input("saisir la coefficient de la module: ")   
                    nbr=input(" saisir le nombre d'horaire: ")        
                    Coll_mod.insert_one({"Code_Module": int(code) , "Nom_Module":nom , "coefficient":coff  , "NbrHeur":nbr})

                if int(choix2) == 4:
                    code = input(" saisir le code de la module à modifier")
                    filtre = {"Code_Module": int(code)}
            
                    nom = input("saisir le nom de la module: ")
                    coeff = input("saisir la coefficient de la module: ")
                    nbr=input(" saisir le nombre d'horaire: ")
                    new_val={ "$set" : { "Nom_Module":nom , "coefficient": int(coeff), "NbrHeur":int(nbr)}}
            
                    resultat=Coll_mod.update_one(filtre , new_val)
                    if(resultat.modified_count==0):
                        print("La modification a échoué, Pensez à vérifier les données saisies")
                    else:
                        print (" La modification a réussi")



        if int(choix) == 3:
            choix3=0
            # ------------------------Gestion des stagiaires ---------------
            while int(choix3) != 8:
                print("1-----------------Créer un Stagiaire")
                print("2-----------------Lister les stagiaires")
                print("3-----------------Rechercher un Stagiaire")#calculer sa moyenne
                print("4-----------------Modifier un Stagiaire")
                print("5-----------------Supprimer un Stagiaire")
                print("6-----------------Saisir les notes  d'un Stagiaire")
                print("7-----------------Lister les Stagiaires d'une classe donnée")
                print("8-----------------retour au menu global")

                choix3 = input("saisir un choix 1 à 5, tappez : 8  pour revenir au menu global")
    #creation des notes par $push et un tableau diff
                if int( choix2)==5:

                    #supprimer une stagiaire
                    code=input("saisir le code du stagiaire à supprimer: ")
                    filtre={"CEF" : code}
                    curseur=Coll_stag.find(filtre , {})
                    table=list(curseur)
                    if len(table)==0:
                        print("Le code saisi ne correspond à aucune stagiaire, dans la base de données")
                    else:
                        reponse=input("Veuillez confirmer la suppression!! O/N: ")
                        if reponse=="O":
                            resultat=Coll_stag.delete_one(filtre)
                            if resultat.deleted_count==0:
                                print("La suppression a échoué")
                            else:
                                print("La suppression a réussi")
                        else:
                            print("Vous avez annulé la suppression")

                if int(choix2)==3:
                # ------------------------rechercher une stagiaire------------
                    code=input(" saisir le code de stagiaire à rechercher: ")
                    filtre={"CEF": code}
                    cur1 = Coll_stag.find(filtre , {})
                    print("***********************************************************")
                    print("code stagiaire \t nom \t prénom  \t adresse \t age \t bac \t moyenne bac \t groupe \t note  ")
                    print("***********************************************************")
                    for cla in cur1:
                        print(cla["CEF"], "\t\t\t", cla["Nom"], "\t\t\t", cla["prenom"],"\t\t\t", cla["Adresse"],"\t\t\t", cla["age"],"\t\t\t", cla["Bac"],"\t\t\t", cla["MoyenneBac"],"\t\t\t", cla["groupe"],"\t\t\t", cla["Note"])
                    print("***********************************************************")
                    #POUR AFFICHER UNE NOTEEE ON UTILISE AGGREGATE
                    


                if int(choix2)==2:
                #----------------Lister les stagiaires-------------------
                    cur1=Coll_stag.find()
                    print("***********************************************************")
                    print("code stagiaire \t nom \t prénom  \t adresse \t age \t bac \t moyenne bac \t groupe \t note ")
                    print("***********************************************************")
                    for x in cur1:
                        print(x["CEF"], "\t\t\t", x["Nom"], "\t\t\t", x["prenom"],"\t\t\t", x["Adresse"],"\t\t\t", x["age"],"\t\t\t", x["Bac"],"\t\t\t", x["MoyenneBac"],"\t\t\t", x["groupe"],"\t\t\t", x["Note"])
                    print("***********************************************************")


                if int(choix2)==1:
                #------------------------ajouter une stagiaire-----------
                    code=input(" saisir le code du stagiaire à créer: ")
                    nom=input("saisir le nom du stagiaire: ")
                    pre=input("saisir le prenom de stagiaire: ")   
                    ad=input(" saisir l'adresse: ")  
                    age=input(" saisir l'age': ")  
                    bac=input(" saisir le bac: ")  
                    mb=input(" saisir lmoyenne de bac: ")  
                    grp=input(" saisir le groupe: ")  
                    note=input(" saisir la note: ")        
                    Coll_stag.insert_one({"CEF": int(code) ,"nom":nom, "prenom":pre , "Adresse":ad  , "age":age , "Bac":age, "MoyenneBac":mb, "groupe":grp , "Notes":note})
                    

                if int(choix2) == 4:
                    code = input(" saisir le code de le stagiaire à modifier")
                    filtre = {"CEF": int(code)}
            
                    nom = input("saisir le nom de stagiaire: ")
                    pre=input("saisir le prenom de stagiaire: ")   
                    ad=input(" saisir l'adresse: ")  
                    age=input(" saisir l'age': ")  
                    bac=input(" saisir le bac: ")  
                    mb=input(" saisir lmoyenne de bac: ")  
                    grp=input(" saisir le groupe: ")  
                    note=input(" saisir la note: ") 
                    new_val={ "$set" : { "nom":nom, "prenom":pre , "Adresse":ad  , "age":age , "Bac":age, "MoyenneBac":mb, "groupe":grp , "Notes":note}}
            
                    resultat=Coll_stag.update_one(filtre , new_val)
                    if(resultat.modified_count==0):
                        print("La modification a échoué, Pensez à vérifier les données saisies")
                    else:
                        print (" La modification a réussi") 