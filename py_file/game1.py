import tkinter as tk
from PIL import Image,ImageTk
from random import randint

window = tk.Tk()
window.title("ROCK PAPER PENCIL SCISSOR")
window.configure(width=1000,height=500,background="black")
window.attributes("-fullscreen",True)

frame = tk.Frame(window,bg="black")
frame.place(relx=0.5,rely=0.5,anchor="center")

rock_img = ImageTk.PhotoImage(Image.open("images/rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("images/paper.png"))
pencil_img = ImageTk.PhotoImage(Image.open("images/pencil.png"))
scissor_img = ImageTk.PhotoImage(Image.open("images/scissor.png"))

player_item = tk.Label(frame,bg="black")
sys_item = tk.Label(frame,bg="black")

player_img = ImageTk.PhotoImage(Image.open("images/player.png"))
sys_img = ImageTk.PhotoImage(Image.open("images/sys.png"))

label_player = tk.Label(frame,image=player_img)
label_sys = tk.Label(frame,image=sys_img)

sys_score = tk.Label(frame,text=0,font=("arial",60,"bold"),bg="white",fg="red")
player_score = tk.Label(frame,text=0,font=("arial",60,"bold"),bg="white",fg="red")

final_msg = tk.Label(frame)

nums = 0

def retry():
    final_msg.grid_forget()
    retry_btn.grid_forget()

    game_name.grid(row=0,column=0)
    exit_button.grid(row=2,column=0)
    start_button.grid(row=1,column=0)



def result():
    player_item.grid_forget()
    sys_item.grid_forget()

    label_player.grid_forget()
    label_sys.grid_forget()

    sys_score.grid_forget()
    player_score.grid_forget()

    button_rock.grid_forget()
    button_paper.grid_forget()
    button_pencil.grid_forget()
    button_scissor.grid_forget()

    if int(sys_score['text'])>int(player_score['text']):
        msg_update("System Wins")
    elif int(sys_score['text'])<int(player_score['text']):
        msg_update("Player Wins")
    else:
        msg_update("...TIE...")

    final_msg["width"]=30
    final_msg["height"]=5
    final_msg["font"]=("arial",30,"bold")
    final_msg["bg"]="white"
    final_msg["fg"]="black"
    
    final_msg.grid(row=0,column=0)
    exit_button.grid(row=2,column=0,columnspan=2)
    retry_btn.grid(row=1,column=0,columnspan=2)
    


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
        msg_update("TIE")

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



def choice_update(a):
    global nums
    
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
        nums = nums-1
    elif a == "paper":
        player_item.configure(image=paper_img)
        nums = nums-1
    elif a == "pencil":
        player_item.configure(image=pencil_img)
        nums = nums-1
    else:
        player_item.configure(image=scissor_img)
        nums = nums-1

    winner_check(a,sys_choice)
    if nums==0:
        # window.after(1000)
        button_rock.grid_forget()
        button_paper.grid_forget()
        button_pencil.grid_forget()
        button_scissor.grid_forget()
        exit_button.grid_forget()

        msg_update("...GAME OVER...")
        window.after(2000,result)

def rounds(num):
    global nums
    nums = int(num)
    
    start_button.grid_forget()
    game_name.grid_forget()
    retry_btn.grid_forget()

    rounds_label.grid_forget()
    button_five.grid_forget()
    button_ten.grid_forget()
    button_fifteen.grid_forget()

    player_item.grid(row=1,column=3)
    sys_item.grid(row=1,column=2)
    label_player.grid(row=1,column=5)
    label_sys.grid(row=1,column=0)
    sys_score["text"]="0"
    sys_score.grid(row=1,column=1)
    player_score["text"]="0"
    player_score.grid(row=1,column=4)
    final_msg["text"]=""
    final_msg["width"]=10
    final_msg["height"]=1
    final_msg["font"]=("arial",40,"bold")
    final_msg["bg"]="black"
    final_msg["fg"]="white"
    final_msg.grid(row=3,column=2,columnspan=2)
    button_rock.grid(row=2,column=1)
    button_paper.grid(row=2,column=2)
    button_scissor.grid(row=2,column=4)
    button_pencil.grid(row=2,column=3)
    exit_button.grid(row=4,column=2,columnspan=2)
        

def init():
    rounds_label.grid(row=0,column=0)
    
    button_five.grid(row=1,column=0)
    button_ten.grid(row=2,column=0)
    button_fifteen.grid(row=3,column=0)

    start_button.grid_forget()
    game_name.grid_forget()
    exit_button.grid_forget()
    retry_btn.grid_forget()

rounds_label = tk.Label(frame,width=30,height=3,text="NUMBER OF ROUNDS",font=("arial",30,"bold"),bg="white",fg="black")
    
button_five = tk.Button(frame,width=10,height=3,text="5",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:rounds('5'))
button_ten = tk.Button(frame,width=10,height=3,text="10",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:rounds('10'))
button_fifteen = tk.Button(frame,width=10,height=3,text="15",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:rounds('15'))

button_rock = tk.Button(frame,width=10,height=3,text="ROCK",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:choice_update("rock"))
button_paper = tk.Button(frame,width=10,height=3,text="PAPER",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:choice_update("paper"))
button_scissor = tk.Button(frame,width=10,height=3,text="SCISSOR",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:choice_update("scissor"))
button_pencil = tk.Button(frame,width=10,height=3,text="PENCIL",font=("arial",20,"bold"),bg="yellow",fg="black",command=lambda:choice_update("pencil"))

game_name = tk.Label(frame,width=30,height=5,text="ROCK PAPER PENCIL SCISSOR",font=("arial",30,"bold"),bg="white",fg="black")
game_name.grid(row=0,column=0)
exit_button = tk.Button(frame,width=10,height=3,text="CLOSE",font=("arial",20,"bold"),bg="white",fg="red",command=lambda:choice_update("exit"))
exit_button.grid(row=2,column=0)

start_button = tk.Button(frame,width=10,height=3,text="GO",font=("arial",20,"bold"),bg="white",fg="green",command=lambda:init())
start_button.grid(row=1,column=0)

retry_btn = tk.Button(frame,width=10,height=3,text="RETRY",font=("arial",20,"bold"),bg="white",fg="green",command=lambda:retry())

window.mainloop()