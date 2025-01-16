# pip install pyautogui

#import == Importar biblioteca
import pyautogui 
import time
import pandas

pyautogui.PAUSE=2 #Tempo, em segundos, que terá de intervalo entre uma linha de codigo e outra

# pyautogui.click -> clicar
# pyautogui.press -> pressionar tecla
# pyautogui.write -> escrever
# payautogui.hotkey -> atalho do teclado

# Passo 1: Abrir sistema
pyautogui.press("win") #Abrir pesquisa windows
pyautogui.write("Opera") #pesquisar seu navegador
pyautogui.press("enter") #Pressiona botao do teclado
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link) #Digita informação desejada
pyautogui.press("enter")

# Passo 2: Login
time.sleep(5) #Tempo de pausa até executar a proxima linha (vai de acordo com a sua maquina/internet)
pyautogui.click (x=689, y=388) #Posção que o mouse precisa clicar na tela (informação retirada ao executar arquivo auxi.py)
pyautogui.write ("blablabl@blablabla.com")
pyautogui.press("tab")
pyautogui.write("blablabl")
pyautogui.press("enter")
time.sleep(5)

# Passo 3: Importar a base de dados dos produtos
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=692, y=272)

    #Codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #Marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #Tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #Categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # Preço Unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #Custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #Obs
    obs = str(tabela.loc[linha,"obs"])
    
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.press("home")

# Passo 5: Repetir passo 4 até acabar produtos