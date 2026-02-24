import tkinter,random,tkinter.messagebox
bg=tkinter.Tk()
plscore=0

options=["rock","paper","scissors"]
def button_pressed(userselected):
    print(userselected)
    global plscore
    comp=random.choice(options)
    if comp=="rock" and userselected=="paper":
        tkinter.messagebox.showinfo(("Results"),"you win I picked rock and you chose paper!!!!!!!!!!")
        plscore=plscore+1
    elif comp=="rock" and userselected=="scissors":
        tkinter.messagebox.showinfo(("Results"),"I win i chose rock and you chose paper!!!!!!!!!!")
        plscore=plscore-1
    elif comp==userselected:
        tkinter.messagebox.showinfo(("Results"),"tie!!!!!!!!!!")
        plscore=plscore+1
    elif comp=="paper" and userselected=="rock":
        tkinter.messagebox.showinfo(("Results"),"i win I picked paper and you chose rock!!!!!!!!!!")
        plscore=plscore-1
    elif comp=="paper" and userselected=="scissors":
        tkinter.messagebox.showinfo(("Results"),"you win I picked paper and you chose scissors!!!!!!!!!!")
        plscore=plscore+2
    elif comp=="scissors" and userselected=="rock":
        tkinter.messagebox.showinfo(("Results"),"you win I picked scissors and you chose rock!!!!!!!!!!")
        plscore=plscore+2
    elif comp=="scissors" and userselected=="paper":
        tkinter.messagebox.showinfo(("Results"),"i win I picked scissors and you chose paper!!!!!!!!!!")
        plscore=plscore-1
    sco.config(text=str(plscore))
lab1=tkinter.Label(bg,text="rock   paper   scissors",bg="orange",font=("comic Sans MS",50,"italic"))
lab1.grid(row=1,column=1)
rock=tkinter.Button(bg,text="rock",bg="grey",command=lambda:button_pressed("rock"),font=("comic Sans MS",50,"italic"))
rock.grid(row=2,column=2)
paper=tkinter.Button(bg,text="paper",bg="blue",command=lambda:button_pressed("paper"),font=("comic Sans MS",50,"italic"))
paper.grid(row=2,column=3)
scissors=tkinter.Button(bg,text="scissors",bg="red",command=lambda:button_pressed("scissors"),font=("comic Sans MS",50,"italic"))
scissors.grid(row=2,column=4)
sco=tkinter.Label(bg,text=plscore,bg="orange",font=("comic Sans MS",50,"italic"))
sco.grid(row=1,column=2)


bg.mainloop()
