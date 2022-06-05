#19

from tkinter import * 
from tkinter import messagebox
import random

player = random.choice(['o' , 'x'])
color = {'o' : 'black' , 'x' : 'red'}
board = [[] , [] , []]

def clear():
    global player
    global board
    for i in range (3):
        for j in range (3):
            board[i][j]['text']==''
            board[i][j]['state']==NORMAL
    player= random.choice(['o' ,'x'])

def click(row , col):
    global player 
    global color 
    global board
    board[row][col].config(text=player , state =DISABLED ,disabledforeground=color[player])
    for i in range(3):
        if(board[i][0]['text']==board[i][1]['text']==board[i][2]['text']==player
           or board[0][i]['text']==board[1][i]['text']==board[2][i]['text']==player):
           messagebox.showinfo('Success', player + ' has won')
           clear()
        
        if (board[0][0]['text']==board[1][1]['text']==board[2][2]['text']==player
            or board[0][2]['text']==board[1][1]['text']==board[2][0]['text']==player):
            messagebox.showinfo('Success', player +'has won')
            clear()
        elif(board[0][0]['state']==board[0][1]['state']==board[0][2]['state']==DISABLED
             and board[1][0]['state']==board[1][1]['state']==board[1][2]['state']==DISABLED
             and board[2][0]['state']==board[2][1]['state']==board[2][2]['state']==DISABLED):
             messagebox.showinfo('same result', 'nobody has won')
             clear()
             
             
             
    if  player == 'x':
        player ='o'
    else :
        player = 'x'
    turn.config(text=player+'s turn')


tkwindow = Tk()
tkwindow.title('tic toc toe game')

button1 = Button(tkwindow , text ='' , font = 'times 20 bold'  , height=3 , width=6 , command=lambda : click(0,0))
button1.grid(row=0, column=0)
board[0].append(button1)


button2 = Button(tkwindow , text ='' , font = 'times 20 bold'  , height=3 , width=6 , command=lambda : click(0,1))
button2.grid(row=0, column=1)
board[0].append(button2)


button3 = Button(tkwindow , text ='' , font = 'times 20 bold'  , height=3 , width=6 , command=lambda : click(0,2))
button3.grid(row=0, column=2)
board[0].append(button3)


button4 = Button(tkwindow , text ='' , font = 'times 20 bold'  , height=3 , width=6 , command=lambda : click(1,0))
button4.grid(row=1, column=0)
board[1].append(button4)

button5 = Button(tkwindow , text ='' , font = 'times 20 bold'  , height=3 , width=6 , command=lambda : click(1,1))
button5.grid(row=1, column=1)
board[1].append(button5)

button6 = Button(tkwindow , text ='' , font = 'times 20 bold' ,  height=3 , width=6 , command=lambda : click(1,2))
button6.grid(row=1, column=2)
board[1].append(button6)

button7 = Button(tkwindow , text ='' , font = 'times 20 bold'  , height=3 , width=6 , command=lambda : click(2,0))
button7.grid(row=2, column=0)
board[2].append(button7)

button8 = Button(tkwindow , text ='' , font = 'times 20 bold'  , height=3 , width=6 , command=lambda : click(2,1))
button8.grid(row=2, column=1)
board[2].append(button8)

button9 = Button(tkwindow , text ='' , font = 'times 20 bold'  , height=3 , width=6 , command=lambda : click(2,2))
button9.grid(row=2, column=2)
board[2].append(button9)

turn = Label(tkwindow , text = player + 's turn' , font = ' Times 20 bold')
turn.grid(row = 3 , column = 0 , columnspan=3)

tkwindow.mainloop()