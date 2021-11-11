#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np
import pandas as pd


# # On définit l'alphabet et la taille maximale d'un mot

# In[2]:


alphabet = "abcdefghijklmnopqrstuvwxyzàâéèêëîïôùûüÿæœç-"
taillemax = 30


# # Fonctionnalité 1 : mot aléatoire sans logique

# #### La fonction creeMotAleatoire permet à partir d'une taille donnée, de créer un mot sans aucune logique en rassemblant des lettres générées aléatoirement de l'alphabet

# In[3]:


def creeMotAleatoire(taille):
    global alphabet
    res = ""
    for i in range(taille):
        res += random.choice(alphabet)
    return res


# ##### voici un exemple de mot sans logique, généré aléatoirement

# In[4]:


f1_mot = creeMotAleatoire(5)
print(f1_mot)


# # Fonctionnalité 2 : Création de mot avec la méthode des Digrammes

# ### A) Definition des fonctions motDigramme, normaliserDigramme et creerDigramme

# #### La fonction motDigramme permet de remplir le dataframe à partir d'un mot donné ( sans normalisation )

# In[5]:


def motDigramme(mot,dataframe):
    mot = mot.lower() # met le mot entierement en minuscule
    lmot = list(mot) # on convertit le mot en liste de chacun de ses caracteres
    lmot = list(set(lmot)) # permet de supprimer les doublons de la liste 
    dataframe[mot[0]]['debut']+=1
    dataframe['fin'][mot[-1:]]+=1
    for i in lmot :
        for j in range(len(mot)-1) :
            if i==mot[j]:
                dataframe[mot[j+1]][i] += 1


# #### La fonction normaliserDigramme permet de normaliser le dataframe, c'est à dire :
# - On considère une ligne du dataframe
# - On somme tous les coefficients de la ligne 
# - On divise tous les coefficients de la ligne par le total calculé précédemment
# - On procède de la même même manière pour chaque ligne

# In[6]:


def normaliserDigramme(dataframe):
    indexs = dataframe.index.values.tolist() 
    for indexrow in indexs:
        somme = dataframe.loc[indexrow].sum() 
        if somme != 0:
            dataframe.loc[indexrow]/= somme


# #### > Il s'agit de la fonction finale, cette fonction permet de créer un digramme normalisé à partir d'un alphabet et d'un dictionnaire de mot ( liste de mots composés exclusivement de lettre de l'alphabet ) <

# In[7]:


def creerDigramme(dic):
    global alphabet
    lettres = list(alphabet)
    tableau = np.zeros((len(alphabet)+1,len(alphabet)+1))
    dataframe = pd.DataFrame(tableau, index = (["debut"] + lettres), columns = (lettres + ["fin"]))
    for mot in dic :
        motDigramme(mot,dataframe)
    normaliserDigramme(dataframe)
    return(dataframe) # on retourne le digramme fini


# ### B) Définition des fonctions convertirFichier, nettoyerListe, creerDictionnaire

# #### Ces fonctions permettent de transformer un fichier.txt composé exclusivement de mots séparés par un saut de ligne, en une liste de mots

# In[8]:


def convertirFichier(chemin):
    with open(chemin,"r",encoding="utf-8") as fic :
        text = fic.read()
    return(text.split("\n")) # on retourne une liste


# In[9]:


def convertirFichier2(chemin):
    fichier = open(chemin,"r",encoding="utf-8")
    text = fichier.read()
    fichier.close()
    return(text.split("\n")) # on retourne une liste


# #### Cette fonction permet de nettoyer une liste en vérifiant que les mots y figurant ne contiennent que des lettres de l'alphabet 

# In[10]:


def nettoyerListe(liste):
    global alphabet 
    liste = [mot for mot in liste if mot] # on retire les mots vides comme ''
    liste = list(set(liste)) # on supprime les doublons
    for mot in liste :
        if len(mot)>0:
            for char in mot.lower() : #parmi les char minuscules contenu dans le mot
                #print(char)
                if char not in alphabet :
                    if mot in liste :
                        #print("*")
                        liste.remove(mot) # on retire les mots qui contiennent une lettre qui n'est pas dans l'alphabet
    return(liste) # on retourne une liste


# In[11]:


def cleanDic(dic):
    suppr = []
    res = []
    global alphabet


    for mot in dic:
        ok = True

        if len(mot) > 1 and len(mot.split(' ')) == 1:
            #mot = enlever_accent(mot)

            for c in mot:
                if c not in alphabet:
                    suppr.append(mot)
                    ok = False

        else:
            suppr.append(mot)
            ok = False

        if ok:


            res.append(mot)

    res.sort()
    return(res)


# #### > Il s'agit de la fonction finale, cette fonction permet à partir d'un fichier.txt indiqué, de créer un dictionnaire ( liste de mots ) nettoyée, c'est à dire que les mots ne comportent que des lettres de l'alphabet ) <

# In[12]:


def creerDictionnaire(chemin):
    dic = convertirFichier(chemin)
    dic = cleanDic(dic) #On a remplacé nettoyer liste
    return(dic)


# ### C) Définition des fonctions sortirLettre et creerMotDigramme

# #### Cette fonction permet en fonction de notre lettre ( qui peut être a,b,c,... ou même debut ), de générer la lettre suivant à partir des probabilités contenu dans le digramme.

# In[13]:


def sortirLettreAlea(lettre_actuelle,digramme):
    listes_des_choix_suivants = digramme.columns.tolist() # on liste toutes les lettres qui peuvent suivre comme a,b,.. et fin
    liste_des_proba = digramme.loc[str(lettre_actuelle)].tolist() # on liste les proba liees a chaque choix
    lettre_suivante = np.random.choice(listes_des_choix_suivants, p=liste_des_proba) # on pioche une lettre selon les proba
    return(lettre_suivante)


# #### > Cette fonction est la fonction finale de l'exercice, elle permet de générer un mot suivant la méthode des Digramme !

# In[14]:


def creerMotAleaDigramme(digramme):
    global taillemax
    res = [sortirLettreAlea('debut',digramme)]
    while res[-1] != "fin" and len(res[:-1])<= taillemax:
        l = sortirLettreAlea(res[-1],digramme)
        res.append(l)
    res = res[0:-1]
    return "".join(res)


# ##### Voici un exemple de digramme réalisé :

# In[15]:


# path = 'data/fr/test.txt'
# ici les mots contenus sont "Salut, Arbre, Banane, Joshua, Cem, Mlamali, Mlachahe, Haligur, Said-Salimo, Bonacorsi"
#dictionnaire_dig = creerDictionnaire(path)
#dictionnaire_dig 


# In[16]:


#df3_test = creerDigramme(dictionnaire_dig)
#df3_test.head()


# ##### et voici 10 mots réalisés suivant l'utilisation du digramme précédent

# In[32]:


"""
for i in range(10):
    f2_mot = creerMotAleaDigramme(df3_test)
    f2_mot = f2_mot.capitalize() # Mettre la premiere lettre en majuscule
    print(f2_mot)
"""


# #### Pour la prochaine session, c'est à dire la fonctionnalité 3 : trigramme, il faut voir le trigramme, comme un digramme avec une dimension supplémentaire. (3d)

# # Fonctionnalité 3 : Trigramme

# ### A) Definition des fonctions couple, recupereCouple et creerDigramme

# #### Cette fonction permet à partir d'une liste de caractères comme ["a","b",c"] de donner une nouvelle liste ["aa","ab","ac","ba","bb","bc","ca","cb","cc"] avec tous les couples possibles

# In[18]:


def couple(liste) : # permet de créer une liste de couple de caractères de l'alphabet du genre aa ; ab ; ac...
    res = []
    for lettre in liste :
        for x in liste :
            res.append(lettre+x)
    return res


# #### Cette fonction permet de casser un mot en tous les couples de lettres consécutives qui le compose 

# In[19]:


def recupereCouple(mot): #permet de convertir "Salut" en "sa ; al ; lu ; ut" ( on le casse en couple de lettres )
    mot = mot.lower()
    return [''.join(pair) for pair in zip(mot[:-1], mot[1:])]


# #### Cette fonction permet de stocker tous les couples de lettres contenus dans un dictionnaire

# In[20]:


def stockCouples(dico) :
    res = []
    for mot in dico :
        res = res + recupereCouple(mot)
    return res


# ### B) Definition des fonctions motTrigramme, normaliserTrigramme et creerTrigramme

# #### La fonction motTrigramme permet de remplir un dataframe à partir d'un mot donné ( sans normalisation )

# In[21]:


def motTrigramme(mot,dataframe):
    mot = mot.lower() 
    lmot = recupereCouple(mot) # on convertit le mot en une liste de couples de lettres
    lmot = list(set(lmot)) # permet de supprimer les doublons de la liste 
    dataframe['fin'][lmot[-1]]+=1
    for i in lmot :
        for j in range(len(mot)-2) :
            if i==(mot[j]+mot[j+1]):
                dataframe[mot[j+2]][i] += 1


# #### La fonction normaliserTrigramme est analogue à normaliserDigramme ( même principe )

# In[22]:


def normaliserTrigramme(dataframe):
    indexs = dataframe.index.values.tolist() 
    for indexrow in indexs:
        somme = dataframe.loc[indexrow].sum() 
        if somme != 0:
            dataframe.loc[indexrow]/= somme


# #### > Il s'agit de la fonction finale, cette fonction permet de créer un Trigramme normalisé à partir d'un alphabet et d'un dictionnaire de mot ( liste de mots composés exclusivement de lettre de l'alphabet ) <

# In[23]:


def creerTrigramme(dic): # permet de créer le tableau trigramme à partir d'un dictionnaire
    global alphabet
    nom_lignes = couple(alphabet)
    lettres = list(alphabet)
    tableau = np.zeros((len(alphabet)*len(alphabet),len(alphabet)+1))
    dataframe = pd.DataFrame(tableau, index = (nom_lignes), columns = (lettres + ["fin"]))
    for mot in dic :
        motTrigramme(mot,dataframe)
    normaliserTrigramme(dataframe)
    return(dataframe) # on retourne le digramme fini


# ### C) Définition des fonctions sortirLettreAlea2 et creerMotTrigramme

# #### Cette fonction permet en fonction de notre couple de lettres ( qui peut être ab, bc, ca ect...), de générer la lettre suivante à partir des probabilités contenu dans le trigramme.

# In[24]:


def sortirLettreAlea2(couple_actuel,trigramme): 
    listes_des_choix_suivants = trigramme.columns.tolist() # on liste toutes les lettres qui peuvent suivre comme a,b,.. et fin
    liste_des_proba = trigramme.loc[str(couple_actuel)].tolist() # on liste les proba liees a chaque choix
    lettre_suivante = np.random.choice(listes_des_choix_suivants, p=liste_des_proba) # on pioche une lettre selon les proba
    return(lettre_suivante)


# #### > Cette fonction est la fonction finale de l'exercice, elle permet de générer un mot suivant la méthode des Trigrammes ! Par convention les deux premières lettres seront déterminées en suivant la méthode des digrammes

# In[25]:


def creerMotAleaTrigramme1(digramme,trigramme):
    global taillemax
    res = [sortirLettreAlea('debut',digramme)]
    deuxieme_lettre = sortirLettreAlea(res[-1],digramme)
    res.append(deuxieme_lettre)
    while res[-1] != "fin" and len(res[:-1])<= taillemax:
        if trigramme.loc[res[-2]+res[-1]].sum()!=1 : # si on a jamais rencontré le couple généré par le digramme 
            l="fin"
        else :
            l = sortirLettreAlea2(res[-2]+res[-1],trigramme)
        res.append(l)
    res = res[0:-1]
    return "".join(res)


# #### > Permet de créer un mot en utilisant uniquement le trigramme et on prendra les deux premières lettres parmi les couples rencontrés dans le dictionnaire

# In[26]:


def creerMotAleaTrigramme2(dico,trigramme):
    global taillemax  
    stockage = stockCouples(dico) #on recupere tous les couples du dico
    i = random.randint(0, len(stockage)-1) # on genere les deux premieres lettres en prenant aleatoirement un couple stocké
    res = []
    res.append(stockage[i][0]) # on stocke la premiere lettre
    res.append(stockage[i][1]) # on stocke la deuxieme lettre
    while res[-1] != "fin" and len(res[:-1])<= taillemax:
        if trigramme.loc[res[-2]+res[-1]].sum()!=1 : # si on a jamais rencontré le couple généré par le digramme 
            l="fin"
        else :
            l = sortirLettreAlea2(res[-2]+res[-1],trigramme)
        res.append(l)
    res = res[0:-1]
    return "".join(res)


# ##### Voici un exemple de trigramme réalisé ( avec le digramme en supplément ):

# In[27]:


'''path2 = 'data/fr/test.txt'
# ici les mots contenus sont "Salut, Arbre, Banane, Joshua, Cem, Mlamali, Mlachahe, Haligur, Said-Salimo, Bonacorsi"
dictionnaire_trig = creerDictionnaire(path2)
dictionnaire_trig'''


# In[28]:


'''digramme_test = creerDigramme(dictionnaire_trig)
digramme_test.head()'''


# In[29]:


'''trigramme_test = creerTrigramme(dictionnaire_trig)
trigramme_test.head()'''


# ##### et voici 10 mots réalisés suivant l'utilisation de la méthode des Trigrammes avec digramme :

# In[30]:


'''for compteur in range(10) :
    exemple = creerMotAleaTrigramme1(digramme_test,trigramme_test)
    exemple = exemple.capitalize() # Mettre la premiere lettre en majuscule
    print(exemple)'''


# ##### voici 1 mot réalisés suivant l'utilisation de la méthode des Trigrammes sans digramme :

# In[31]:


'''exemple = creerMotAleaTrigramme2(dictionnaire_trig,trigramme_test)
exemple = exemple.capitalize() # Mettre la premiere lettre en majuscule
print(exemple)'''

