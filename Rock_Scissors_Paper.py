from tkinter import *
from PIL import Image,ImageTk
from random import randint, choices

#main win
root= Tk()
root.title("Rock Scissors Paper")                                  
root.configure(background= "purple")                                


piatra_img = ImageTk.PhotoImage(Image.open("piatra.png"))
hartie_img = ImageTk.PhotoImage(Image.open("hartie.png"))
foarfeca_img = ImageTk.PhotoImage(Image.open("foarfeca.png"))

#2pov
piatra_img_comp = ImageTk.PhotoImage(Image.open("piatra_2.png"))
hartie_img_comp = ImageTk.PhotoImage(Image.open("hartie_2.png"))
foarfeca_img_comp = ImageTk.PhotoImage(Image.open("foarfeca_2.png"))


user_label = Label(root, image = piatra_img,bg="purple")                
computer_label = Label(root, image = piatra_img_comp,bg="purple")
computer_label.grid(row=1 , column=0)                                   
user_label.grid(row=1, column =4)                                       


jucatorScor = Label(root,text =0, font =100,bg="purple", fg="white")
computerScor = Label(root, text=0,font =100,bg="purple", fg="white" )
computerScor.grid(row=1,column=1)
jucatorScor.grid(row=1,column=3)

#indicatori
user_indicator = Label(root, font=50, text ="EU",bg="purple", fg="white")
computer_indicator = Label(root, font=50, text="COMPUTER",bg="purple", fg="white")
user_indicator.grid(row=0 , column=3 )
computer_indicator.grid(row=0 , column=1 )

#mesajele
mesaje = Label(root,font =50, bg="purple", fg="white")                    
mesaje.grid(row=3, column=2)


def actualiz_Mesaj(x):
    mesaje ['text'] = x



def actualiz_Iscor():                                                       
     scor = int(jucatorScor["text"])
     scor = scor+ 1
     jucatorScor["text"] = str(scor)



def actualiz_Cscor():                                                        
    scor = int(computerScor["text"])
    scor = scor + 1
    computerScor["text"] = str(scor)



def verif_castigator(jucator, computer):
    if jucator == computer:
        actualiz_Mesaj("Este egalitate!")
    elif jucator == "piatra":
        if computer == "hartie":
            actualiz_Mesaj("Ai pierdut!")
            actualiz_Cscor()
        else:
            actualiz_Mesaj("Ai castigat!")
            actualiz_Iscor()
    elif jucator == "hartie":
        if computer =="foarfeca":
            actualiz_Mesaj("Ai pierdut!")
            actualiz_Cscor()
        else:
            actualiz_Mesaj("Ai castigat!")
            actualiz_Iscor()
    elif jucator == "foarfeca":
        if computer == "piatra":
            actualiz_Mesaj("Ai pierdut!")
            actualiz_Cscor()
        else:
            actualiz_Mesaj("Ai castigat!")
            actualiz_Iscor()
    else:
        pass                                                        



alegere = ["piatra","hartie","foarfeca"]

def realege(x):



    computer = alegere[randint(0, 2)]
    if computer == "piatra":
        computer_label.configure(image=piatra_img_comp)
    elif computer == "hartie":
        computer_label.configure(image=hartie_img_comp)
    else:
        computer_label.configure(image = foarfeca_img_comp)

    if x=="piatra":
        user_label.configure(image=piatra_img)
    elif x=="hartie":
        user_label.configure(image=hartie_img)
    else:
        user_label.configure(image=foarfeca_img)
    verif_castigator(x,computer)


piatra = Button(root,width=20, height=2, text="PIATRA", bg="orange", fg="white",command = lambda:realege("piatra"))
hartie = Button(root,width=20, height=2, text="HARTIE", bg="green", fg="white",command = lambda:realege("hartie"))
foarfeca = Button(root,width=20, height=2, text="FOARFECA", bg="blue", fg="white",command = lambda:realege("foarfeca"))
piatra.grid(row=2,column=1)
hartie.grid(row=2,column=2)
foarfeca.grid(row=2,column=3)



root.mainloop()
