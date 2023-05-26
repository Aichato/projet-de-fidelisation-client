# Projet-de-fidelisation-client
## Description de l'ensemble de données :
Il s'agit d'un jeu de données public. Le format du jeu de données est indiqué ci-dessous.

L'ensemble de données contient 10000 lignes et 14 colonnes différentes.

La colonne cible ici est : **'Exited'**.

source de donnée : https://www.kaggle.com/code/omarzakariasalah/bank-customer-churn-modeling/input#:~:text=Input%20Data-,Churn_Modelling,-.csv

|Les variables| Définition|
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
- Ingénierie des caractéristiques(chargement et traitement des données)
- Diviser l'ensemble de données en 70 % de l'ensemble de formation et 30 % de l'ensemble de test.
- Vérifier le score de précision pour l'ensemble de formation et l'ensemble de test.
- Comparer les précisions pour l'ensemble de formation et l'ensemble de test, afin de vérifier les problèmes de surajustement.

## importer les bibliotheques necessaires
- *import pandas as pd* : 

    **Pandas** est une librairie python qui permet de manipuler facilement des données à analyser
- *import pickle* :

    **pickle** est un module de python qui permet de sauvegarder une ou plusieurs variables dans un fichier et de récupérer leurs valeurs ultérieurement.
- *import seaborn as sns* :

    **Seaborn** est une bibliothèque qui offre la possibilité de résumer et de visualiser des données. Elle permet de créer de jolis graphiques statistiques en Python.
- from imblearn.over_sampling import SMOTE

    **SMOTE** est une méthode de suréchantillonnage des observations minoritaires, en cas de deséquilibre entre deux classe.
- from sklearn.model_selection import train_test_split

    **train_test_split** est une fonction qui permet de décomposer le jeu de données en 2 groupes: les données pour l'apprentissage et les données pour les tests.
- from sklearn.preprocessing import StandardScaler

    **StandardScaler** permet de faire la mise a l'echelle, c'est á dire normaliser les données
- from sklearn.linear_model import LogisticRegression

    **LogisticRegression** est utilisée pour la classification et l'analyse prédictive. La régression logistique estime la probabilité qu'un événement se produise.
- from sklearn.metrics import accuracy_score

  **accuracy_score** L'accuracy est souvent utilisée comme mesure de qualité pour la classification supervisée. c'est une métrique pour évaluer la performance des modèles de classification 
- from sklearn.metrics import precision_score, recall_score,f1_score

   **precision_score, recall_score,f1_score** permet de connaître le nombre de prédictions positifs bien effectuées.
- from sklearn.svm import SVC

   **SVC** est un modéle utilisé pour résoudre un problème de classification. 
- from sklearn.neighbors import KNeighborsClassifier

   **KNeighborsClassifier** peut être utilisé pour résoudre les problèmes de classification et de régression.
- from sklearn.tree import DecisionTreeClassifier

   **DecisionTreeClassifier** permet de réaliser une classification multi-classe à l'aide d'un arbre de décision.
- from sklearn.ensemble import RandomForestClassifier

   **RandomForestClassifier** est un algorithme de Machine Learning très populaire auprès des Data Scientists en raison de sa précision, de sa simplicité et de sa         flexibilité. Cet algorithme peut être utilisé pour résoudre les problèmes de régression et de classification.
- from sklearn.ensemble import GradientBoostingClassifier

   **GradientBoostingClassifier** détermine les défauts en utilisant des points de données pondérés.
   
  A la fin faire **streamlit run Prediction.py** dans le terminal de pycharm ou visual studio code pour lire le fichier **Prediction.py**
