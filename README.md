# Word inventing machine

We built a program using python able to invent words or simple sentences. (:fr:) <br>
Il existe plusieurs façons de générer aléatoirement des mots. Parmi toutes celles existantes, ce programme utilise deux méthodes pour former des mots : les méthodes d'enchainements digrammes et trigrammes.

### ⚙ How to run it
- Choisir la méthode de création voulu (digramme or trigramme)
- Selectionner le fichier/dictionnaire source sur lequel se baser pour créer nos mots
- Saisir le nombres de nouveaux mots que vous voulez créer
- Saisir la taille maximum que doivent faire ces mots

Vos nouveaux mots seront stockées dans un fichier .txt rangé dans le dossier /results !

Pour rappel, la langue française est composée de 42 lettres, les 26 lettres de l’alphabet latin : 13 voyelles accentuées, le graphème ç, ainsi que les deux ligatures (æ, œ), et aussi le symbole. Après avoir choisie un dictionnaire de base, les mots de celui qui ne respecterons pas cette alphabet ne seront pas pris en compte.

### 🔩 The methods used to create the words

#### • Enchainement de *digrammes*
Afin de générer des mots plus plausibles, à la lecture, nous orientons le choix de chaque lettre selon des règles probabilistes d’enchaînement de deux lettres. <br>

Pour pouvoir générer des mots à partir de digrammes, il faut dans un premier temps disposer d’un dictionnaire (une liste de mots). Puis pour chaque mot de ce dictionnaire, pour chaque lettre, regarder quelle est la lettre suivante, et mettre à jour la table de probabilité. Il peut être utile de mémoriser quelles lettres commencent un mot, et lesquelles terminent un mot. <br>

Par exemple, avec le mot informatique, on extrait la table de probabilités suivante :<br><br>
<img src="img/tableauinfo.png" width="300" alt="Table de probabilités du mot 'informatique'"><br><br>

Une fois la table complète de probabilités calculée, il suffit de partir d’une lettre, et d’enchaîner les lettres en fonction de la table de probabilité. En suivant le tableau ci-dessus, et en partant de la lettre 't', on génère le mot 'tique'. <br> 
Bien évidemment, cela n’a aucun sens de faire une table de probabilités sur un seul mot. <u>Plus on prend de mots en compte, plus la table de probabilités reflète correctement l’enchaînement des lettres dans la langue</u>.

#### •• Enchaînement de *trigrammes*
La méthode des trigrammes suit la même procédure que la méthode des digrammes, mais au lieu de ne considérer qu’une seule lettre pour regarder la suivante, on considère les deux précédentes. Cela crée une table de probabilités plus conséquente, mais beaucoup plus fine pour la création de mot.

### 📌 Résultats
Comparons les résultats obtenu avec les méthodes dit diagramme et trigramme, après avoir sélectionné une liste de 11 mille adjectifs français. Pour des paramètres égaux (nb de nouveau mots = 5000 ET taille max d'un nouveau mot = 15) on obtient : <br><br>

![](img/resultat1.png) <br>
[Nouveaux Verbe | DIGRAMME](results/result_DI_fr-adjectif_15_5000.txt "cliquez pour voir les mots crées") <br>

![](img/resultat2.png) <br>
[Nouveaux Verbe | TRIGRAMME](results/result_TRI_fr-adjectif_15_5000.txt "cliquez pour voir les mots crées")

On observe que certains mots paraissent français mais ne le sont pas haha ! <br>
Aussi on pourra remarquer que le % de nouveau mot crée avec le trigramme, déjà existant dans la liste de 6 mille verbes (donc le % de mots qui existent belle et bien !) est superieur au % de nouveau mots crée avec le digramme.

---
### 🎳 Bonus
Maintenant que notre programme marche bien, on peut encore s'amuser en l'executant avec d'autres listes de mots !
#### • Créer de nouveaux prénoms Comorien 🇰🇲
De parents comoriens, chaque membre de ma famille possède un prénom comorien, un prénom qui sonnent comorien. Je me suis dis, pourquoi ne pas créer des prénoms comoriens pour voir ? <br>

Pour ce faire, j'avais besoin d'un dictionnaire de prénoms comoriens.. mais contrairement au dictionnaire de prénoms français, sur internet on ne trouve pas de dictionnaire de mots comorien... Je devais donc créer moi même ce dictionnaire.<br>

Non, je n'ai pas tapé un par un tous les noms comoriens que je connaissais. En faite, en cherchant une liste de prénoms comorien je suis tombé sur un site qui énumération plein de prénoms féminin et masculin comorien. Hmmm comment récuperer des élements sur une veille page we.. bim WEB SCRAPING !
J'ai donc utiliser une methode de <b> web scraping </b> en python pour récuperer super facilement ces 2 listes de prénoms, les laver et les convertir en format txt utilisable pour mon programme.<br>

Après execution magie magie on obtiens :<br>
[Nouveaux prénoms comoriens | Fille](results/result_DI_km-prenomFeminin_15_5000.txt "cliquez pour voir les mots crées") <br>
[Nouveaux Prénoms comoriens | Garçon](results/result_DI_km-prenomMasculin_15_5000.txt "cliquez pour voir les mots crées")<br>

J'ai montré ça à mes parents, ils ont pu validé le fait que malgré que la majorité des mots n'aies aucun sens, on dirait vraiment des prénoms comoriens ! <br> 

En conclusion, comme avec les nouveaux mots crées avec un dictionnaire français, on se rend compte qu'il y a une "mélodie" dans ces nouveaux mots crée qui nous semble familière. On peut même dire que les mots sont en réalité des partitions, les enchainements de lettre sont des enchainements de note et selon la disposition de certaines notes, l'air joué change, la langue change. 

#### • Créer des noms aléatoires pour mes composition 🎹


---
### 📸 Screenshots 

![](img/1.PNG "screen")
![](img/3.png "screen")

---
### 👨🏾‍💻👨🏼‍💻 Auteurs
[Mlamali SAID SALIMO](https://www.linkedin.com/in/mlamalisaidsalimo) and [Joshua Bonacorsi](https://www.linkedin.com/in/joshuabonacorsi). <br/>
