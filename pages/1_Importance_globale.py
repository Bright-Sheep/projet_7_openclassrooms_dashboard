import streamlit as st
import requests
import matplotlib.pyplot as plt
from variable import link

st.set_page_config(
    page_title="Importance globale",
    page_icon="📈",
)
st.markdown("# Importance des caractéristiques globales")
st.markdown("Quel est le poid des caractéristiques dans le modèle utilisé.")

# On fait la requête url
url = f'{link}/id_global_params/'

# On affiche le poids des caractéristiques globales
weight = requests.get(url).json()["global_weight"]
feature = requests.get(url).json()["feature"]

with plt.style.context("ggplot"):
    fig = plt.figure(figsize=(8,12))
    plt.barh(range(len(weight)), weight, color=["tab:blue" if coef<0 else "tab:orange" for coef in weight])
    plt.yticks(range(len(weight)), feature);
    plt.title("Poids des caractéristiques")
st.pyplot(fig)