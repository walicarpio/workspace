@echo off
title Lanzador App Savalcorp
:: Cambia a la carpeta donde está tu archivo (opcional si el .bat está en la misma carpeta)
cd /d "C:\Users\eberrios\Desktop\Personal\capacita\workspace\proyecto"
:: Ejecuta streamlit
streamlit run app.py
pause