import PySimpleGUI as sg
#define um tema para a parte visual
sg.theme("Reddit")
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
    #caso o produto final seja 0 ele informa que é coplanar
    if produto == 0:
        c = "Os vetors U,V e W são coplanares"
        return c
    #caso não seja coplanar ele retorna o valor do produto final
    else:
        return produto
#Cria a primeira janela
def make_win1():
    #layout da primeira tela
    Layout = [
            [sg.Text('Produto Misto')],
            [sg.Text(
            ""
            ,size=(100,None))],
            [sg.Image("")],
            [sg.Text(
                ""
            ,size=(100,None))],
            [sg.Image("")],
            [sg.Button('Proximo'), sg.Button('Sair')]
        ]
    return sg.Window('Definição produto misto', layout= Layout, finalize=True)
#cria a janela 2
def make_win2():
    #layout da segunda janela
    Layout = [
        [sg.Text("",size=(100,None))],
        [sg.Button("Retornar"),sg.Button("Proximo"),sg.Button("Sair")]
    ]
    return sg.Window('Parte 2', layout= Layout, finalize=True)
#Cria a janela 3
def make_win3():
    tela_r = sg.Text(key="-r-")
    #layout da terceira janela
    Layout = [
        [sg.Text("Digite os valores dos vetores abaixo")],
        [sg.Text("Vetor U:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-1-'),sg.Input(do_not_clear=True,size=(10,1),key='-2-'),sg.Input(do_not_clear=True,size=(10,1),key='-3-')],
        [sg.Text("Vetor V:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-4-'),sg.Input(do_not_clear=True,size=(10,1),key='-5-'),sg.Input(do_not_clear=True,size=(10,1),key='-6-')],
        [sg.Text("Vetor W:")],
        [sg.Input(do_not_clear=True,size=(10,1),key='-7-'),sg.Input(do_not_clear=True,size=(10,1),key='-8-'),sg.Input(do_not_clear=True,size=(10,1),key='-9-')],
        [sg.Text("Resultado:"),tela_r],
        [sg.Button("Calcular",key='-c-'),sg.Button('Retornar'),sg.Exit("Sair")]
    ]
    return sg.Window('Window Title', layout = Layout, finalize=True)
#deifine a janela inicial
window1, window2 , window3 = make_win1(), None, None
#loop
while True:             
    window, event, Values = sg.read_all_windows()
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
    #Caso esteja na janela 2 e aperte em retornar ele esconde a janela 2 e mostra a janela 1
    if window == window2 and event == 'Retornar':
        window1.un_hide()
        window2.hide()
    #Caso esteja na janela 3 e aperte em retornar ele esconde a janela 3 e mostra a janela 2
    if window == window3 and event == 'Retornar':
        window2.un_hide()
        window3.hide()
    #caso aperte o botão calcular ele pega os valores e envia para a função produtomisto() /linha 5/
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
        resultado = produtomisto(vet)
        #mostra na tela o resultado
        window['-r-'].update(resultado)

window.close()