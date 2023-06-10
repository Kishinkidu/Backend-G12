from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
#MIME> multipurpose internet mail extension


def enviarCorreo():
    mensaje = MIMEMultipart()
    #titulo del correo
    mensaje["Subject"] = "Olvidaste la password"
    #Emisor del correo
    mensaje["from"] = "erick@gmail.com"
    #Destinatario del correo
    mensaje["to"] = "yiyomandarin123@gmail.com"
    #cuerpo del correo
    body ="Hola , buenos dias. Al parecer has olvidado tu contraseña, te suguerimos que cambies con els siguiente link"

    texto = MIMEText(body, "plain")

    mensaje.attach(texto)
    #Inicio la conexion con mi cuenta de gmail
    conexion =SMTP("smtp.gmail.com",587)
    conexion.starttls()
    #me autentico con mis credenciales
    conexion.login("erick@gmail.com", "Welcome123!")
    #envio el correo hacia los destianatarios
    conexion.sendmail(from_addr="erick@gmail.com",
                        to_addrs="yiyomandarin123@gmail.com",
                        msg=mensaje.as_string())
    #finalizo la conexion con el servidor de correos
    conexion.quit()

    print("email enviado exitosamente")

enviarCorreo()