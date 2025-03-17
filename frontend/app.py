import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="NetMonitor", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu_options = ["Tableau de bord", "Anomalies", "Statistiques", "Logs & Historique"]

def button_nav():
    selected_button = None
    for option in menu_options:
        if st.sidebar.button(option, key=option):
            selected_button = option
    return selected_button

selected_button = button_nav()
if not selected_button:
    selected_button = "Tableau de bord"

# Données factices simulant l'interface des images
connexions_data = pd.DataFrame({
    "Horodatage": ["2023-03-15 14:32:45", "2023-03-15 14:33:12", "2023-03-15 14:35:01"],
    "Source": ["192.168.1.105:54321", "192.168.1.105:54322", "45.33.12.186:22"],
    "Destination": ["216.58.215.110:443", "172.217.21.142:80", "192.168.1.1:22345"],
    "Protocole": ["HTTPS", "HTTP", "SSH"],
    "Durée": ["00:02:15", "00:00:45", "00:05:22"],
    "Statut": ["Normal", "Normal", "Suspect"]
})

anomalies_data = pd.DataFrame({
    "Horodatage": ["2023-03-15 14:35:01", "2023-03-15 14:40:12", "2023-03-15 15:00:45"],
    "IP Source": ["45.33.12.186", "203.0.113.42", "198.51.100.123"],
    "IP Destination": ["192.168.1.1", "192.168.1.1", "192.168.1.105"],
    "Type": ["Tentative de connexion SSH", "Scan de ports", "Trafic HTTP suspect"],
    "Risque": ["Élevé", "Moyen", "Faible"]
})

# Tableau de bord
if selected_button == "Tableau de bord":
    st.title("📡 Surveillance Réseau")
    st.dataframe(connexions_data)
    
    # Graphique d'activité réseau
    st.subheader("📊 Activité Réseau")
    activity_chart = px.line(x=["14:30", "14:35", "14:40", "14:45", "15:00"], y=[9, 18, 27, 15, 36], title="Flux de connexions par minute")
    st.plotly_chart(activity_chart, use_container_width=True)

# Anomalies
elif selected_button == "Anomalies":
    st.title("🚨 Détection d'Anomalies")
    st.dataframe(anomalies_data)
    
    # Graphique des tendances
    st.subheader("📈 Tendance des Anomalies")
    anomalies_chart = px.bar(x=["00:00", "04:00", "08:00", "12:00", "14:00"], y=[1, 2, 3, 2, 4], title="Évolution des anomalies")
    st.plotly_chart(anomalies_chart, use_container_width=True)

# Statistiques
elif selected_button == "Statistiques":
    st.title("📊 Statistiques Réseau")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Connexions Totales", "1245", "+9%")
    col2.metric("Connexions Suspectes", "3.2%", "-0.4%")
    col3.metric("Connexions Actives", "42", "-3")
    col4.metric("Anomalies Détectées", "8", "-2")
    
    # Graphique d'activité réseau
    st.subheader("📊 Connexions par protocole")
    protocols_chart = px.pie(values=[45, 25, 15, 10, 5], names=["HTTPS", "HTTP", "DNS", "SSH", "Autres"], title="Répartition des Protocoles")
    st.plotly_chart(protocols_chart, use_container_width=True)

# Logs et Historique
elif selected_button == "Logs & Historique":
    st.title("📜 Logs & Historique")
    st.dataframe(connexions_data)
    st.download_button("📥 Exporter les logs", data=connexions_data.to_csv(index=False), file_name="logs.csv", mime="text/csv")