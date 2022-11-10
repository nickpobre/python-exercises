from re import A
import matplotlib.pyplot as plt
import PySimpleGUI as sg

#define um tema para a parte visual
sg.theme("Reddit")

#Função que calcula o produto vetorial
def produto_vetorial(vetor = []):
    w1 = vetor[0]*vetor[3]
    w2 = vetor[1]*vetor[4] 
    w3 = vetor[2]*vetor[5]
    f = [w1,w2,w3]
    return f

def is_coplanar(a):
    if a == 0:
        c = "Os vetores U, V e W são coplanares"
        return c
    else:
        return a

#Função que calcula o produto misto
def produtomisto(vetor = []):  
    #multiplicação da matriz
    a1 = vetor[6]*vetor[1]*vetor[5]
    a2 = vetor[0]*vetor[4]*vetor[8]
    a3 = vetor[3]*vetor[7]*vetor[2]
    b1 = vetor[8]*vetor[1]*vetor[3]
    b2 = vetor[2]*vetor[4]*vetor[6]
    b3 = vetor[5]*vetor[7]*vetor[0]
    #soma dos produtos
    produto = (a1+a2+a3) - (b1+b2+b3)
    if produto < 0:
        return produto * produto
    else:
        return produto

def view_2(vetor = []):
    resultado = produto_vetorial(vetor)
    new_vet = []
    new_vet.append(vet)
    new_vet.append(resultado)
    aux = new_vet[0]+new_vet[1]
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    ax.set_xlim([-1,20])
    ax.set_ylim([-20,20])
    ax.set_zlim([0,20])
    start = [0,0,0]
    ax.quiver(start[0],start[1],start[2],aux[0],aux[1],aux[2])
    ax.quiver(start[0],start[1],start[2],aux[3],aux[4],aux[5])
    ax.quiver(start[0],start[1],start[2],aux[6],aux[7],aux[8],color="red")
    ax.view_init(10,10)
    plt.show()

def view(vetor = []):
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    start = [0,0,0]
    ax.quiver(start[0],start[1],start[2],vetor[0],vetor[1],vetor[2])
    ax.quiver(start[0],start[1],start[2],vetor[3],vetor[4],vetor[5])
    ax.quiver(start[0],start[1],start[2],vetor[6],vetor[7],vetor[8])
    ax.quiver(vetor[0],vetor[1],vetor[2],vetor[6],vetor[7],vetor[8],color = 'red', alpha=.4)
    ax.quiver(vetor[6],vetor[7],vetor[8],vetor[0],vetor[1],vetor[2],color = 'red', alpha=.4)
    ax.quiver(vetor[0],vetor[1],vetor[2],vetor[3],vetor[4],vetor[5],color = 'red', alpha=.4)
    ax.quiver(vetor[3],vetor[4],vetor[5],vetor[0],vetor[1],vetor[2],color = 'red', alpha=.4)
    ax.quiver(vetor[3],vetor[4],vetor[5],vetor[6],vetor[7],vetor[8],color = 'red', alpha=.4)
    ax.quiver(vetor[6],vetor[7],vetor[8],vetor[3],vetor[4],vetor[5],color = 'red', alpha=.4)
    ax.quiver(vetor[6],vetor[7],vetor[8],vetor[3],vetor[4],vetor[5],color = 'red', alpha=.4)
    ax.quiver(vetor[6]+vetor[3],vetor[7]+vetor[4],vetor[8]+vetor[5],vetor[0],vetor[1],vetor[2],color = 'red', alpha=.4)
    ax.quiver(vetor[0]+vetor[6],vetor[1]+vetor[7],vetor[2]+vetor[8],vetor[3],vetor[4],vetor[5],color = 'red', alpha=.4)
    ax.quiver(vetor[0]+vetor[3],vetor[1]+vetor[4],vetor[2]+vetor[5],vetor[6],vetor[7],vetor[8],color = 'red', alpha=.4)
    ax.view_init(10,10)
    plt.show()

def pm4(vetor = []):
    ab = vetor[3]-vetor[0]
    ab2 = vetor[4]-vetor[1]
    ab3 = vetor[5]-vetor[2]
    ac = vetor[6]-vetor[0]
    ac2 = vetor[7]-vetor[1]
    ac3 = vetor[8]-vetor[2]
    ad = vetor[9]-vetor[0]
    ad2 = vetor[10]-vetor[1]
    ad3 = vetor[11]-vetor[2]
    vet = [ab,ab2,ab3,ac,ac2,ac3,ad,ad2,ad3]
    return vet
#Cria a primeira janela

def make_win1():
    #layout da primeira tela
    
    Layout = [
            [sg.Image('C:/Users/felly/Documents/GitHub/python-exercises/img-0.png',expand_y=True)],
            [sg.Button("Proximo"),sg.Button("Sair")],
        ]

    return sg.Window('Definição produto misto', layout= Layout, finalize=True)

#cria a janela 2
def make_win2():
    #layout da segunda janela
    Layout = [
        [sg.Image('C:/Users/felly/Documents/GitHub/python-exercises/exe1.png',expand_y=True)],
        [sg.Image('C:/Users/felly/Documents/GitHub/python-exercises/exe2.png',expand_y=True)],
        [sg.Image('C:/Users/felly/Documents/GitHub/python-exercises/exe3.png',expand_y=True)],
        [sg.Button("Retornar"),sg.Button("Proximo"),sg.Button("Sair")]
    ]
    return sg.Window('Parte 2', layout= Layout, finalize=True)

#Cria a janela 3
def make_win3():
    #layout da terceira janela
    Layout = [
        [sg.Text("Digite os valores dos vetores abaixo")],
        [sg.Text("Vetor U:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-1-'),sg.Input(do_not_clear=True,size=(10,1),key='-2-'),sg.Input(do_not_clear=True,size=(10,1),key='-3-')],
        [sg.Text("Vetor V:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-4-'),sg.Input(do_not_clear=True,size=(10,1),key='-5-'),sg.Input(do_not_clear=True,size=(10,1),key='-6-')],
        [sg.Text("Resultado:"),tela_r],
        [sg.Button("Calcular",key='-pv-'),sg.Button('Retornar'),sg.Button("Proximo"),sg.Button('Visualizar',key='-v-'),sg.Exit("Sair")]
    ]
    return sg.Window('Calcular produto vetorial', layout = Layout, finalize=True)

#Cria a janela 4
def make_win4():
    Layout = [
        [sg.Text("Digite os valores dos vetores abaixo")],
        [sg.Text("Vetor U:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-1-'),sg.Input(do_not_clear=True,size=(10,1),key='-2-'),sg.Input(do_not_clear=True,size=(10,1),key='-3-')],
        [sg.Text("Vetor V:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-4-'),sg.Input(do_not_clear=True,size=(10,1),key='-5-'),sg.Input(do_not_clear=True,size=(10,1),key='-6-')],
        [sg.Text("Vetor W:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-7-'),sg.Input(do_not_clear=True,size=(10,1),key='-8-'),sg.Input(do_not_clear=True,size=(10,1),key='-9-')],
        [sg.Text("Resultado:"),tela_r],
        [sg.Button("Calcular",key='-c-'),sg.Button('Retornar'),sg.Button("Proximo"),sg.Button('Visualizar'),sg.Exit("Sair")]
    ]
    return sg.Window('Calcular produto misto', layout = Layout, finalize=True)

def make_win5():
    Layout = [
        [sg.Text("Digite os valores dos vetores abaixo")],
        [sg.Text("Vetor U:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-1-'),sg.Input(do_not_clear=True,size=(10,1),key='-2-'),sg.Input(do_not_clear=True,size=(10,1),key='-3-')],
        [sg.Text("Vetor V:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-4-'),sg.Input(do_not_clear=True,size=(10,1),key='-5-'),sg.Input(do_not_clear=True,size=(10,1),key='-6-')],
        [sg.Text("Vetor W:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-7-'),sg.Input(do_not_clear=True,size=(10,1),key='-8-'),sg.Input(do_not_clear=True,size=(10,1),key='-9-')],
        [sg.Text("Vetor D:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-10-'),sg.Input(do_not_clear=True,size=(10,1),key='-11-'),sg.Input(do_not_clear=True,size=(10,1),key='-12-')],
        [sg.Text("Resultado:"),tela_r],
        [sg.Text("Produto misto:"),sg.Text("",key='-pm4r-')],
        [sg.Text("Volume:"),sg.Text("",key='-v4r-')],
        [sg.Button("Calcular",key='-p4-'),sg.Button('Retornar'),sg.Button("Vizualizar",key='-v4-'),sg.Exit("Sair")]
    ]
    return sg.Window("Calcular Tetraedro", layout = Layout, finalize=True)

#define a janela inicial
window1,window2 ,window3 ,window4 ,window5 = make_win1(), None, None, None, None

#loop para manter o programa sempre aberto ate que um evento de fechar seja chamado
while True:

    window, event, Values = sg.read_all_windows()
    tela_r = sg.Text(key="-r-")
    
    #caso aperte no botão de sair
    if event == sg.WIN_CLOSED or event == 'Sair':
        window.close()
        if window == window2:       
            window2 = None
        elif window == window1:
            break

    #Caso esteja na janela 1 e aperta no botão proximo ele esconde a janela 1 e mostra a janela 2  
    elif window == window1 and event == 'Proximo':
        window2 = make_win2()
        window1.hide()
    
    #Caso esteja na janela 2 e aperta no botão proximo ele esconde a janela 2 e mostra a janela 3
    elif window == window2 and event == 'Proximo':
        window3 = make_win3()
        window2.hide()

    #Caso esteja na janela 3 e aperta no botão proximo ele esconde a janela 3 e mostra a janela 4
    elif window == window3 and event == 'Proximo':
        window4 = make_win4()
        window3.hide()

    #Caso esteja na janela 5 e aperta no botão proximo ele esconde a janela 5 e mostra a janela 5
    elif window == window4 and event == 'Proximo':
        window5 = make_win5()
        window4.hide()

    #Caso esteja na janela 2 e aperte em retornar ele esconde a janela 2 e mostra a janela 1
    if window == window2 and event == 'Retornar':
        window1.un_hide()
        window2.hide()
    
    #Caso esteja na janela 3 e aperte em retornar ele esconde a janela 3 e mostra a janela 2
    if window == window3 and event == 'Retornar':
        window2.un_hide()
        window3.hide()
    
    if window == window4 and event == 'Retornar':
        window3.un_hide()
        window4.hide()
    
    if window == window5 and event == 'Retornar':
        window4.un_hide()
        window5.hide()
    
    #caso aperte o botão calcular ele pega os valores e envia para a função produtomisto()
    if event == '-c-':
        vet = [
            int(Values['-1-']),
            int(Values['-2-']),
            int(Values['-3-']),
            int(Values['-4-']),
            int(Values['-5-']),
            int(Values['-6-']),
            int(Values['-7-']),
            int(Values['-8-']),
            int(Values['-9-']),
        ]
        resultado = is_coplanar(produtomisto(vet))

        #mostra na tela o resultado
        window['-r-'].update(resultado)
    if event == 'Visualizar':
        vet = [
            int(Values['-1-']),
            int(Values['-2-']),
            int(Values['-3-']),
            int(Values['-4-']),
            int(Values['-5-']),
            int(Values['-6-']),
            int(Values['-7-']),
            int(Values['-8-']),
            int(Values['-9-']),
        ]
        view(vet)
    if event == '-v-':
        vet = [
            int(Values['-1-']),
            int(Values['-2-']),
            int(Values['-3-']),
            int(Values['-4-']),
            int(Values['-5-']),
            int(Values['-6-']),
        ]
        view_2(vet)
    #caso aperte o botão calcular ele pega os valores e envia para a função produto_vetorial()
    if event == '-pv-':
        vet = [
            int(Values['-1-']),
            int(Values['-2-']),
            int(Values['-3-']),
            int(Values['-4-']),
            int(Values['-5-']),
            int(Values['-6-']),
        ]
        resultado = produto_vetorial(vet)
        window['-r-'].update(resultado)

    if event == '-p4-':
        vet = [
            int(Values['-1-']),
            int(Values['-2-']),
            int(Values['-3-']),
            int(Values['-4-']),
            int(Values['-5-']),
            int(Values['-6-']),
            int(Values['-7-']),
            int(Values['-8-']),
            int(Values['-9-']),
            int(Values['-10-']),
            int(Values['-11-']),
            int(Values['-12-']),
        ]
        resultado = pm4(vet)
        a = produtomisto(resultado)
        b = a/6
        window['-pm4r-'].update(a)
        window['-v4r-'].update(b)
        window['-r-'].update(resultado)

    if event == '-v4-':
        vet = [
            int(Values['-1-']),
            int(Values['-2-']),
            int(Values['-3-']),
            int(Values['-4-']),
            int(Values['-5-']),
            int(Values['-6-']),
            int(Values['-7-']),
            int(Values['-8-']),
            int(Values['-9-']),
            int(Values['-10-']),
            int(Values['-11-']),
            int(Values['-12-']),
        ]
        resultado = pm4(vet)
        view(resultado)

window.close()