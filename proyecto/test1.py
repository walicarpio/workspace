#Basado en archivo padre 'main2.py'

import pandas as pd
import smtplib
import os
import time
from email.message import EmailMessage
from datetime import datetime
from main import EMAIL_ORIGEN

# --- CONFIGURACIÓN ---
EXCEL_FILE = 'usuarios.xlsx'
FOLDER_ADJUNTOS = './documentos/pediatria'
EMAIL_PRINCIPAL = "eberrios@savalcorp.com" 
EMAIL_PASSWORD = "dqfpkbcjkbpdrvty" 
CASILLA_COMPARTIDA = "calvomackenna@savalcorp.com" 
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587

def enviar_correos():
    if not os.path.exists(FOLDER_ADJUNTOS):
        print(f"❌ Carpeta no encontrada: {FOLDER_ADJUNTOS}")
        return

    try:
        df = pd.read_excel(EXCEL_FILE)
    except Exception as e:
        print(f"❌ Error al leer Excel: {e}")
        return

    fallidos = []
    print(f"🚀 Iniciando envío múltiple desde {CASILLA_COMPARTIDA}...")

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() 
        server.login(EMAIL_PRINCIPAL, EMAIL_PASSWORD)

        for index, fila in df.iterrows():
            nombre = str(fila['nombre']).strip()
            destinatario = str(fila['correo']).strip()
            representante = str(fila['RPS']).strip()
            materia = str(fila['materia']).strip()
            archivo_nombre = str(fila['archivo solicitado']).strip()
            
            # --- LÓGICA PARA MÚLTIPLES ARCHIVOS ---
            # Separamos los nombres por coma y limpiamos espacios
            lista_archivos = [a.strip() for a in str(fila['archivo solicitado']).split(',')]
            
             # 4. Construcción del mensaje
            msg = EmailMessage()
            msg['Subject'] = f"Solicitud de Artículos Científicos Centro SAVAL - {materia}"
            msg['From'] = CASILLA_COMPARTIDA
            msg['To'] = destinatario
            msg.set_content(f"Estimado(a) doctor(a) {nombre},\n\nJunto con saludarle, de acuerdo a lo solicitado a través de nuestro(a) Representante SAVAL {representante}, envío copia en texto completo de los artículos seleccionados desde el catálogo de artículos científicos para el mes de febrero 2026. \n\nEsperando que el material enviado sea de interés y utilidad, me despido atentamente.")

            archivos_adjuntados_con_exito = 0

            for archivo_nombre in lista_archivos:
                    ruta_archivo = os.path.join(FOLDER_ADJUNTOS, archivo_nombre)
                    
                    if os.path.exists(ruta_archivo):
                        with open(ruta_archivo, 'rb') as f:
                            msg.add_attachment(
                                f.read(), 
                                maintype='application', 
                                subtype='octet-stream', 
                                filename=archivo_nombre
                            )
                        archivos_adjuntados_con_exito += 1
                    else:
                        print(f"⚠️ Archivo no encontrado: {archivo_nombre}")
                        fallidos.append(f"Fila {index+1}: No se encontró {archivo_nombre}")

                # Solo enviamos si logramos adjuntar al menos uno (o según tu preferencia)
            if archivos_adjuntados_con_exito > 0:
                    server.send_message(msg)
                    print(f"✅ [{index + 1}] Enviado a {destinatario} ({archivos_adjuntados_con_exito} archivos)")
                    time.sleep(3)
            else:
                    raise FileNotFoundError("No se pudo adjuntar ningún archivo de la lista.")

    except Exception as e:
                error_msg = f"Fila {index + 1} ({destinatario}): {str(e)}"
                print(f"⚠️ Error: {error_msg}")
                fallidos.append(error_msg)

    server.quit()

    if fallidos:
            with open("log_errores.txt", "w", encoding="utf-8") as f:
                f.write(f"REPORTE DE ERRORES - {datetime.now()}\n\n")
                for error in fallidos: f.write(error + "\n")
            print(f"\n📢 Proceso con advertencias. Revisar 'log_errores.txt'.")
    else:
            print("\n🏁 ¡Éxito! Todos los correos y sus archivos fueron enviados.")

if __name__ == "__main__":
    enviar_correos()