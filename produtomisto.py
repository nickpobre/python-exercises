from unittest import result
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
    return produto

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
    resultado = produtomisto(vet)
    return resultado
#Cria a primeira janela
def make_win1():
    #layout da primeira tela
    Layout = [
            [sg.Text('Produto Misto')],
            [sg.Text("")],
            [sg.Image("")],
            [sg.Text("")],
            [sg.Image("")],
            [sg.Button('Proximo'), sg.Button('Sair')]
        ]
    return sg.Window('Definição produto misto', layout= Layout, finalize=True)

#cria a janela 2
def make_win2():
    #layout da segunda janela
    Layout = [
        [sg.Text("")],
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
        [sg.Button("Calcular",key='-pv-'),sg.Button('Retornar'),sg.Button("Proximo"),sg.Exit("Sair")]
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
        [sg.Button("Calcular",key='-c-'),sg.Button('Retornar'),sg.Button("Proximo"),sg.Exit("Sair")]
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
        [sg.Button("Calcular",key='-p4-'),sg.Button('Retornar'),sg.Exit("Sair")]
    ]
    return sg.Window("Calcular Tetraedro", layout = Layout, finalize=True)

#define a janela inicial
window1, window2 , window3, window4, window5 = make_win1(), None, None, None, None

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
        resultado = is_coplanar(pm4(vet))
        window['-r-'].update(resultado)

window.close()