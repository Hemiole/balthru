
import streamlit as st

st.title("Love(i,a)")
st.write("Calculez votre compatibilité amoureuse")

with st.form("Formulaire"):
    col1, col2 = st.columns(2)
    col1.write("Personne A")
    col2.write("Personne B")

    a_age = col1.number_input("Age", 0, 200, key=100)
    a_education = col1.select_slider("Niveau d'éducation", ["Bac ou moins", "Bac +1/2", "Bac +3", "Bac +5", "Doctorat"], key=101)
    a_environnement = col1.segmented_control("Environnement", ["Urbain", "Suburbain", "Rural"], key=102)
    a_carriere = col1.selectbox("Domaine d'activité", ["Finance", "Ingénierie", "Santé", "Technologie", "Marketing", "Entreprenariat", "Science", "Droit", "Arts", "Education"], key=103)
    a_ambition = col1.slider("Ambition", 0.00, 1.00, 0.00, 0.01, key=104)
    a_ouverture = col1.slider("Ouverture", 0.00, 1.00, 0.00, 0.01, key=105)
    a_extraversion = col1.slider("Extraversion", 0.00, 1.00, 0.00, 0.01, key=106)
    a_agreabilite = col1.slider("Agréabilité", 0.00, 1.00, 0.00, 0.01, key=107)
    a_consciensiosite = col1.slider("Consciensiosité", 0.00, 1.00, 0.00, 0.01, key=108)
    a_chronotype = col1.slider("Chronotype (du soir au matin)", 0.00, 1.00, 0.00, 0.01, key=109)
    a_spontaneite = col1.slider("Spontanéité", 0.00, 1.00, 0.00, 0.01, key=110)
    a_expressivite = col1.slider("Expressivité émotionnelle", 0.00, 1.00, 0.00, 0.01, key=111)
    a_langage = col1.selectbox("Langage d'amour", ["Cadeaux", "Moments", "Services", "Toucher", "Affirmation"], key=112)

    b_age = col2.number_input("Age", 0, 200, key=200)
    b_education = col2.select_slider("Niveau d'éducation", ["Bac ou moins", "Bac +1/2", "Bac +3", "Bac +5", "Doctorat"], key=201)
    b_environnement = col2.segmented_control("Environnement", ["Urbain", "Suburbain", "Rural"], key=202)
    b_carriere = col2.selectbox("Domaine d'activité", ["Finance", "Ingénierie", "Santé", "Technologie", "Marketing", "Entreprenariat", "Science", "Droit", "Arts", "Education"], key=203)
    b_ambition = col2.slider("Ambition", 0.00, 1.00, 0.00, 0.01, key=204)
    b_ouverture = col2.slider("Ouverture", 0.00, 1.00, 0.00, 0.01, key=205)
    b_extraversion = col2.slider("Extraversion", 0.00, 1.00, 0.00, 0.01, key=206)
    b_agreabilite = col2.slider("Agréabilité", 0.00, 1.00, 0.00, 0.01, key=207)
    b_consciensiosite = col2.slider("Consciensiosité", 0.00, 1.00, 0.00, 0.01, key=208)
    b_chronotype = col2.slider("Chronotype (du soir au matin)", 0.00, 1.00, 0.00, 0.01, key=209)
    b_spontaneite = col2.slider("Spontanéité", 0.00, 1.00, 0.00, 0.01, key=210)
    b_expressivite = col2.slider("Expressivité émotionnelle", 0.00, 1.00, 0.00, 0.01, key=211)
    b_langage = col2.selectbox("Langage d'amour", ["Cadeaux", "Moments", "Services", "Toucher", "Affirmation"], key=212)

    envoyer = st.form_submit_button("Calculer")

if envoyer:
    st.success("Merci !")