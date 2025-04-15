#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 17:58:31 2025

@author: juan
"""

import streamlit as st

def recomendar_vino(plato, edad, genero, region_favorita):
    if edad < 18:
        return {"mensaje": "Está prohibida la venta de alcohol en España a menores de 18 años."}, 0
    
    vinos = {
        "Rías Baixas": {
            "vino": "Pazo de Señoráns Albariño",
            "uva": "Albariño",
            "cosecha": "2020",
            "region": "Rías Baixas, Galicia",
            "copa": 3.5,
            "botella": 25.0,
            "explicacion": "El Albariño, fresco y afrutado, va perfecto con platos fríos como el gazpacho."
        },
        "Rioja": {
            "vino": "Marqués de Murrieta Rioja Reserva",
            "uva": "Tempranillo, Mazuelo, Graciano",
            "cosecha": "2018",
            "region": "Rioja, La Rioja",
            "copa": 5.0,
            "botella": 35.0,
            "explicacion": "Vino con cuerpo y complejidad, ideal para platos tradicionales como la tortilla española."
        },
        "Valdeorras": {
            "vino": "Bodegas Valdesil Godello",
            "uva": "Godello",
            "cosecha": "2021",
            "region": "Valdeorras, Galicia",
            "copa": 4.0,
            "botella": 27.0,
            "explicacion": "Suave y equilibrado, armoniza bien con ensaladas y verduras."
        },
        "Cataluña": {
            "vino": "Cava Freixenet Cordon Negro",
            "uva": "Macabeo, Xarel·lo, Parellada",
            "cosecha": "NV",
            "region": "Cataluña",
            "copa": 3.0,
            "botella": 36.0,
            "explicacion": "Acidez y burbujas finas que equilibran los sabores intensos."
        },
        "Ribera del Duero": {
            "vino": "Protos Crianza",
            "uva": "Tempranillo",
            "cosecha": "2018",
            "region": "Ribera del Duero, Castilla y León",
            "copa": 3.1,
            "botella": 26.0,
            "explicacion": "Taninos suaves, ideal para platos con sabores complejos como la paella."
        }
    }

    platos_precio = {
        "Gazpacho andaluz": 9.0,
        "Tortilla española": 7.5,
        "Ensaladilla rusa": 6.5,
        "Almejas a la marinera": 12.0,
        "Pimientos de padrón": 8.0,
        "Paella Valenciana": 18.0,
        "Cordero asado al horno": 22.0,
        "Merluza a la gallega": 16.0,
        "Croquetas de jamón ibérico": 9.0,
        "Pollo al ajillo": 14.0,
    }

    if edad < 30:
        vino_recomendado = vinos["Rioja"] if genero == "masculino" else vinos["Rías Baixas"]
    else:
        vino_recomendado = vinos.get(region_favorita, None)

    return vino_recomendado if vino_recomendado else {"vino": "Vino genérico", "explicacion": "No se encontró una recomendación específica."}, platos_precio.get(plato, 0)


# --- INTERFAZ DE STREAMLIT ---
st.set_page_config(page_title="Sumiller Virtual", page_icon="🍷")
st.title("🍷 Chin Chin: Tu Sumiller Virtual")

st.markdown("Bienvenido a tu recomendador de vinos personalizado. Elige tus preferencias y te sugerimos el mejor vino para tu plato.")

# Inputs
edad = st.number_input("¿Qué edad tienes?", min_value=0, max_value=120, step=1)
genero = st.selectbox("¿Cuál es tu género?", ["masculino", "femenino", "otro"])
region_favorita = st.selectbox("¿Cuál es tu región vinícola favorita?", ["Rías Baixas", "Rioja", "Valdeorras", "Cataluña", "Ribera del Duero"])
plato_elegido = st.selectbox("¿Qué plato vas a comer?", [
    "Gazpacho andaluz", "Tortilla española", "Ensaladilla rusa", "Almejas a la marinera",
    "Pimientos de padrón", "Paella Valenciana", "Cordero asado al horno",
    "Merluza a la gallega", "Croquetas de jamón ibérico", "Pollo al ajillo"
])

if st.button("🍽️ Recomendar vino"):
    vino_info, precio_plato = recomendar_vino(plato_elegido, edad, genero, region_favorita)

    if "mensaje" in vino_info:
        st.warning(vino_info["mensaje"])
    else:
        st.success(f"Has elegido **{plato_elegido}** (Precio: {precio_plato}€)")
        st.markdown(f"### 🥂 Recomendación de vino: **{vino_info['vino']}**")
        st.markdown(f"- **Uva:** {vino_info['uva']}")
        st.markdown(f"- **Cosecha:** {vino_info['cosecha']}")
        st.markdown(f"- **Región:** {vino_info['region']}")
        st.markdown(f"- **Precio por copa:** {vino_info['copa']}€")
        st.markdown(f"- **Precio por botella:** {vino_info['botella']}€")
        st.info(vino_info["explicacion"])

