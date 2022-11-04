from tkinter import *
import smtplib as mail

root = Tk()

root.title("Correo electronico")


def enviar():
    try:
        username = usuario.get()
        password = contra.get()
        to = destino.get()
        subject = asunto.get()
        body = cuerpo.get()
        if (username == "" or password == "" or to =="" or subject == "" or body == ""):
            alert.config(text="Debe llenar todos los campos")
        else:
            mensajeFinal =f"""
            subjet: {subject}

            Body: {body}
            
            """
            server = mail.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to, mensajeFinal)
            alert.config(text="El mensaje fue enviado exitosamente", fg ="blue")
    except Exception as e:
        alert.config(text=" Error al envier mensaje ", fg="red")
        print(e)
        pass

def borrar():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    
    alert.destroy()

Label(root, text="Enviar correo", font=("Roboto", 15)).grid(row=0, sticky= N)
Label(root, text="Llena el formulario", font=("Roboto", 11)).grid(row=1, sticky=W, padx=5, pady=10)
Label(root, text="Correo: ", font=("Roboto", 11)).grid(row=2, sticky=W, padx=5)
Label(root, text="Contraseña:", font=("Roboto", 11)).grid(row=3, sticky=W,padx=5)
Label(root, text="Para:", font=("Roboto", 11)).grid(row=4, sticky=W, padx=5)
Label(root, text="Asunto:", font=("Roboto", 11)).grid(row=5, sticky=W, padx=5)
Label(root, text="Cuerpo: ", font=("Roboto", 11)).grid(row=6, sticky=W, padx=5)

alert = Label(root, text="", font=("Roboto", 11), fg="red")
alert.grid(row=9, sticky=S)

usuario = StringVar()
contra = StringVar()
destino = StringVar()
asunto = StringVar()
cuerpo = StringVar()

entry1 = Entry(root, textvariable=usuario)
entry1.grid(row=2, column=1)

entry2 = Entry(root, textvariable=contra, show="*")
entry2.grid(row=3, column=1)

entry3 = Entry(root, textvariable=destino)
entry3.grid(row=4, column=1)

entry4 = Entry(root, textvariable=asunto)
entry4.grid(row=5, column=1)

entry5 = Entry(root, textvariable=cuerpo)
entry5.grid(row=6, column=1)


Button(root, command= enviar, text ="Enviar").grid(row=8, sticky=W,pady=15, padx=25)
Button(root, command=borrar, text="Borrar").grid(row=8, column=1)

root.mainloop()