import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Analyse de la Vitesse de Production")

uploaded_file = st.file_uploader("Veuillez télécharger votre fichier Excel", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        # Vérification que les colonnes nécessaires sont présentes
        if "CODE PRODUIT" not in df.columns or "QTY LBS" not in df.columns or "HR" not in df.columns:
            st.error("Le fichier Excel doit contenir les colonnes 'CODE PRODUIT', 'QTY LBS' et 'HR'.")
        else:
            # Affichage des données brutes
            st.write("Données du fichier Excel :")
            st.write(df)

            # Calcul de la vitesse de production (QTY LBS / HR)
            df["Vitesse de Production"] = df["QTY LBS"] / df["HR"]

            # Graphique en ligne de la vitesse de production
            st.write("Graphique de la Vitesse de Production en Ligne :")
            fig, ax = plt.subplots()
            ax.plot(df["#ÉTAPE"], df["Vitesse de Production"])
            ax.set_xlabel("Étape de Production")
            ax.set_ylabel("Vitesse de Production (Lbs/Heure)")
            st.pyplot(fig)

            # Graphique en barre de la vitesse de production
            st.write("Graphique en Barre de la Vitesse de Production :")
            fig, ax = plt.subplots()
            ax.bar(df["#ÉTAPE"], df["Vitesse de Production"])
            ax.set_xlabel("Étape de Production")
            ax.set_ylabel("Vitesse de Production (Lbs/Heure)")
            st.pyplot(fig)

            # Affichage de la vitesse moyenne
            vitesse_moyenne = df["Vitesse de Production"].mean()
            st.write(f"Vitesse de production moyenne : {vitesse_moyenne:.2f} Lbs/Heure")

    except Exception as e:
        st.error(f"Une erreur s'est produite lors du traitement du fichier: {e}")

    except Exception as e:
        st.error(f"Une erreur s'est produite lors du traitement du fichier: {e}")
