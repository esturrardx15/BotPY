# pip install pyautogui

import pyautogui #importar a biblioteca
pyautogui.PAUSE=0.5 #Tempo, em segundos, que terá de intervalo entre uma linha de comando e outra

# pyautogui.click -> clicar
# pyautogui.press -> pressionar tecla
# pyautogui.write -> escrever

# Passo 1: Abrir sistema
pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# Passo 2: Login
# Passo 3: Importar a base de dados dos produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir passo 4 até acabar produtos