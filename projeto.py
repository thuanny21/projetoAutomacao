import pyautogui
import pandas as pd 
import time

#define o tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 0.5


#abrir sistema (navegador)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperar carregar
time.sleep(3)

#fazer login
pyautogui.click(x=416, y=266)
pyautogui.write("thuannymarcilia@outlook.com")

#senha
pyautogui.press("tab")
pyautogui.write("123")

#clicar em logar
pyautogui.click(x=691, y=537)
time.sleep(3)

#importar a base de produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)

#aqui precisamos percorrer as linhas da tabela para cada linha vamosthuannymarcilia@outlook.com sua senha cadastrar um produto
for linha in tabela.index:
  pyautogui.click(x=1723, y=418)
  pyautogui.write(str(tabela.loc[linha, "codigo"])) #pega o código da tabela e escreva no campo
  pyautogui.press("tab")#passa pro proximo campo
  pyautogui.write(str(tabela.loc[linha, "marca"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "tipo"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "preco-unitario"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  if not pd.isna(tabela.loc[linha, "obs"]):
    pyautogui.write(str(tabela.loc[linha, "obs"]))

pyautogui.click(x=1808, y=1380)
pyautogui.scroll(5000)




