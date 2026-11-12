
import streamlit as st

st.title("Love(i,a)")
st.write("Bienvenue")

with st.form("Formulaire"):
    a_age = st.number_input("Age", 0, 200)
    a_education = st.select_slider("Niveau d'éducation", ["Bac ou moins", "Bac +1/2", "Bac +3", "Bac +5", "Doctorat"])
    a_environnement = st.segmented_control("Environnement", ["Urbain", "Suburbain", "Rural"])
    a_carriere = st.selectbox("Domaine d'activité", ["Finance", "Ingénierie", "Santé", "Technologie", "Marketing", "Entreprenariat", "Science", "Droit", "Arts", "Education"])
    a_ambition = st.slider("Ambition", 0.00, 1.00, 0.00, 0.01)
    a_ouverture = st.slider("Ouverture", 0.00, 1.00, 0.00, 0.01)
    a_extraversion = st.slider("Extraversion", 0.00, 1.00, 0.00, 0.01)
    a_agreabilite = st.slider("Agréabilité", 0.00, 1.00, 0.00, 0.01)
    a_consciensiosite = st.slider("Consciensiosité", 0.00, 1.00, 0.00, 0.01)
    
    a_chronotype = st.slider("Chronotype (du soir au matin)", 0.00, 1.00, 0.00, 0.01)
    a_spontaneite = st.slider("Spontanéité", 0.00, 1.00, 0.00, 0.01)

    a_expressivite = st.slider("Expressivité émotionnelle", 0.00, 1.00, 0.00, 0.01)

    a_langage = st.selectbox("Langage d'amour", ["Cadeaux", "Moments", "Services", "Toucher", "Affirmation"])
    envoyer = st.form_submit_button("Calculer")
