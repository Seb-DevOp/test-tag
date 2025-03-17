import streamlit as st
import requests

st.title("Frontend Streamlit")

# Appel au backend
backend_url = "http://backend:8000"
response = requests.get(f"{backend_url}/")

if response.status_code == 200:
    st.success(f"Réponse du backend : {response.json()}")
else:
    st.error("Erreur de connexion au backend")
