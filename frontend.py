
from unittest import case

import streamlit as st

def faire_row(a_age,a_educ,a_envi,a_carriere,a_ambi,a_ouver,a_extra,a_agrea,a_cons,a_chrono,a_sponta,a_express,a_langage,b_age,b_educ,b_envi,b_carriere,b_ambi,b_ouver,b_extra,b_agrea,b_cons,b_chrono,b_sponta,b_express,b_langage):
    #conversion education
    match a_educ:
        case "Bac ou moins":
            a_educ = 0
        case "Bac +1/2":
            a_educ = 1
        case "Bac +3":
            a_educ = 2
        case "Bac +5":
            a_educ = 3
        case "Doctorat":
            a_educ = 4

    match b_educ:
        case "Bac ou moins":
            b_educ = 0
        case "Bac +1/2":
            b_educ = 1
        case "Bac +3":
            b_educ = 2
        case "Bac +5":
            b_educ = 3
        case "Doctorat":
            b_educ = 4


    #conversion environnement
    match a_envi:
        case "Urbain":
            a_envi = 0
        case "Suburbain":
            a_envi = 1
        case "Rural":
            a_envi = 2
    match b_envi:
        case "Urbain":
            b_envi = "Urban"
        case "Suburbain":
            b_envi = "Suburban"
        case "Rural":
            b_envi = "Rural"


    #conversion carriere:
    match a_carriere:
        case "Finance":
            a_carriere = "Finance"
        case "Ingénierie":
            a_carriere = "Engineering"
        case "Santé":
            a_carriere = "Healthcare"
        case "Technologie":
            a_carriere = "Tech"
        case "Marketing":
            a_carriere = "Marketing"
        case "Entreprenariat":
            a_carriere = "Entrepreneurship"
        case "Science":
            a_carriere = "Science"
        case "Droit":
            a_carriere = "Law"
        case "Arts":
            a_carriere = "Arts"
        case "Education":
            a_carriere = "Education"

    match b_carriere:
            case "Finance":
                b_carriere = "Finance"
            case "Ingénierie":
                b_carriere = "Engineering"
            case "Santé":
                b_carriere = "Healthcare"
            case "Technologie":
                b_carriere = "Tech"
            case "Marketing":
                b_carriere = "Marketing"
            case "Entreprenariat":
                b_carriere = "Entrepreneurship"
            case "Science":
                b_carriere = "Science"
            case "Droit":
                b_carriere = "Law"
            case "Arts":
                b_carriere = "Arts"
            case "Education":
                b_carriere = "Education"


    #conversion langage
    match a_langage:
        case "Cadeaux":
            a_langage = "Receiving Gifts"
        case "Moments":
            a_langage = "Quality Time"
        case "Services":
            a_langage = "Acts of Service"
        case "Toucher":
            a_langage = "Physical Touch"
        case "Affirmation":
            a_langage = "Words of Affirmation"

    match b_langage:
            case "Cadeaux":
                b_langage = "Receiving Gifts"
            case "Moments":
                b_langage = "Quality Time"
            case "Services":
                b_langage = "Acts of Service"
            case "Toucher":
                b_langage = "Physical Touch"
            case "Affirmation":
                b_langage = "Words of Affirmation"


    row = {
        "a_age": a_age,
        "a_education": a_educ,
        "a_location": a_envi,
        "a_career": a_carriere,
        "a_ambition": a_ambi,
        "a_openness": a_ouver,
        "a_extraversion": a_extra,
        "a_agreeableness": a_agrea,
        "a_conscientiousness": a_cons,
        "a_chronotype": a_chrono,
        "a_spontaneity": a_sponta,
        "a_expressiveness": a_express,
        "a_love_language": a_langage,
        "b_age": b_age,
        "b_education": b_educ,
        "b_location": b_envi,
        "b_career": b_carriere,
        "b_ambition": b_ambi,
        "b_openness": b_ouver,
        "b_extraversion": b_extra,
        "b_agreeableness": b_agrea,
        "b_conscientiousness": b_cons,
        "b_chronotype": b_chrono,
        "b_spontaneity": b_sponta,
        "b_expressiveness": b_express,
        "b_love_language": b_langage
    }
    return row

def analyse(profils):
    return "placeholder"



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
    ligne = faire_row(a_age, a_education, a_environnement, a_carriere, a_ambition, a_ouverture, a_extraversion, a_agreabilite, a_consciensiosite, a_chronotype, a_spontaneite, a_expressivite, a_langage, b_age, b_education, b_environnement, b_carriere, b_ambition, b_ouverture, b_extraversion, b_agreabilite, b_consciensiosite, b_chronotype, b_spontaneite, b_expressivite, b_langage)
    compatibilite = analyse(ligne) 
    st.write(f"Compatibilité amoureuse : {compatibilite}")
    st.write(ligne)
    st.success("Merci !")