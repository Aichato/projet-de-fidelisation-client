# Projet-de-fidelisation-client
## Description de l'ensemble de données :
Il s'agit d'un jeu de données public. Le format du jeu de données est indiqué ci-dessous.

L'ensemble de données contient 10000 lignes et 14 colonnes différentes.

La colonne cible ici est : **'Exited'**.

source de donnée : https://www.kaggle.com/code/omarzakariasalah/bank-customer-churn-modeling/input#:~:text=Input%20Data-,Churn_Modelling,-.csv

|Les variable| Définition|
|:-----------|:----------|
|RowNumber | Le nombre de colonne unique|
|CustomerId | Identifiant unique du client|
|Surname | Nom du client|
|CreditScore | Le score de credit|
|Geography | Emplacement géographique des clients|
|Gender | Le sexe du client|
|Age | L'age du client|
|Tenure | Le nombre d'année|
|Balance | Solde actuel des clients|
|NumOfProducts | Le nombre de service|
|HasCrCard | Si un client possède ou non une carte de crédit|
|IsActiveMember | Si un client est actif ou non|
|EstimatedSalary | Estimation du salaire de chaque client|
|Exited | **Le client a quitté la banque ou non (Variable cible)**|


## Flux de travail
Afin de créer un modèle, voici la procédure à suivre: 
- Ingénierie des caractéristiques(
- Diviser l'ensemble de données en 70 % de l'ensemble de formation et 30 % de l'ensemble de test.
- Vérifier le score de précision pour l'ensemble de formation et l'ensemble de test.
- Comparer les précisions pour l'ensemble de formation et l'ensemble de test, afin de vérifier les problèmes de surajustement.
