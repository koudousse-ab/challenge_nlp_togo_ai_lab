import re
import joblib
import streamlit as st


# ==============================
# Chargement des modèles
# ==============================

vectorizer = joblib.load("tfidf_vectorizer.joblib")
model = joblib.load("modele_logistic_regression.joblib")
stopwords_fr = joblib.load("stopwords_fr.joblib")


# ==============================
# Prétraitement du texte
# ==============================

def nettoyer_texte(texte):
    texte = texte.lower()
    texte = re.sub(r"[\W\d_]+", " ", texte, flags=re.UNICODE)
    texte = re.sub(r"\s+", " ", texte).strip()

    tokens = texte.split()

    tokens = [
        mot for mot in tokens
        if mot not in stopwords_fr
    ]

    return " ".join(tokens)


# ==============================
# Interface
# ==============================

st.set_page_config(
    page_title="Classification NLP",
    page_icon="💬"
)

st.title("Classification de commentaires citoyens")
st.write(
    "Entrez un commentaire pour prédire sa catégorie."
)

texte_utilisateur = st.text_area(
    "Votre commentaire",
    placeholder="Exemple : Le service était rapide et le personnel accueillant."
)

if st.button("Classifier"):

    if not texte_utilisateur.strip():
        st.warning("Veuillez saisir un commentaire.")

    else:
        texte_propre = nettoyer_texte(texte_utilisateur)

        vecteur = vectorizer.transform([texte_propre])

        prediction = model.predict(vecteur)[0]

        st.success(f"Catégorie prédite : **{prediction}**")