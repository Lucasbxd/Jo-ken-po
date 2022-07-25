from tkinter import *
from PIL import ImageTk
import PIL.Image
from random import randint
from tkinter import messagebox
from operator import itemgetter, attrgetter


gray1 = '#252627'
gray2 = '#2e3031'

def center_window(width, height):
    global app
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    app.geometry('%dx%d+%d+%d' % (width, height, x, y))

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
    global name_player

    class label(Label):
        def __init__(self, parent, img):
            super().__init__()
            self['bg'] = gray2
            self['image'] = img

    def reset():
        match.set('Pontos: {}'.format(match1))
        if(status == 'lose'):
            arq = open('./config/ranking.txt','a')
            arq.write('{},{}\n'.format(name_player,match1))
            arq.close()
            messagebox.showinfo('Partida Finalizada', 'Você perdeu!\nPontuação: {}'.format(match1))
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

    fr0_0 = Frame(app, bg=gray1)
    fr0_0.place(x=0, y=50, width=390, height=220)
    fr0_1 = frame(app)
    fr0_1.place(x=4, y=54, width=122, height=122)
    fr0_2 = frame(app)
    fr0_2.place(x=264, y=54, width=122, height=122)

    cpu_choice = ['pedra', 'papel', 'tesoura']
    cpu = cpu_choice[randint(0, 2)]

    R_img4 = ImageTk.PhotoImage(PIL.Image.open('./img/win_off.png').resize((30, 30)))
    R_img5 = ImageTk.PhotoImage(PIL.Image.open('./img/win_on.png').resize((30, 30)))
    R_img6 = ImageTk.PhotoImage(PIL.Image.open('./img/vs.png').resize((100, 97)))
    R_img7 = ImageTk.PhotoImage(PIL.Image.open('./img/proximo.png').resize((20, 20)))

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
    lb0_7 = Label(app, bg=gray1, text='CPU', fg='white',font=('Unispace', '15', 'bold'))
    lb0_7.place(x=310, y=180)

    bt0_1 = Button(app, bg=gray1, fg='white', relief=RIDGE,font=('Unispace', '12', 'bold'),image=R_img7, command=reset, compound=LEFT, text=' Avançar', activebackground=gray1, bd=2)
    #bt0_1.place(x=130, y=180)
    bt0_1.place(x=142, y=180)

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
    center_window(390,220)
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
    
    def home():
        app.destroy()
        menu()

    fr1 = Frame(app, bg=gray1).place(x=0, y=0, width=390, height=220)
    fr2 = frame(app).place(x=4, y=54, width=122, height=122)
    fr3 = frame(app).place(x=134, y=54, width=122, height=122)
    fr4 = frame(app).place(x=264, y=54, width=122, height=122)

    match = StringVar()
    match.set('Pontos: {}'.format(match1))
    lb1_1 = Label(app, textvariable=match, bg=gray1, fg='white', font=('Unispace', '15', 'bold')).place(x=130, y=10)
    lb1_2 = Label(app, bg=gray1, text='Papel', fg='white', font=('Unispace', '15', 'bold')).place(x=30, y=180)
    lb1_3 = Label(app, bg=gray1, text='Pedra', fg='white', font=( 'Unispace', '15', 'bold')).place(x=160, y=180)
    lb1_4 = Label(app, bg=gray1, text='Tesoura', fg='white', font=('Unispace', '15', 'bold')).place(x=280, y=180)

    R_img1 = ImageTk.PhotoImage(PIL.Image.open('./img/papel.png').resize((100, 100)))
    R_img2 = ImageTk.PhotoImage(PIL.Image.open('./img/pedra.png').resize((100, 100)))
    R_img3 = ImageTk.PhotoImage(PIL.Image.open('./img/tesoura.png').resize((100, 100)))
    R_img8 = ImageTk.PhotoImage(PIL.Image.open('./img/home.png').resize((20, 20)))

    bt1 = button(app, R_img1, papel).place(x=5, y=55, width=120, height=120)
    bt2 = button(app, R_img2, pedra).place(x=135, y=55, width=120, height=120)
    bt3 = button(app, R_img3, tesoura).place(x=265, y=55, width=120, height=120)
    bt4 = button(app, R_img8, home).place(x=0, y=0)
    app.mainloop()

def menu():
    global app
    global tx1
    app = Tk()
    center_window(390,220)
    app.resizable(False, False)
    app.title('Menu')

    fr1 = Frame(app, bg=gray1).place(x=0, y=0, width=390, height=220)
    fr2 = Frame(app, bg=gray2).place(x=0, y=0, width=390, height=40)
    lb1 = Label(app, text='Jogo da velha', bg=gray2, fg='white',font=('Unispace', '12', 'bold')).place(x=120, y=10)
    lb2 = Label(app, text='Seu Nome: ', bg=gray1, fg='white',font=('Unispace', '12', 'bold')).place(x=80, y=60)

    def play_choose():
        global name_player
        if tx1.get() != '':
            name_player = tx1.get()
            app.destroy()
            play()
        else:
            messagebox.showerror('Campo de nome vazio','Digite um Nome para jogar.')

    def ranking():
        global frame
        global R_img0_0
        global R_img0_1
        global R_img0_2
        global R_img0_3

        class label1(Label):
            def __init__(self, parent, text):
                super().__init__()
                self['bg'] = gray2
                self['fg'] = 'white'
                self['font'] = ('Unispace', '12', 'bold')
                self['textvariable'] = text

        class ranking():
            def __init__(self, name, point):
                self.name = name
                self.point = point

            def __repr__(self):
                return '{},{}'.format(self.name,self.point)
        
        def reset_ranking():
            
            fr1_1.destroy()
            fr2_1.destroy()
            fr3.destroy()
            fr4.destroy()
            fr5.destroy()
            fr6.destroy()
            fr7.destroy()
            fr8.destroy()
            lb0_0.destroy()
            lb0_1.destroy()
            lb0_2.destroy()
            lb0_3.destroy()
            lb0_4.destroy()
            lb0_5.destroy()
            lb1_1.destroy()
            lb1_2.destroy()
            lb1_3.destroy()
            lb1_4.destroy()
            lb1_5.destroy()
            lb2_1.destroy()
            lb2_2.destroy()
            lb2_3.destroy()
            lb2_4.destroy()
            lb2_5.destroy()
            bt0_1.destroy()

        R_img0_0 = ImageTk.PhotoImage(PIL.Image.open('./img/primeiro.png').resize((40, 40)))
        R_img0_1 = ImageTk.PhotoImage(PIL.Image.open('./img/segundo.png').resize((40, 40)))
        R_img0_2 = ImageTk.PhotoImage(PIL.Image.open('./img/terceiro.png').resize((40, 40)))
        R_img0_3 = ImageTk.PhotoImage(PIL.Image.open('./img/replay.png').resize((20, 20)))

        
        fr1_1 = Frame(app, bg=gray1)
        fr1_1.place(x=0, y=0, width=390, height=220)
        fr2_1 = Frame(app, bg=gray2)
        fr2_1.place(x=0, y=0, width=390, height=40)
        fr3 = Frame(app, bg='white')
        fr3.place(x=4, y=54, width=122, height=122)
        fr4 = Frame(app, bg='white')
        fr4.place(x=134, y=54, width=122, height=122)
        fr5 = Frame(app, bg='white')
        fr5.place(x=264, y=54, width=122, height=122)
        fr6 = Frame(app, bg=gray2)
        fr6.place(x=5, y=55, width=120, height=120)
        fr7 = Frame(app, bg=gray2)
        fr7.place(x=135, y=55, width=120, height=120)
        fr8 = Frame(app, bg=gray2)
        fr8.place(x=265, y=55, width=120, height=120)

        lb0_0 = Label(app, text='As três melhores colocações', bg=gray2, fg='white',font=('Unispace', '12', 'bold'))
        lb0_0.place(x=55, y=10)

        name = StringVar()
        name.set('Nome:')

        point = StringVar()
        point.set('Pontos:')

        name1 = StringVar()
        name2 = StringVar()
        name3 = StringVar()

        point1 = IntVar()
        point2 = IntVar()
        point3 = IntVar()

        list_ranking = []
        arq = open('./config/ranking.txt').readlines()

        if len(arq) > 2:
            for line in arq:
                list_ranking.append(ranking(line.split(',')[0], int(line.split(',')[1].rstrip())))
            list_ranking = sorted(
                list_ranking, key=attrgetter('point'), reverse=True)

            first = str(list_ranking[0])
            second = str(list_ranking[1])
            third = str(list_ranking[2])

            name1.set(first.split(',')[0])
            point1.set(first.split(',')[1])

            name2.set(second.split(',')[0])
            point2.set(second.split(',')[1])

            name3.set(third.split(',')[0])
            point3.set(third.split(',')[1])
        
        else:
            name1.set('S/N')
            point1.set(0)

            name2.set('S/N')
            point2.set(0)

            name3.set('S/N')
            point3.set(0)
        
        lb0_1 = label1(app, name)
        lb0_1.place(x=10, y=60)
        lb0_2 = label1(app, name1)
        lb0_2.place(x=10, y=82)
        lb0_3 = label1(app, point)
        lb0_3.place(x=10, y=105)
        lb0_4 = label1(app, point1)
        lb0_4.place(x=85, y=105)
        lb0_5 = Label(app, bg=gray2, image=R_img0_0)
        lb0_5.place(x=42, y=131)
        
        lb1_1 = label1(app, name)
        lb1_1.place(x=140, y=60)
        lb1_2 = label1(app, name2)
        lb1_2.place(x=140, y=82)
        lb1_3 = label1(app, point)
        lb1_3.place(x=140, y=105)
        lb1_4 = label1(app, point2)
        lb1_4.place(x=215, y=105)
        lb1_5 = Label(app, bg=gray2, image=R_img0_1)
        lb1_5.place(x=175, y=131)
                
        lb2_1 = label1(app, name)
        lb2_1.place(x=270, y=60)
        lb2_2 = label1(app, name3)
        lb2_2.place(x=270, y=82)
        lb2_3 = label1(app, point)
        lb2_3.place(x=270, y=105)
        lb2_4 = label1(app, point3)
        lb2_4.place(x=345, y=105)
        lb2_5 = Label(app, bg=gray2, image=R_img0_2)
        lb2_5.place(x=300, y=131)       

        bt0_1 = Button(app, bg=gray1, fg='white', command=reset_ranking, relief=FLAT, font=('Unispace', '12', 'bold'),image=R_img0_3, compound=LEFT, text=' Voltar', activebackground=gray1, bd=1)
        bt0_1.place(x=147, y=185)

    R_img1 = ImageTk.PhotoImage(PIL.Image.open('./img/papel.png').resize((60, 60)))
    R_img2 = ImageTk.PhotoImage(PIL.Image.open('./img/tesoura.png').resize((60, 60)))

    lb3 = Label(app, bg=gray1, image=R_img1).place(x=70, y=120)
    lb4 = Label(app, bg=gray1, image=R_img2).place(x=265, y=120)
    tx1 = Entry(app, bg='white', fg='black')
    tx1.place(x=180, y=62)
    bt1 = Button(app, bg=gray2, fg='white', text='Jogar', command=play_choose, font=('Unispace', '12', 'bold')).place(x=170, y=100)
    bt2 = Button(app, bg=gray2, fg='white', text='Ranking', command=ranking, font=('Unispace', '12', 'bold')).place(x=160, y=150)
    lb5 = Label(app, bg=gray1, fg='white', text='Desenvolvido por: Lucasbxd', font=('Arial','8','italic')).place(x=0,y=200)
    app.mainloop()
menu()
