# Rugby Injury Prediction App

Cette application Streamlit permet de prédire le risque de blessure non-contact chez les joueurs de rugby à partir de données individuelles et de tests de performance.

## Structure du projet

```
rugby-injury-prediction/
├── .gitignore
├── README.md
├── requirements.txt
├── streamlit_app.py
└── models/
    └── .gitkeep        # placeholder pour le dossier de modèles pickles
```

- **`streamlit_app.py`** : code principal de l’application Streamlit.
- **`models/`** : contient vos fichiers `.pkl` de modèles (bayes_lower_limb.pkl, bayes_ankle.pkl, bayes_severe.pkl, fusion_model.pkl).  
- **`requirements.txt`** : dépendances Python.
- **`.gitignore`** : fichiers et dossiers à ignorer par Git.

## Installation

1. Clonez le dépôt :  
   ```bash
   git clone https://github.com/<votre-utilisateur>/rugby-injury-prediction.git
   cd rugby-injury-prediction
   ```
2. Créez et activez un environnement virtuel (optionnel) :  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate   # Windows
   ```
3. Installez les dépendances :  
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Placez vos fichiers `.pkl` dans `models/`.  
2. Lancez l’application :  
   ```bash
   streamlit run streamlit_app.py
   ```
3. Ouvrez `http://localhost:8501` dans votre navigateur.

## Contribution

1. Forkez le projet.  
2. Créez une branche :  
   ```bash
   git checkout -b feature/ma-fonctionnalité
   ```
3. Ajoutez vos changements :  
   ```bash
   git add .
   git commit -m "feat: description"
   ```
4. Poussez et proposez une Pull Request.