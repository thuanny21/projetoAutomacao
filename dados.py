import pyautogui
import pandas as pd 
import time

#importar a base de produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)