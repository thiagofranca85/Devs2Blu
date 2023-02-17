import pyautogui as p

p.hotkey('win', 'r', duration=1)
p.sleep(1)
p.typewrite('cmd')
p.sleep(1)
p.hotkey('enter')
p.sleep(1)
p.click(x=436, y=285)
p.sleep(1)
p.typewrite('code .')
p.sleep(1)
p.hotkey('enter')