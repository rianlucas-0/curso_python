import os
# import datetime
# import pyautogui
# import time

# pyautogui.press('win')
# pyautogui.write('chrome')
# pyautogui.press('enter')
# time.sleep(1)
# pyautogui.write('teste')
# time.sleep(1)
# print(datetime.date.today())

lista_arquivos = os.listdir('arquivos')

for arquivo in lista_arquivos:
    if '.txt' in arquivo:
        if '22' in arquivo:
            os.rename(f'arquivos/{arquivo}', f'arquivos/22/{arquivo}')
            print('Movimentar para a pasta 22', arquivo)
        else:
            os.rename(f'arquivos/{arquivo}', f'arquivos/23/{arquivo}')
            print('Movimentar para a pasta 23', arquivo)