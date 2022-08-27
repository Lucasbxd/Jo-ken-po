import cmd
import re
from tkinter import *
from tokenize import String
from PIL import ImageTk
import PIL.Image
from random import randint
from tkinter import messagebox
from operator import itemgetter, attrgetter

cor_cinza_ton1 = '#252627'
cor_cinza_ton2 = '#2e3031'
cor_cinza_ton3 = '#a9a9a9'
cor_preto_ton1 = 'black'
cor_branco_ton1 = 'white'

def redimensionar_imagem(local, nova_largura, nova_altura):
  return ImageTk.PhotoImage(PIL.Image.open(local).resize((nova_largura, nova_altura)))

def centralizar_janela(width, height):
    global app
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    app.geometry('%dx%d+%d+%d' % (width, height, x, y))

def finalizar_jogo():
  global pontuacao
  global nome_do_player
  global variavel_pontuacao
  global escolha_do_player
  global inserir_nome
  global imagem_win_off
  global imagem_win_on
  global imagem_vs
  global imagem_proximo

  def reset():
    global pontuacao
    variavel_pontuacao.set('Pontos: {}'.format(pontuacao))
    if(status_do_jogo == 'perdeu'):
      abrir_arquivo_ranking = open('./config/ranking.txt','a')
      abrir_arquivo_ranking.write('{},{}\n'.format(nome_do_player,pontuacao))
      abrir_arquivo_ranking.close()
      messagebox.showinfo('Partida Finalizada', 'Você perdeu!\nPontuação: {}'.format(pontuacao))
      app.destroy()
      jogar()
      
    frame_layout1.destroy()
    frame_layout2.destroy()
    frame_layout3.destroy()
    label_imagem_win_off1.destroy()
    label_imagem_win_off2.destroy()
    label_imagem_win_on.destroy()
    label_imagem_cpu.destroy()
    label_imagem_escolha_player.destroy()
    label_texto_player.destroy()
    label_texto_cpu.destroy()
    label_imagem_vs.destroy()
    button_proximo.destroy()

  frame_layout1 = Frame(app, bg=cor_cinza_ton1)
  frame_layout1.place(x=0, y=50, width=390, height=220)

  frame_layout2 = Frame(app, bg=cor_branco_ton1)
  frame_layout2.place(x=4, y=54, width=122, height=122)

  frame_layout3 = Frame(app, bg=cor_branco_ton1)
  frame_layout3.place(x=264, y=54, width=122, height=122)

  opcoes_de_escolha = ['pedra', 'papel', 'tesoura']
  escolha_do_cpu = opcoes_de_escolha[randint(0,2)]

  imagem_win_off = redimensionar_imagem('./img/win_off.png',30,30)
  label_imagem_win_off1 = Label(app, bg=cor_cinza_ton1, image=imagem_win_off)
  label_imagem_win_off1.place(x=50, y=20)

  label_imagem_win_off2 = Label(app, bg=cor_cinza_ton1, image=imagem_win_off)
  label_imagem_win_off2.place(x=310, y=20)

  imagem_win_on = redimensionar_imagem('./img/win_on.png',30,30)
  label_imagem_win_on = Label(app, bg=cor_cinza_ton1, image=imagem_win_on)

  if(escolha_do_player == escolha_do_cpu):
    status_do_jogo = 'empate'
        
  elif((escolha_do_player == 'papel' and escolha_do_cpu == 'pedra') 
      or (escolha_do_player == 'tesoura' and escolha_do_cpu == 'papel') 
      or (escolha_do_player == 'pedra' and escolha_do_cpu == 'tesoura')):
    status_do_jogo = 'ganhou'
    label_imagem_win_on.place(x=50, y=20)
    pontuacao += 1

  elif((escolha_do_player == 'papel' and escolha_do_cpu == 'tesoura') 
      or (escolha_do_player == 'pedra' and escolha_do_cpu == 'papel') 
      or (escolha_do_player == 'tesoura' and escolha_do_cpu == 'pedra')):
    status_do_jogo = 'perdeu'
    label_imagem_win_on.place(x=310, y=20)

  if escolha_do_player == 'papel':
      image_player = imagem_papel
  elif escolha_do_player == 'pedra':
      image_player = imagem_pedra
  elif escolha_do_player == 'tesoura':
      image_player = imagem_tesoura
  
  label_imagem_escolha_player = Label(app, bg=cor_cinza_ton1, image=image_player)
  label_imagem_escolha_player.place(x=5, y=55, width=120, height=120)

  if escolha_do_cpu == 'papel':
      image_cpu = imagem_papel
  elif escolha_do_cpu == 'pedra':
      image_cpu = imagem_pedra
  elif escolha_do_cpu == 'tesoura':
      image_cpu = imagem_tesoura

  label_imagem_cpu = Label(app, bg=cor_cinza_ton1, image=image_cpu)
  label_imagem_cpu.place(x=265, y=55, width=120, height=120)

  imagem_vs = redimensionar_imagem('./img/vs.png',100,97)
  label_imagem_vs = Label(app, bg=cor_cinza_ton1, image=imagem_vs)
  label_imagem_vs.place(x=140, y=55, width=110, height=120)

  label_texto_player = Label(app, bg=cor_cinza_ton1, text='Player', fg='white',font=('Unispace', '15', 'bold'))
  label_texto_player.place(x=30, y=180)
  
  label_texto_cpu = Label(app, bg=cor_cinza_ton1, text='CPU', fg='white',font=('Unispace', '15', 'bold'))
  label_texto_cpu.place(x=310, y=180)

  imagem_proximo = redimensionar_imagem('./img/proximo.png',20,20)
  button_proximo = Button(app, 
    bg=cor_cinza_ton1, 
    fg='white', 
    relief=RIDGE,
    font=('Unispace', '12', 'bold'),
    image=imagem_proximo, 
    command=reset, 
    compound=LEFT, 
    text=' Avançar', 
    activebackground=cor_cinza_ton1, 
    bd=2)
  button_proximo.place(x=142, y=180)

def jogar():
  global app
  global pontuacao
  global variavel_pontuacao
  global imagem_papel
  global imagem_pedra
  global imagem_tesoura
  global pontuacao
  pontuacao = 0

  app = Tk()
  centralizar_janela(390,220)
  app.resizable(False, False)
  app.title('Jogar')

  def finalizar(escolha):
    global escolha_do_player
    escolha_do_player = escolha
    finalizar_jogo()

  def home():
    app.destroy()
    menu()

  frame_layout1 = Frame(app, bg=cor_cinza_ton1)
  frame_layout1.place(x=0, y=0, width=390, height=220)

  frame_layout2 = Frame(app, bg=cor_branco_ton1)
  frame_layout2.place(x=4, y=54, width=122, height=122)

  frame_layout3 = Frame(app, bg=cor_branco_ton1)
  frame_layout3.place(x=134, y=54, width=122, height=122)

  frame_layout4 = Frame(app, bg=cor_branco_ton1)
  frame_layout4.place(x=264, y=54, width=122, height=122)

  variavel_pontuacao = StringVar()
  variavel_pontuacao.set('Pontos: {}'.format(pontuacao))

  label_pontuacao = Label(app, textvariable=variavel_pontuacao, bg=cor_cinza_ton1, fg='white', font=('Unispace', '15', 'bold'))
  label_pontuacao.place(x=130, y=10)

  label_texto_papel = Label(app, bg=cor_cinza_ton1, text='Papel', fg='white', font=('Unispace', '15', 'bold'))
  label_texto_papel.place(x=30, y=180)

  label_texto_pedra = Label(app, bg=cor_cinza_ton1, text='Pedra', fg='white', font=( 'Unispace', '15', 'bold'))
  label_texto_pedra.place(x=160, y=180)

  label_texto_tesoura = Label(app, bg=cor_cinza_ton1, text='Tesoura', fg='white', font=('Unispace', '15', 'bold'))
  label_texto_tesoura.place(x=280, y=180)

  imagem_papel = redimensionar_imagem('./img/papel.png',100,100)
  button_jogar_papel = Button(app, 
    bg=cor_cinza_ton2, 
    relief=FLAT, 
    bd=0, 
    image=imagem_papel, 
    activebackground=cor_cinza_ton2, 
    command=lambda: finalizar('papel'))
  button_jogar_papel.place(x=5, y=55, width=120, height=120)

  imagem_pedra = redimensionar_imagem('./img/pedra.png',100,100)
  button_jogar_pedra = Button(app, 
    bg=cor_cinza_ton2, 
    relief=FLAT, 
    bd=0, 
    image=imagem_pedra, 
    activebackground=cor_cinza_ton2, 
    command=lambda: finalizar('pedra'))
  button_jogar_pedra.place(x=135, y=55, width=120, height=120)

  imagem_tesoura = redimensionar_imagem('./img/tesoura.png',100,100)
  button_jogar_tesoura = Button(app, 
    bg=cor_cinza_ton2, 
    relief=FLAT, 
    bd=0, 
    image=imagem_tesoura, 
    activebackground=cor_cinza_ton2, 
    command=lambda: finalizar('tesoura'))
  button_jogar_tesoura.place(x=265, y=55, width=120, height=120)

  imagem_home = redimensionar_imagem('./img/home.png',20,20)
  button_jogar_tesoura = Button(app, 
    bg=cor_cinza_ton2, 
    relief=FLAT, 
    bd=0, 
    image=imagem_home, 
    activebackground=cor_cinza_ton2, 
    command=home)
  button_jogar_tesoura.place(x=0, y=0)

  app.mainloop()

def ranking():
  global imagem_replay
  global app

  app = Tk()
  centralizar_janela(390,220)
  app.resizable(False, False)
  app.title('Ranking')

  class ranking():
    def __init__(self, name, point):
        self.name = name
        self.point = point

    def __repr__(self):
        return '{},{}'.format(self.name,self.point)
  
  def reset_ranking():
    app.destroy()
    menu()

  frame_layout_ranking1 = Frame(app, bg=cor_cinza_ton1)
  frame_layout_ranking1.place(x=0, y=0, width=390, height=220)

  frame_layout_ranking2 = Frame(app, bg=cor_cinza_ton2)
  frame_layout_ranking2.place(x=0, y=0, width=390, height=40)

  frame_layout_ranking3 = Frame(app, bg=cor_branco_ton1)
  frame_layout_ranking3.place(x=4, y=54, width=122, height=122)

  frame_layout_ranking4 = Frame(app, bg=cor_branco_ton1)
  frame_layout_ranking4.place(x=134, y=54, width=122, height=122)

  frame_layout_ranking5 = Frame(app, bg=cor_branco_ton1)
  frame_layout_ranking5.place(x=264, y=54, width=122, height=122)

  frame_layout_ranking6 = Frame(app, bg=cor_cinza_ton2)
  frame_layout_ranking6.place(x=5, y=55, width=120, height=120)

  frame_layout_ranking7 = Frame(app, bg=cor_cinza_ton2)
  frame_layout_ranking7.place(x=135, y=55, width=120, height=120)

  frame_layout_ranking8 = Frame(app, bg=cor_cinza_ton2)
  frame_layout_ranking8.place(x=265, y=55, width=120, height=120)

  label_texto_colocacoes = Label(app, text='As três melhores colocações', bg=cor_cinza_ton2, fg='white',font=('Unispace', '12', 'bold'))
  label_texto_colocacoes.place(x=55, y=10)

  nome_primeiro_lugar = StringVar()
  pontos_primeiro_lugar = IntVar()

  nome_segundo_lugar = StringVar()
  pontos_segundo_lugar = IntVar()

  nome_terceiro_lugar = StringVar()
  pontos_terceiro_lugar = IntVar()

  lista_ranking = []
  arquivo_do_ranking = open('./config/ranking.txt').readlines()

  if(len(arquivo_do_ranking) > 2):
      for line in arquivo_do_ranking:
        lista_ranking.append(ranking(line.split(',')[0], int(line.split(',')[1].rstrip())))
      lista_ranking = sorted(lista_ranking, key=attrgetter('point'), reverse=True)

      primeiro = str(lista_ranking[0])
      segundo = str(lista_ranking[1])
      terceiro = str(lista_ranking[2])

      nome_primeiro_lugar.set(primeiro.split(',')[0])
      pontos_primeiro_lugar.set(primeiro.split(',')[1])

      nome_segundo_lugar.set(segundo.split(',')[0])
      pontos_segundo_lugar.set(segundo.split(',')[1])

      nome_terceiro_lugar.set(terceiro.split(',')[0])
      pontos_terceiro_lugar.set(terceiro.split(',')[1])
  else:
      nome_primeiro_lugar.set('S/N')
      pontos_primeiro_lugar.set(0)

      nome_segundo_lugar.set('S/N')
      pontos_segundo_lugar.set(0)

      nome_terceiro_lugar.set('S/N')
      pontos_terceiro_lugar.set(0)

  label_nome1 = Label(app, bg=cor_cinza_ton2, fg=cor_cinza_ton3, text='Nome:', font=('Unispace', '12', 'bold'))
  label_nome1.place(x=10, y=60)

  label_pontos1 = Label(app, bg=cor_cinza_ton2, fg=cor_cinza_ton3, text='Pontos:', font=('Unispace', '12', 'bold'))
  label_pontos1.place(x=10, y=105)

  label_nome_primeiro = Label(app, bg=cor_cinza_ton2, fg=cor_branco_ton1, textvariable=nome_primeiro_lugar, font=('Unispace', '12', 'bold'))
  label_nome_primeiro.place(x=10, y=82)

  label_pontos_primeiro = Label(app, bg=cor_cinza_ton2, fg=cor_branco_ton1, textvariable=pontos_primeiro_lugar, font=('Unispace', '12', 'bold'))
  label_pontos_primeiro.place(x=85, y=105)

  imagem_medalha_primeiro = redimensionar_imagem('./img/primeiro.png',40,40)
  label_imagem_medalha_primeiro = Label(app, bg=cor_cinza_ton2, image=imagem_medalha_primeiro)
  label_imagem_medalha_primeiro.place(x=42, y=131)

  label_nome2 = Label(app, bg=cor_cinza_ton2, fg=cor_cinza_ton3, text='Nome:', font=('Unispace', '12', 'bold'))
  label_nome2.place(x=140, y=60)

  label_pontos2 = Label(app, bg=cor_cinza_ton2, fg=cor_cinza_ton3, text='Pontos:', font=('Unispace', '12', 'bold'))
  label_pontos2.place(x=140, y=105)

  label_nome_segundo = Label(app, bg=cor_cinza_ton2, fg=cor_branco_ton1, textvariable=nome_segundo_lugar, font=('Unispace', '12', 'bold'))
  label_nome_segundo.place(x=140, y=82)

  label_pontos_segundo = Label(app, bg=cor_cinza_ton2, fg=cor_branco_ton1, textvariable=pontos_segundo_lugar, font=('Unispace', '12', 'bold'))
  label_pontos_segundo.place(x=215, y=105)

  imagem_medalha_segundo = redimensionar_imagem('./img/segundo.png',40,40)
  label_imagem_medalha_segundo = Label(app, bg=cor_cinza_ton2, image=imagem_medalha_segundo)
  label_imagem_medalha_segundo.place(x=175, y=131)

  label_nome3 = Label(app, bg=cor_cinza_ton2, fg=cor_cinza_ton3, text='Nome:', font=('Unispace', '12', 'bold'))
  label_nome3.place(x=270, y=60)

  label_pontos3 = Label(app, bg=cor_cinza_ton2, fg=cor_cinza_ton3, text='Pontos:', font=('Unispace', '12', 'bold'))
  label_pontos3.place(x=270, y=105)

  label_nome_terceiro = Label(app, bg=cor_cinza_ton2, fg=cor_branco_ton1, textvariable=nome_terceiro_lugar, font=('Unispace', '12', 'bold'))
  label_nome_terceiro.place(x=270, y=82)

  label_pontos_terceiro = Label(app, bg=cor_cinza_ton2, fg=cor_branco_ton1, textvariable=pontos_terceiro_lugar, font=('Unispace', '12', 'bold'))
  label_pontos_terceiro.place(x=345, y=105)

  imagem_medalha_terceiro = redimensionar_imagem('./img/terceiro.png',40,40)
  label_imagem_medalha_terceiro = Label(app, bg=cor_cinza_ton2, image=imagem_medalha_terceiro)
  label_imagem_medalha_terceiro.place(x=300, y=131) 
  
  imagem_replay = redimensionar_imagem('./img/replay.png',20,20)
  button_voltar_ranking = Button(app, 
    bg=cor_cinza_ton1, 
    fg=cor_branco_ton1, 
    command=reset_ranking, 
    relief=FLAT, 
    font=('Unispace', '12', 'bold'),
    image=imagem_replay, 
    compound=LEFT, 
    text=' Voltar', 
    activebackground=cor_cinza_ton1,
    activeforeground=cor_branco_ton1,
    bd=1)
  button_voltar_ranking.place(x=147, y=185)

  app.mainloop()

def menu():
  global app
  global inserir_nome

  app = Tk()
  centralizar_janela(390,220)
  app.resizable(False, False)
  app.title('Menu')

  def iniciar_jogo():
    global nome_do_player
    if(inserir_nome.get() != ''):
      nome_do_player = inserir_nome.get()
      app.destroy()
      jogar()
    else:
      messagebox.showerror('Campo de nome vazio','Digite um Nome para jogar.')
  
  def abrir_ranking():
    app.destroy()
    ranking()
  
  frame_layout1 = Frame(app, bg=cor_cinza_ton1)
  frame_layout1.place(x=0, y=0, width=390, height=220)

  frame_layout2 = Frame(app, bg=cor_cinza_ton2)
  frame_layout2.place(x=0, y=0, width=390, height=40)

  label_texto_titulo = Label(app, text='Jogo da velha', bg=cor_cinza_ton2, fg='white',font=('Unispace', '12', 'bold'))
  label_texto_titulo.place(x=120, y=10)

  label_texto_nome = Label(app, text='Seu Nome: ', bg=cor_cinza_ton1, fg='white',font=('Unispace', '12', 'bold'))
  label_texto_nome.place(x=80, y=60)

  imagem_papel = redimensionar_imagem('./img/papel.png',60,60)
  label_imagem_papel = Label(app, bg=cor_cinza_ton1, image=imagem_papel)
  label_imagem_papel.place(x=70, y=120)

  imagem_tesoura = redimensionar_imagem('./img/tesoura.png',60,60)
  label_imagem_tesoura = Label(app, bg=cor_cinza_ton1, image=imagem_tesoura)
  label_imagem_tesoura.place(x=265, y=120)

  inserir_nome = Entry(app, bg=cor_branco_ton1, fg=cor_preto_ton1)
  inserir_nome.place(x=180, y=62)

  button_jogar = Button(app, bg=cor_cinza_ton2, fg='white', text='Jogar', command=iniciar_jogo, font=('Unispace', '12', 'bold'))
  button_jogar.place(x=170, y=100)

  button_ranking = Button(app, bg=cor_cinza_ton2, fg='white', text='Ranking', command=abrir_ranking, font=('Unispace', '12', 'bold'))
  button_ranking.place(x=160, y=150)

  label_creditos = Label(app, bg=cor_cinza_ton1, fg='white', text='Desenvolvido por: Lucasbxd', font=('Arial','8','italic'))
  label_creditos.place(x=0,y=200)

  app.mainloop()

menu()