import pyautogui as p

p.hotkey('win', 'r', duration=1)

p.sleep(1)
p.typewrite('notepad')
p.sleep(1)
p.hotkey('enter')
p.sleep(2)
p.typewrite('Sejam bem vindos ao mundo da automacao')
p.sleep(2)
p.hotkey('enter')
p.typewrite('Ueb')
p.press('a', presses=30)
p.sleep(5)
valor = p.getActiveWindow()
valor.close()
p.press('right')
p.sleep(2)
p.press('enter')