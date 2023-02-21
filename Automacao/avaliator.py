import pyautogui as p
import rpa as r
import tagui as t

# # Acesso ao Navegador, Site e Avaliação pelo pyautogui
# url = 'https://externo.proway.com.br/login-aluno'

# webbrowser.register('chrome',
# 	None,
#     # Endereço Chrome Curso
# 	# webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
# 	# Endereço Chrome em casa
# 	webbrowser.BackgroundBrowser("C://Users//xDraKx//AppData//Local//Google//Chrome//Application//chrome.exe"))
# webbrowser.get('chrome').open(url)

# p.sleep(3)

# btn_acessar = p.locateCenterOnScreen('btn_acessar.png')
# p.sleep(1)
# p.click(btn_acessar)
# p.sleep(1)
# btn_avaliar_aula = p.locateCenterOnScreen('btn_avaliar_aula_2.png')
# p.sleep(1)
# p.click(btn_avaliar_aula)
# p.sleep(1)

# Selecionando todas as opções da Avaliação, digitando o texto e enviando
# Usando RPA

r.init()
r.url('https://www.google.com')
r.type('//*[@name="q"]', 'Como curar a tosse do pedro?[enter]')



