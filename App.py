import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Analyse de la Vitesse de Production")

uploaded_file = st.file_uploader("Veuillez télécharger votre fichier Excel", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        # Validation des données avec un bloc `else`
        if "Temps" not in df.columns or "Vitesse" not in df.columns:
            st.error("Le fichier Excel doit contenir des colonnes 'Temps' et 'Vitesse'.")
        else:
            # Affichage des données brutes
            st.write("Données du fichier Excel :")
            st.write(df)

            # Graphique en ligne de la vitesse de production
            st.write("Graphique de la Vitesse de Production en Ligne :")
            fig, ax = plt.subplots()
            ax.plot(df["Temps"], df["Vitesse"])
            ax.set_xlabel("Temps")
            ax.set_ylabel("Vitesse de Production")
            st.pyplot(fig)

            # Graphique en barre de la vitesse de production
            st.write("Graphique en Barre de la Vitesse de Production :")
            fig, ax = plt.subplots()
            ax.bar(df["Temps"], df["Vitesse"])
            ax.set_xlabel("Temps")
            ax.set_ylabel("Vitesse de Production")
            st.pyplot(fig)

            # Calcul de la vitesse moyenne
            vitesse_moyenne = df["Vitesse"].mean()
            st.write(f"Vitesse de production moyenne : {vitesse_moyenne:.2f}")

    except Exception as e:
        st.error(f"Une erreur s'est produite lors du traitement du fichier: {e}")
