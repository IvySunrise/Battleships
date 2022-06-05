from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
player_1_list = []
player_2_list = []
coordinates_2 = 0
coordinates_1 = 0
number_of_battleship_2_guesses = 0
number_of_battleship_1_guesses = 0
player_2_battleships = 10
player_1_battleships = 10
def start():
    global player_co
    global tab1
    global x
    tab1 = Tk()
    tab1.geometry("240x90")
    tab1.title("coordinate form 1")
    player_co = ttk.Entry(tab1, text = "Co-ordinate")
    player_co.place(relx = 0.5,rely = 0.1,anchor = 'center')
    player_co.pack()
    nice_button = ttk.Button(tab1, text = 'Submit!', command=submit_value)
    nice_button.place(relx = 0.5, rely = 0.5,anchor = 'center')
    root.destroy()
def submit_value():
    global player_1_list
    global coordinates_2
    player_1_list.append(player_co.get())
    coordinates_2 = coordinates_2 + 1
    if coordinates_2 == 10:
        hehe()
def submit_value_2():
    global player_2_list
    global coordinates_1
    player_2_list.append(player_co_2.get())
    coordinates_1 = coordinates_1 + 1
    if coordinates_1 == 10:
        battleships_1_arena()
def woo():
    print("Woo!")
def results_screen():
    tab4.destroy()
    tab5 = Tk()
    tab5.geometry("640x480")
    trophy = ImageTk.PhotoImage(Image.open('battleship.png'))
    nice_button = ttk.Button(tab5, text = 'Click Me !', image=trophy, command=woo)
    nice_button.place(relx = 0.5, rely = 0.5,anchor = 'center')
    if player_1_battleships > player_2_battleships:
        Label = ttk.Label(tab5,text ='Player 1 wins')
        Label.place(relx = 0.5,rely = 0.1,anchor = 'center')
    elif player_2_battleships > player_1_battleships:
        Label = ttk.Label(tab5,text ='Player 2 wins')
        Label.place(relx = 0.5,rely = 0.1,anchor = 'center')
    else:
        Label = ttk.Label(tab5,text ='Draw!')
        Label.place(relx = 0.5,rely = 0.1,anchor = 'center')
def destroy_player_2():
    global player_1_battleships
    global number_of_battleship_1_guesses
    input_ = player_guess_2.get()
    if input_ in player_1_list:
            print("WOOOO! You shot down a battleship!")
            player_1_list.remove(player_guess_2.get())
            player_1_battleships = player_1_battleships - 1
    else:
        print("Keep trying")
    number_of_battleship_1_guesses = number_of_battleship_1_guesses + 1
    if number_of_battleship_1_guesses == 10:
        print("Results time!")
        results_screen()
def destroy_player_1():
    global player_2_battleships
    global number_of_battleship_2_guesses
    input_ = player_guess.get()
    if input_ in player_2_list:
        print("WOOOO! You shot down a battleship!")
        player_2_list.remove(player_guess.get())
        player_2_battleships = player_2_battleships - 1
    else:
        print("Keep trying")
    number_of_battleship_2_guesses = number_of_battleship_2_guesses + 1
    if number_of_battleship_2_guesses == 10:
        battleships_2_arena()
        tab3.destroy()
def battleships_2_arena():
    global tab4
    global player_guess_2
    tab4 = Tk()
    print("Switch over! Player 2's turn!")
    tab4.geometry("240x90")
    tab4.title("coordinate decimator 2")
    player_guess_2 = ttk.Entry(tab4, text = "Mwahaha")
    player_guess_2.place(relx = 0.5,rely = 0.1,anchor = 'center')
    player_guess_2.pack()
    nice_button = ttk.Button(tab4, text = 'Submit!', command=destroy_player_2)
    nice_button.place(relx = 0.5, rely = 0.5,anchor = 'center')
def battleships_1_arena():
    global player_guess
    global tab3
    tab3 = Tk()
    tab3.geometry("240x90")
    tab3.title("coordinate decimator 1")
    player_guess = ttk.Entry(tab3, text = "Mwahaha")
    player_guess.place(relx = 0.5,rely = 0.1,anchor = 'center')
    player_guess.pack()
    nice_button = ttk.Button(tab3, text = 'Submit!', command=destroy_player_1)
    nice_button.place(relx = 0.5, rely = 0.5,anchor = 'center')
    tab2.destroy()
def hehe():
    global player_co_2
    global tab2
    tab2 = Tk()
    tab2.geometry("240x90")
    tab2.title("coordinate form 2")
    player_co_2 = ttk.Entry(tab2, text = "Co-ordinate")
    player_co_2.place(relx = 0.5,rely = 0.1,anchor = 'center')
    player_co_2.pack()
    nice_button = ttk.Button(tab2, text = 'Submit!', command=submit_value_2)
    nice_button.place(relx = 0.5, rely = 0.5,anchor = 'center')
    tab1.destroy()
root = Tk()
frm = ttk.Frame(root, padding=10)
root.geometry("640x480")
frm.grid()
Label_middle = ttk.Label(root,text ='Welcome to Battleships, click the boat to start')
Label_middle.place(relx = 0.5,rely = 0.1,anchor = 'center')
battleship=PhotoImage(file='battleship.png')
nice_button = ttk.Button(root, text = 'Click Me !', image = battleship, command=start)
nice_button.place(relx = 0.5, rely = 0.5,anchor = 'center')
root.mainloop()
