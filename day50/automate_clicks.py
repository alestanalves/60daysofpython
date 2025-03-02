import pyautogui
import time

print("Posicione o mouse na tela e espere 5 segundos...")
# time.sleep(5)

# print(pyautogui.position())
while True:
    time.sleep(5)
    x, y = 754, 680
    pyautogui.click(x, y)
    print(f"Clicou na primeira posicao: {x}, {y}")

    time.sleep(5)
    x, y = 507, 554
    pyautogui.click(x, y)
    print(f"Clicou na segunda posicao: {x}, {y}")
