#PARA INTERACIAR CON EL SISTEMA OPERATIVO
import os
#OBJETO QUE CREA EL MENSAJE DE CORREO
from email.message import EmailMessage
#CERTIFICADO SSL
import ssl
#PARA ENVIAR EL CORREO
import smtplib
#LIBRERIA PARA MANEJAR ARCHIVOS EN EL CUERPO DEL CORREO
import imghdr

email_emisor = 'CORREO CON EL QUE SE MANDA EL MENSAJE'
email_contrasena = os.environ.get('EMAIL_PASSWORD') #VARIABLE DE ENTORNO ENCARGADA DE GUARDAR LAS CREDENCIALES DEL CORREO EMISOR, EN CASO DE NO TENER VARIABLE DE ENTORNO SE PUEDE PONER AHI LA CONTRASENA

email_receptor = 'CORREO/S QUE RECIBE/N EL MENSAJE'

#CUERPO Y ASUNTO DEL CORREO

asunto = 'Test automatizacion correo'
cuerpo = """
	Test correo
"""

#SE CREA UN OBJETO "em" EL CUAL CONTRENDRA LA INFORMACION DEL CORREO

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

#EN CASO DE AGREGAR ARCHIVOS HAY QUE HACERLO DE LA SIGUIENTE FORMA:

with open('index.jpeg', 'rb') as file:
	file_data = file.read()
	file_type = imghdr.what(file.name)
	file_name = file.name
em.add_attachment(file_data, filename=file_name, subtype=file_type, maintype='image')

#SE BRINDA MAYOR SEGURIDAD AL ENVIO UTILIZANDO UN CERTIFICADO SSL

contexto = ssl.create_default_context()

#ENVIO DEL CORREO:

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
	smtp.login(email_emisor, email_contrasena)
	smtp.sendmail(email_emisor, email_receptor, em.as_string())
