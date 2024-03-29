import streamlit as st
import requests
from variable import link

st.set_page_config(
    page_title="Autorisation de crédit",  # => Quick reference - Streamlit
    page_icon=":smiley:",
    layout="centered",  # wide
    initial_sidebar_state="auto")  # collapsed

# On initialise les paramètres globaux au cas où on recharge la page
if 'my_params_1' not in st.session_state:
    st.session_state.my_params_1 = 5
if 'my_id_1' not in st.session_state:
    st.session_state.my_id_1 = 100043

# Barre latérale
nb_params = st.sidebar.slider("Sélectionner le nombre de paramètres à afficher", 1, 20, st.session_state.my_params_1)
st.session_state.my_params_2 = nb_params

id_client = st.sidebar.number_input('Id du client',min_value=0,value=st.session_state.my_id_1)
st.session_state.my_id_2 = id_client

# On fait la requête à l'url
url = f'{link}/id_local_params/?SK_ID_CURR={id_client}&NB_FEATURE={nb_params}'
response = requests.get(url).json()["local_weight"]

# On vérifie que la requête a abouti et on annonce si le crédit a été refusé ou accepté
st.markdown("# Demande de crédit :")

if response != -1:
    pred = requests.get(url).json()["prediction"]
    st.markdown("Votre demande de crédit est :")
    if pred == 0:
        st.success('Accordé !')
    else :
        st.error('Refusé...')
else :
    st.text('Client non trouvé. Veuillez le rajouter à la base de données.')

# On affiche le rapport des caractéristiques locales
st.markdown("## Importance des caractéristiques locales")

if response != -1:
    st.components.v1.html(response, width=1100, height=1000, scrolling=True)
else :
    st.text('Client non trouvé. Veuillez le rajouter à la base de données.')