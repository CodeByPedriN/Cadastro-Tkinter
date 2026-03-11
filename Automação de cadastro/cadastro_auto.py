import pyautogui
import time


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

with open("lista.txt", "r") as arquivo:    
    for linha in arquivo:
        produto = linha.split(",")[0]
        quantidade = linha.split(",")[1]
        preco = linha.split(",")[2]
        
        pyautogui.click (x=1276, y=492)
        pyautogui.write(produto)
        pyautogui.press("tab")
        pyautogui.write(quantidade)
        pyautogui.press("tab")
        pyautogui.write(preco)
        pyautogui.click (x=1283, y=649)
        time.sleep(1)