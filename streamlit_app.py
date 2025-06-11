import streamlit as st
import pandas as pd
import numpy as np
import pickle
import shap
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------
# Charger les modèles pré-entraînés (dossier models/)
# -----------------------------------------------------------------------
@st.cache(allow_output_mutation=True)
def load_models():
    return {
        'Blessure membre inférieur': pickle.load(open('models/bayes_lower_limb.pkl', 'rb')),
        'Blessure cheville':          pickle.load(open('models/bayes_ankle.pkl',      'rb')),
        'Blessure sévère':            pickle.load(open('models/bayes_severe.pkl',     'rb')),
        'Fusion multimodale':         pickle.load(open('models/fusion_model.pkl',    'rb')),
    }

models = load_models()

# -----------------------------------------------------------------------
# Interface utilisateur
# -----------------------------------------------------------------------
st.title("Prédiction du risque de blessure - Joueurs de rugby")
st.write("Entrez les données du joueur pour estimer le risque et le type probable de blessure non-contact.")

# Sidebar
st.sidebar.header("Données du joueur")
age           = st.sidebar.number_input("Âge", min_value=16, max_value=50, value=20)
poids         = st.sidebar.number_input("Poids (kg)", value=80)
ac_ratio      = st.sidebar.number_input("Acute:Chronic Load Ratio", value=1.0)
monotony      = st.sidebar.number_input("Monotonie de charge", value=1.0)
v10           = st.sidebar.number_input("Vitesse 10 m (s)", value=1.8, step=0.01)
v40           = st.sidebar.number_input("Vitesse 40 m (s)", value=5.0, step=0.01)
f_adducteurs  = st.sidebar.number_input("Force adducteurs (N)", value=300)
f_ischio      = st.sidebar.number_input("Force ischio-jambiers (N)", value=300)
angle_dorsi   = st.sidebar.number_input("Angle dorsiflexion (°)", value=20)
hist_inf      = st.sidebar.selectbox("Antécédent blessure membre inférieur", ['Non','Oui'])
hist_cheville = st.sidebar.selectbox("Antécédent blessure cheville", ['Non','Oui'])
hist_comm     = st.sidebar.selectbox("Antécédent commotion cérébrale", ['Non','Oui'])
position      = st.sidebar.selectbox("Position", ['Arrière','Avant'])

if st.sidebar.button("Estimer le risque"):
    df = pd.DataFrame({
        'Age': [age], 'Poids': [poids],
        'AcuteChronicRatio': [ac_ratio],
        'Monotony': [monotony],
        'Vitesse10m': [v10], 'Vitesse40m': [v40],
        'ForceAdducteurs': [f_adducteurs],
        'ForceIschio': [f_ischio],
        'AngleDorsiflexion': [angle_dorsi],
        'HistMembreInf': [1 if hist_inf=='Oui' else 0],
        'HistCheville': [1 if hist_cheville=='Oui' else 0],
        'HistCommotion': [1 if hist_comm=='Oui' else 0],
        'PositionAvant': [1 if position=='Avant' else 0]
    })
    # Prédictions
    probabilities = {label: model.predict_proba(df)[0][1] for label, model in models.items()}
    # Affichage
    st.subheader("Probabilités de blessure")
    st.bar_chart(pd.Series(probabilities))
    top_type = max(probabilities, key=probabilities.get)
    st.markdown(f"**Blessure la plus probable :** {top_type}")

    # SHAP pour interprétation
    st.subheader("Interprétation SHAP")
    explainer = shap.Explainer(models['Fusion multimodale'], df)
    shap_values = explainer(df)
    shap.summary_plot(shap_values, df, show=False)
    st.pyplot(plt.gcf())