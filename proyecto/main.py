import pandas as pd
import smtplib
import os
import time
from email.message import EmailMessage


# --- CONFIGURACIÓN PERSONALIZADA ---
EXCEL_FILE = 'usuarios.xlsx'
FOLDER_ADJUNTOS = './documentos/pediatria'
EMAIL_ORIGEN = "eberrios@savalcorp.com"
EMAIL_PASSWORD = "dqfpkbcjkbpdrvty"
SMTP_SERVER = "smtp.office365.com"  # Servidor oficial de Outlook/O365
SMTP_PORT = 587

def enviar_correos():
    # 1. Validar existencia de carpeta de adjuntos
    if not os.path.exists(FOLDER_ADJUNTOS):
        print(f"❌ Error: No se encuentra la carpeta {FOLDER_ADJUNTOS}")
        return

    # 2. Cargar base de datos
    try:
        df = pd.read_excel(EXCEL_FILE)
    except Exception as e:
        print(f"❌ Error al leer Excel: {e}")
        return
    
    print(f"🚀 Iniciando envío para {len(df)} destinatarios...")

    # 3. Conexión al servidor de Outlook
    try:
        # Outlook requiere SMTP estándar + STARTTLS
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() 
        server.login(EMAIL_ORIGEN, EMAIL_PASSWORD)

        for index, fila in df.iterrows():
            nombre = str(fila['nombre']).strip()
            destinatario = str(fila['correo']).strip()
            representante = str(fila['RPS']).strip()
            materia = str(fila['materia']).strip()
            archivo_nombre = str(fila['archivo solicitado']).strip()

            # 4. Construcción del mensaje
            msg = EmailMessage()
            msg['Subject'] = f"Solicitud de Artículos Científicos Centro SAVAL - {materia}"
            msg['From'] = EMAIL_ORIGEN
            msg['To'] = destinatario
            msg.set_content(f"Estimado(a) doctor(a) {nombre},\n\nJunto con saludarle, de acuerdo a lo solicitado a través de nuestro(a) Representante SAVAL {representante}, envío copia en texto completo de los artículos seleccionados desde el catálogo de artículos científicos para el mes de febrero 2026. \n\nEsperando que el material enviado sea de interés y utilidad, me despido atentamente.")

            # 5. Gestión del adjunto
            ruta_archivo = os.path.join(FOLDER_ADJUNTOS, archivo_nombre)
            
            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'rb') as f:
                    msg.add_attachment(
                        f.read(),
                        maintype='application',
                        subtype='octet-stream',
                        filename=archivo_nombre
                    )
                
                # 6. Envío
                server.send_message(msg)
                print(f"✅ [{index + 1}] Enviado correctamente a: {destinatario}")
                
                # Pausa de seguridad (2 segundos) para evitar bloqueos de Outlook
                time.sleep(2) 
            else:
                print(f"❌ Archivo no encontrado para {nombre}: {archivo_nombre}")

        server.quit()
        print("\n🏁 Proceso de envío finalizado con éxito.")

    except smtplib.SMTPAuthenticationError:
        print("❌ Error: Credenciales rechazadas. Verifica el correo o la clave de aplicación.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    enviar_correos()