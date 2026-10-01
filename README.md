# Classification de commentaires citoyens sur les services publics

Ce projet porte sur la classification automatique de commentaires citoyens en trois catégories : Satisfaction, Insatisfaction et Suggestion.
Le dataset contient 150 commentaires, répartis de manière équilibrée entre les trois classes.
Les textes ont été mis en minuscules, nettoyés des caractères indésirables, tokenisés et traités avec une liste de stopwords français.
Les éventuels termes éwé/mina ont été conservés afin de ne pas supprimer une information potentiellement utile à la classification.
Les données ont été séparées en 80 % pour l'entraînement et 20 % pour le test, avec un random_state fixé à 42.
La représentation TF-IDF a été utilisée avec des unigrammes et des bigrammes.
Deux algorithmes ont été testés : Logistic Regression et Linear SVM.
Les modèles ont été évalués avec l'Accuracy, le F1-score macro et les matrices de confusion.
Logistic Regression a obtenu une Accuracy de 70,00 % et un F1-score macro de 0,7033.
Linear SVM a obtenu une Accuracy de 70,00 % et un F1-score macro de 0,7012.
L'analyse des erreurs montre des confusions liées notamment aux formulations courtes, ambiguës et à certains commentaires proposant des améliorations.
Une limite importante est la faible taille du dataset, qui réduit la diversité des exemples disponibles pour l'apprentissage.
Deux pistes d'amélioration sont l'augmentation du dataset et l'utilisation de modèles multilingues pré-entraînés.
Pour reproduire le projet, installer les dépendances avec `pip install -r requirements.txt`, puis exécuter le notebook Jupyter.
