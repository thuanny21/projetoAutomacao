import pyautogui
import pandas as pd 
import time

#define o tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 0.5


#abrir sistema (navegador)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#esperar carregar
time.sleep(5)
print(pyautogui.position())#pegar a posição do mouse para saber onde clicar
pyautogui.scroll(-200) #testar quanto de scroll

#fazer login
pyautogui.click(x=669, y=379)
pyautogui.write("thuannymarcilia@outlook.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.click(x=1902, y=838)

#aqui precisamos percorrer as linhas da tabela para cada linha vamos cadastrar um produto
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




