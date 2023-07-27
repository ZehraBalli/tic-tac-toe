
from tkinter import *#arayüzlü python kütüphanesidir tk.
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" oynuyor"))

            elif check_winner() is True:
                label.config(text=(players[0]+" oyuncusu kazandı"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" oynuyor"))

            elif check_winner() is True:
                label.config(text=(players[1]+" oyuncusu kazandı"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner(): #3 satır ya da sütun eşitse ya da çapraz olarak eşitse mor ve true döndür

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="purple")
            buttons[row][1].config(bg="purple")
            buttons[row][2].config(bg="purple")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="purple")
            buttons[1][column].config(bg="purple")
            buttons[2][column].config(bg="purple")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="purple")
        buttons[1][1].config(bg="purple")
        buttons[2][2].config(bg="purple")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="purple")
        buttons[1][1].config(bg="purple")
        buttons[2][0].config(bg="purple")
        return True

    elif empty_spaces() is False:#boşluk kalmadıysa ve doğru cevap yoksa

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="red")#kırmızı renkle bildiri yapıyoruz
        return "Tie"

    else:
        return False


def empty_spaces():#boşluk işlemleri

    spaces = 9 #boşluk tanımlaması yaptım

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":#satır sütun doldukça spaces 1 azalttık
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def yeni_oyun():

    global player

    player = random.choice(players)

    label.config(text=player+" oyuncusu")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#2F4F4F")#renk kodunu verdik arayüzün


window = Tk()#arayüz için tk kullandım.
window.title("S-O-S")
players = ["s","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " oyuncusu", font=('consolas',30))
label.pack(side="top")

reset_button = Button(text="Yeniden Başla", font=('consolas',15), command=yeni_oyun)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',30), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()#tk olaylarını temizler