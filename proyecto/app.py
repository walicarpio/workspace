import streamlit as st
import pandas as pd
import smtplib
import os
import time
from email.message import EmailMessage
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="SAVAL - Envío de Artículos", page_icon="📚", layout="wide")

st.title("📚 Centro SAVAL: Automatización de Artículos Científicos")
st.markdown("Carga el archivo Excel para iniciar el proceso de envío masivo.")

# --- BARRA LATERAL (Ajustes Técnicos) ---
with st.sidebar:
    st.header("⚙️ Configuración")
    email_principal = st.text_input("Correo Autenticación", value="eberrios@savalcorp.com")
    email_password = st.text_input("Contraseña de Aplicación", type="password", value="dqfpkbcjkbpdrvty")
    casilla_compartida = st.text_input("Enviar desde (Casilla)", value="calvomackenna@savalcorp.com")
    folder_adjuntos = st.text_input("Carpeta de Adjuntos", value="./documentos/pediatria")
    delay = st.slider("Pausa entre correos (seg)", 1, 10, 3)

# --- PASO 1: CARGA DE ARCHIVO ---
uploaded_file = st.file_uploader("Sube tu archivo usuarios.xlsx", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    # Vista previa de datos
    with st.expander("📊 Ver vista previa del Excel"):
        st.dataframe(df)

    # --- PASO 2: REDACCIÓN Y PREVIA ---
    st.divider()
    col_text, col_prev = st.columns([1, 1])
    
    with col_text:
        st.subheader("📝 Redacción del Mensaje")
        asunto_base = st.text_input("Asunto", value="Solicitud de Artículos Científicos Centro SAVAL")
        cuerpo_base = st.text_area("Cuerpo del mensaje", 
            value="Estimado(a) doctor(a) {nombre},\n\nJunto con saludarle, de acuerdo a lo solicitado a través de nuestro(a) Representante SAVAL {representante}, envío copia en texto completo de los artículos seleccionados desde el catálogo de artículos científicos para el mes de febrero 2026.\n\nEsperando que el material enviado sea de interés y utilidad, me despido atentamente.",
            height=250)

    with col_prev:
        st.subheader("👁️ Vista Previa del Primer Envío")
        if not df.empty:
            f = df.iloc[0]
            try:
                # Simulamos el primer registro para la previa
                prev_asunto = f"{asunto_base} - {f['materia']}"
                prev_cuerpo = cuerpo_base.format(nombre=f['nombre'], representante=f['RPS'])
                st.info(f"**Asunto:** {prev_asunto}\n\n**Para:** {f['correo']}\n\n**Mensaje:**\n{prev_cuerpo}")
                st.caption(f"📎 Adjuntos: {f['archivo solicitado']}")
            except Exception as e:
                st.error(f"Error en campos: Asegúrate que el Excel tenga las columnas 'nombre', 'RPS' y 'materia'.")

    # --- PASO 3: EJECUCIÓN ---
    st.divider()
    if st.button("🚀 INICIAR ENVÍO MASIVO", use_container_width=True):
        if not os.path.exists(folder_adjuntos):
            st.error(f"❌ La carpeta de adjuntos no existe: {folder_adjuntos}")
        else:
            fallidos = []
            exitosos = 0
            progreso = st.progress(0)
            status = st.empty()

            try:
                server = smtplib.SMTP("smtp.office365.com", 587)
                server.starttls()
                server.login(email_principal, email_password)

                for index, fila in df.iterrows():
                    nombre = str(fila['nombre']).strip()
                    destinatario = str(fila['correo']).strip()
                    representante = str(fila['RPS']).strip()
                    materia = str(fila['materia']).strip()
                    lista_archivos = [a.strip() for a in str(fila['archivo solicitado']).split(',')]

                    status.text(f"Enviando a: {destinatario}...")
                    
                    try:
                        msg = EmailMessage()
                        msg['Subject'] = f"{asunto_base} - {materia}"
                        msg['From'] = casilla_compartida
                        msg['To'] = destinatario
                        msg.set_content(cuerpo_base.format(nombre=nombre, representante=representante))

                        adjuntos_cont = 0
                        for a_nombre in lista_archivos:
                            ruta = os.path.join(folder_adjuntos, a_nombre)
                            if os.path.exists(ruta):
                                with open(ruta, 'rb') as f:
                                    msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=a_nombre)
                                adjuntos_cont += 1
                            else:
                                fallidos.append(f"Fila {index+1} ({destinatario}): No se halló {a_nombre}")

                        if adjuntos_cont > 0:
                            server.send_message(msg)
                            exitosos += 1
                            time.sleep(delay)
                        else:
                            fallidos.append(f"Fila {index+1} ({destinatario}): Sin archivos válidos.")
                    
                    except Exception as e:
                        fallidos.append(f"Fila {index+1} ({destinatario}): {str(e)}")

                    progreso.progress((index + 1) / len(df))

                server.quit()
                st.success(f"🏁 Proceso completado. Enviados: {exitosos}. Errores: {len(fallidos)}")

                if fallidos:
                    st.warning("Lista de incidencias:")
                    st.write(fallidos)
                    # Opción para descargar log
                    log_text = "\n".join(fallidos)
                    st.download_button("📥 Descargar Reporte de Errores", log_text, file_name="log_errores.txt")

            except Exception as e:
                st.error(f"❌ Error crítico de conexión: {e}")

