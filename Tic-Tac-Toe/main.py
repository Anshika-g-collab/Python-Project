from tkinter import *
root = Tk()
root.geometry("600x600")
root.title("Tic-Tac-Toe")
root.resizable(0,0)
frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1,text="Tic-Tac-Toe" , font=("Arial",23),bg="lightblue",width=50)
titleLabel.pack()

optionFrame=Frame(root,bg="grey")
optionFrame.pack()



frame2 = Frame(root)
frame2.pack()

board = {
    1: " ",2:" ",3:" ",
    4: " ",5:" ",6:" ",
    7: " ",8:" ",9:" ",
}
    
turn="X" 
game_end=False
mode = "singlePlayer"
def changeModeToSingle():
     global mode
     mode = "singlePlayer"
     aibutton["bg"]="orange"
     multibutton["bg"]="grey"
def changeModeToMulti():
    global mode
    mode = "multiPlayer"
    multibutton["bg"]="orange"
    aibutton["bg"]="grey"
def updateBoard():
    for key in board.keys():
        buttons[key-1]["text"] = board[key]

def checkForWin(player):
    #rows

    if board[1]==board[2] and board[2]==board[3] and board[3]==player: # initially all will be equal as they are empty
        return True

    elif board[4]==board[5] and board[5]==board[6] and board[6]==player: 
            return True

    elif board[7]==board[8] and board[8]==board[9] and board[9]==player: 
            return True
#columns
    elif board[1]==board[4] and board[4]==board[7] and board[7]==player: 
            return True

    elif board[2]==board[5] and board[5]==board[8] and board[8]==player: 
            return True

    elif board[3]==board[6] and board[6]==board[9] and board[9]==player: 
            return True
#diagonals
    elif board[1]==board[5] and board[5]==board[9] and board[9]==player: 
            return True

    elif board[3]==board[5] and board[5]==board[7] and board[7]==player: 
            return True
    return False
def restartGame():
    global game_end 
    game_end= False
    for button in buttons:
        button["text"]=" "

    for i in board.keys():
        board[i]=" "
    winningLabel = Label(frame2,text="",bg="beige",font=("arial",20),width=15)
    winningLabel.grid(row=3,column=0,columnspan=3)
    drawLabel = Label(frame2,text="",bg="beige",font=("arial",20),width=15)
    drawLabel.grid(row=3,column=0,columnspan=3)
def checkForDraw():
    for i in board.keys():
        if board[i]==" ":
            return False
    return True
def play(event):
    global turn,game_end #global variable ki value function k sndr change nhi kr skte, therefre wriring this statement.
    if game_end:
        return
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    
    if clicked=="n":
        clicked=1
    else:
        clicked = int(clicked)
    if button["text"]==" ":#to not overwrite
        if turn=="X":
            
            board[clicked]=turn
            if checkForWin(turn):
                winningLabel = Label(frame2,text=f"{turn} wins the game!!!",bg="Orange",font=("Arial",20))
                winningLabel.grid(row=3,column=0,columnspan=3)
                game_end=True
            elif checkForDraw():
                drawLabel = Label(frame2,text=f" OOPS!!! It's a Draw .",bg="Orange",font=("Arial",17))
                drawLabel.grid(row=3,column=0,columnspan=3)
                game_end=True

            turn="O"
            if mode=="singlePlayer":
                    playComputer()
                    if checkForWin(turn):
                        winningLabel = Label(frame2,text=f"{turn} wins the game!!!",bg="Orange",font=("Arial",20))
                        winningLabel.grid(row=3,column=0,columnspan=3)
                        game_end=True
                    turn="X"
                    updateBoard()
            
        else:
            button["text"] = "O"
            board[clicked]=turn
            if checkForWin(turn):
                winningLabel = Label(frame2,text=f"{turn} wins the game!!!",bg="Orange",font=("Arial",20))
                winningLabel.grid(row=3,column=0,columnspan=3)
                game_end=True
                
            elif checkForDraw():
                drawLabel = Label(frame2,text=f" OOPS!!! It's a Draw .",bg="Orange",font=("Arial",17))
                drawLabel.grid(row=3,column=0,columnspan=3)
                game_end=True
            turn="X"
        updateBoard()  

def minimax(board,isMaximising):
    if checkForWin("O"):
        return 1
    if checkForWin("X"):
        return -1
    if checkForDraw():
        return 0
    if isMaximising:
        bestScore = -100
        for key in board.keys():
            if board[key]==" ":
                board[key]="O"
                score = minimax(board,False)
                board[key]=" "
                if score>bestScore:
                    bestScore = score
        return bestScore   
    else:
        bestScore = 100
        for key in board.keys():
            if board[key]==" ":
                board[key]="X"
                score = minimax(board,True)
                board[key]=" "
                if score<bestScore:
                    bestScore = score
        return bestScore  
def playComputer():
    bestScore = -100
    bestMove = 0

    for key in board.keys():
        if board[key]==" ":
            board[key]="O"
            score = minimax(board,False)
            board[key]=" "
            if score>bestScore:
                bestScore = score
                bestMove=key
    board[bestMove]="O"

# ---------UI--------
#change mode options
aibutton = Button(optionFrame,text="singlePlayer",width=21,height=1,font=("arial",18),bg = "grey",borderwidth=5,command=changeModeToSingle)
aibutton.grid(row=0,column=0,columnspan=1,sticky=NW)

multibutton = Button(optionFrame,text="Multiplayer",width=21,height=1,font=("arial",18),bg = "grey",borderwidth=5,command=changeModeToMulti)
multibutton.grid(row=0,column=1,columnspan=1,sticky=NW)


# TTT board  ------- UI
# first row
button1 = Button(frame2,text=" ",width=4,height=2,font=("arial",32),bg = "lightpink",relief=RAISED,borderwidth=4)
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button2 = Button(frame2,text=" ",width=4,height=2,font=("arial",32),bg = "lightpink",relief=RAISED,borderwidth=4)
button2.grid(row=0,column=1)
button2.bind("<Button-1>",play)

button3 = Button(frame2,text=" ",width=4,height=2,font=("arial",32),bg = "lightpink",relief=RAISED,borderwidth=4)
button3.grid(row=0,column=2)
button3.bind("<Button-1>",play)

# second row
button4 = Button(frame2,text=" ",width=4,height=2,font=("arial",32),bg = "lightpink",relief=RAISED,borderwidth=4)
button4.grid(row=1,column=0)
button4.bind("<Button-1>",play)

button5 = Button(frame2,text=" ",width=4,height=2,font=("arial",32),bg = "lightpink",relief=RAISED,borderwidth=4)
button5.grid(row=1,column=1)
button5.bind("<Button-1>",play)

button6 = Button(frame2,text=" ",width=4,height=2,font=("arial",32),bg = "lightpink",relief=RAISED,borderwidth=4)
button6.grid(row=1,column=2)
button6.bind("<Button-1>",play)

# third row
button7 = Button(frame2,text=" ",width=4,height=2,font=("arial",32),bg = "lightpink",relief=RAISED,borderwidth=4)
button7.grid(row=2,column=0)
button7.bind("<Button-1>",play)

button8 = Button(frame2,text=" ",width=4,height=2,font=("arial",32),bg = "lightpink",relief=RAISED,borderwidth=4)
button8.grid(row=2,column=1)
button8.bind("<Button-1>",play)

button9 = Button(frame2,text=" ",width=4,height=2,font=("arial",32),bg = "lightpink",relief=RAISED,borderwidth=4)
button9.grid(row=2,column=2)
button9.bind("<Button-1>",play)



restartbutton = Button(frame2,text="Restart Game",width=12,height=1,font=("arial",18),bg = "lightgreen",relief=RAISED,borderwidth=4,command=restartGame)
restartbutton.grid(row=4,column=0,columnspan=3)

buttons =[button1,button2,button3,button4,button5,button6,button7,button8,button9]




root.mainloop()