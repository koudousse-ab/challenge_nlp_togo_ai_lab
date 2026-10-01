# Classification de commentaires citoyens sur les services publics

## Objectif
Construire un système NLP capable de classer automatiquement les commentaires en **Satisfaction**, **Insatisfaction** et **Suggestion**.

## Données
- 150 commentaires, répartis équitablement entre les 3 catégories.
- Prétraitement : minuscules, nettoyage, tokenisation et stopwords français.
- Les termes éwé/mina sont conservés pour préserver l'information potentiellement utile.

## Méthodologie
- Séparation : 80 % entraînement / 20 % test (`random_state=42`).
- Vectorisation : **TF-IDF** avec unigrammes et bigrammes.
- Modèles : **Logistic Regression** et **Linear SVM**.
- Évaluation : Accuracy, F1-score macro et matrices de confusion.

## Résultats
| Modèle | Accuracy | F1-score macro |
|---|---:|---:|
| Logistic Regression | 70,00 % | 0,7033 |
| Linear SVM | 70,00 % | 0,7012 |

## Limites
Le dataset est de petite taille, ce qui limite la diversité des exemples et la robustesse de la classification.

## Pistes d'amélioration
- Augmenter le dataset, notamment avec davantage de commentaires éwé/mina.
- Tester des modèles multilingues pré-entraînés comme CamemBERT, mBERT ou XLM-R.

## Reproduction
```bash
pip install -r requirements.txt
```
Puis ouvrir et exécuter `notebook.ipynb`.
