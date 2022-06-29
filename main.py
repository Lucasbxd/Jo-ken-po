from tkinter import *
from PIL import ImageTk
import PIL.Image
from random import randint
from tkinter import messagebox

gray1 = '#252627'
gray2 = '#2e3031'

def finish():
    global app
    global R_img1
    global R_img2
    global R_img3
    global player_choose
    global cpu
    global match
    global R_img4
    global R_img5
    global R_img6
    global R_img7
    global match1

    class label(Label):
        def __init__(self, parent, img):
            super().__init__()
            self['bg'] = gray2
            self['image'] = img
    
    def reset():
        if(match1 < 10):
            match.set('Rodada 0{}'.format(match1))
        else:
            match.set('Rodada {}'.format(match1))
        
        if(status == 'lose'):
            messagebox.showinfo('Partida Finalizada','Você perdeu!')
            app.destroy()
            play()

        fr0_0.destroy()
        fr0_1.destroy()
        fr0_2.destroy()
        lb0_0.destroy()
        lb0_1.destroy()
        lb0_2.destroy()
        lb0_3.destroy()
        lb0_4.destroy()
        lb0_5.destroy()
        lb0_6.destroy()
        lb0_7.destroy()
        bt0_1.destroy()
        print(match1)


        
    fr0_0 = Frame(app, bg=gray1)
    fr0_0.place(x=0, y=50, width=390, height=220)
    fr0_1 = frame(app)
    fr0_1.place(x=4, y=54, width=122, height=122)
    fr0_2 = frame(app)
    fr0_2.place(x=264, y=54, width=122, height=122)

    cpu_choice = ['pedra', 'papel', 'tesoura']
    cpu = cpu_choice[randint(0, 2)]

    R_img4 = ImageTk.PhotoImage(PIL.Image.open('win_off.png').resize((30, 30)))
    R_img5 = ImageTk.PhotoImage(PIL.Image.open('win_on.png').resize((30, 30)))
    R_img6 = ImageTk.PhotoImage(PIL.Image.open('vs.png').resize((100, 97)))
    R_img7 = ImageTk.PhotoImage(PIL.Image.open('proximo.png').resize((20, 20)))

    lb0_3 = Label(app, bg=gray1, image=R_img4)
    lb0_3.place(x=50, y=20)
    lb0_4 = Label(app, bg=gray1, image=R_img4)
    lb0_4.place(x=310, y=20)
    lb0_5 = Label(app, bg=gray1, image=R_img5)

    if player_choose == 'papel' and cpu == 'papel' or player_choose == 'tesoura' and cpu == 'tesoura' or player_choose == 'pedra' and cpu == 'pedra':
        status = 'draw'
    elif player_choose == 'papel' and cpu == 'pedra' or player_choose == 'tesoura' and cpu == 'papel' or player_choose == 'pedra' and cpu == 'tesoura':
        status = 'win'
        match1 += 1
        lb0_5.place(x=50, y=20)
    elif player_choose == 'papel' and cpu == 'tesoura' or player_choose == 'pedra' and cpu == 'papel' or player_choose == 'tesoura' and cpu == 'pedra':
        status = 'lose'
        lb0_5.place(x=310, y=20)

    if player_choose == 'papel':
        image_player = R_img1
    elif player_choose == 'pedra':
        image_player = R_img2
    elif player_choose == 'tesoura':
        image_player = R_img3
    lb0_0 = label(app, image_player)
    lb0_0.place(x=5, y=55, width=120, height=120)

    if cpu == 'papel':
        image_cpu = R_img1
    elif cpu == 'pedra':
        image_cpu = R_img2
    elif cpu == 'tesoura':
        image_cpu = R_img3
    lb0_1 = label(app, image_cpu)
    lb0_1.place(x=265, y=55, width=120, height=120)
    lb0_2 = Label(app, bg=gray1, image=R_img6)
    lb0_2.place(x=140, y=55, width=110, height=120)
    lb0_6 = Label(app, bg=gray1, text='Player', fg='white',font=('Unispace', '15', 'bold'))
    lb0_6.place(x=30, y=180)
    lb0_7 = Label(app, bg=gray1, text='CPU', fg='white', font=('Unispace', '15', 'bold'))
    lb0_7.place(x=310, y=180)

    bt0_1 = Button(app, bg=gray1, fg='white', relief=FLAT, font=('Unispace', '12', 'bold'), image=R_img7, command=reset,compound=LEFT, text=' Continuar', activebackground=gray1, bd=1)
    bt0_1.place(x=130, y=180)

def play():
    global app
    global frame
    global R_img1
    global R_img2
    global R_img3
    global cpu
    global match
    global match1
    match1 = 0
    app = Tk()
    app.geometry('390x220')
    app.resizable(False, False)
    app.title('Jogar')

    class button(Button):
        def __init__(self, parent, img, cmd):
            super().__init__()
            self['bg'] = gray2
            self['relief'] = FLAT
            self['bd'] = 0
            self['image'] = img
            self['activebackground'] = gray2
            self['command'] = cmd

    class frame(Frame):
        def __init__(self, parent):
            super().__init__()
            self['bg'] = 'white'

    def papel():
        global player_choose
        player_choose = 'papel'
        finish()

    def pedra():
        global player_choose
        player_choose = 'pedra'
        finish()

    def tesoura():
        global player_choose
        player_choose = 'tesoura'
        finish()

    fr1 = Frame(app, bg=gray1).place(x=0, y=0, width=390, height=220)
    fr2 = frame(app).place(x=4, y=54, width=122, height=122)
    fr3 = frame(app).place(x=134, y=54, width=122, height=122)
    fr4 = frame(app).place(x=264, y=54, width=122, height=122)

    match = StringVar()
    match.set('Rodada 0{}'.format(match1))
    lb1_1 = Label(app, textvariable=match, bg=gray1, fg='white',font=('Unispace', '20', 'bold')).place(x=130, y=5)
    lb1_2 = Label(app, bg=gray1, text='Papel', fg='white',font=('Unispace', '15', 'bold')).place(x=30, y=180)
    lb1_3 = Label(app, bg=gray1, text='Pedra', fg='white', font=('Unispace', '15', 'bold')).place(x=160, y=180)
    lb1_4 = Label(app, bg=gray1, text='Tesoura', fg='white',font=('Unispace', '15', 'bold')).place(x=280, y=180)

    R_img1 = ImageTk.PhotoImage(PIL.Image.open('papel.png').resize((100, 100)))
    R_img2 = ImageTk.PhotoImage(PIL.Image.open('pedra.png').resize((100, 100)))
    R_img3 = ImageTk.PhotoImage(PIL.Image.open('tesoura.png').resize((100, 100)))

    bt1 = button(app, R_img1, papel).place(x=5, y=55, width=120, height=120)
    bt2 = button(app, R_img2, pedra).place(x=135, y=55, width=120, height=120)
    bt3 = button(app, R_img3, tesoura).place(
        x=265, y=55, width=120, height=120)
    app.mainloop()


play()