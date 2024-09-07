from tkinter import *
from PIL import Image,ImageTk
from random import randint

window = Tk()
window.title("ROCK PAPER PENCIL SCISSOR")
window.configure(width=1000,height=500,background="black")

rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
pencil_img = ImageTk.PhotoImage(Image.open("pencil.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))

player_item = Label(window,bg="black")
player_item.grid(row=1,column=3)
sys_item = Label(window,bg="black")
sys_item.grid(row=1,column=2)

player_img = ImageTk.PhotoImage(Image.open("player.png"))
sys_img = ImageTk.PhotoImage(Image.open("sys.png"))

label_player = Label(window,image=player_img)
label_player.grid(row=1,column=5)
label_sys = Label(window,image=sys_img)
label_sys.grid(row=1,column=0)

sys_score = Label(window,text=0,font=("arial",60,"bold"),bg="white",fg="red")
sys_score.grid(row=1,column=1)
player_score = Label(window,text=0,font=("arial",60,"bold"),bg="white",fg="red")
player_score.grid(row=1,column=4)

final_msg = Label(window,font=("arial",40,"bold"),bg="black",fg="white")
final_msg.grid(row=3,column=2,columnspan=2)

def msg_update(b):
    final_msg['text'] = b

def sys_update():
    final = int(sys_score['text'])
    final += 1
    sys_score['text'] = str(final)

def player_update():
    final = int(player_score['text'])
    final += 1
    player_score['text'] = str(final)

def winner_check(p,c):

    if p == c:
        msg_update("...TIE...")

    elif p == "rock":
        if c == "paper":
            msg_update("System Wins")
            sys_update()
        else:
            msg_update("Player Wins")
            player_update()

    elif p == "paper":
        if c == "rock":
            msg_update("Player Wins")
            player_update()
        else:
            msg_update("System Wins")
            sys_update()

    elif p == "pencil":
        if c == "paper":
            msg_update("Player Wins")
            player_update()
        else:
            msg_update("System Wins")
            sys_update()

    elif p == "scissor":
        if c == "rock":
            msg_update("System Wins")
            sys_update()
        else:
            msg_update("Player Wins")
            player_update()
        
    else:
        pass

def choice_update(a):

    if a == "exit":
        window.quit()

    to_select = ["rock","paper","pencil","scissor"]
    sys_choice = to_select[randint(0,3)]
    
    if sys_choice == "rock":
        sys_item.configure(image=rock_img)
    elif sys_choice == "paper":
        sys_item.configure(image=paper_img)
    elif sys_choice == "pencil":
        sys_item.configure(image=pencil_img)
    else:
        sys_item.configure(image=scissor_img)

    if a == "rock":
        player_item.configure(image=rock_img)
    elif a == "paper":
        player_item.configure(image=paper_img)
    elif a == "pencil":
        player_item.configure(image=pencil_img)
    else:
        player_item.configure(image=scissor_img)

    winner_check(a,sys_choice)


button_rock = Button(window,width=10,height=3,text="ROCK",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:choice_update("rock"))
button_rock.grid(row=2,column=1)
button_paper = Button(window,width=10,height=3,text="PAPER",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:choice_update("paper"))
button_paper.grid(row=2,column=2)
button_scissor = Button(window,width=10,height=3,text="SCISSOR",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:choice_update("scissor"))
button_scissor.grid(row=2,column=3)
button_pencil = Button(window,width=10,height=3,text="PENCIL",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:choice_update("pencil"))
button_pencil.grid(row=2,column=4)

exit_button = Button(window,width=10,height=3,text="CLOSE",font=("arial",20,"bold"),bg="white",fg="red",command=lambda:choice_update("exit"))
exit_button.grid(row=4,column=2,columnspan=2)

window.mainloop()