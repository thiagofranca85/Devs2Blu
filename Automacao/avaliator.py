import pyautogui as p
import rpa as r
import webbrowser

# Acesso ao Navegador, Site e Avaliação pelo pyautogui
url = 'https://externo.proway.com.br/login-aluno'

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(url)

p.sleep(3)

btn_acessar = p.locateCenterOnScreen('btn_acessar.png')
p.sleep(1)
p.click(btn_acessar)
p.sleep(1)
btn_avaliar_aula = p.locateCenterOnScreen('btn_avaliar_aula.png')
p.sleep(1)
p.click(btn_avaliar_aula)
p.sleep(1)

# Selecionando todas as opções da Avaliação, digitando o texto e enviando
# Usando RPA

r.init()

r.wait(2)
opcao1 = r.select('//*[@id="dailyEvaluationForm_hoje"]/div/label[5]/span[2]')
r.click(opcao1)




