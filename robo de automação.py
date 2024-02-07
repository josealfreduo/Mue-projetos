# PROJETO DE AUTOMAÇÃO DE ITENS PARA UMA LOJA

# 1 ENTRAR NO SISTEMA
#import pyautogui
import pyautogui
import time
#  clickar - pyautogui.click
# escrever - pyautogui.write
# precionar - pyautogui.press
# apertar - pyatuogui.hotkey = crtl c e crtl v
pyautogui.PAUSE = 1
# apertar o windowns
pyautogui.press("win")
# digitar o nome do programa(crhome)
pyautogui.write("edge")
# apertar enter
pyautogui.press("enter")
# digitar link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
# apertar enter
pyautogui.press("enter")

# espera 5 segudos
time.sleep(5)

# 2 FAZER LOGIN
pyautogui.click(x=714, y=358)
#digita email
pyautogui.write("gabrielflorianopolis@hotmail.com")
# passar para o campo da senha
pyautogui.press('tab')
# digitar a senha
pyautogui.write("Canasbol123")
# logar
pyautogui.click(x=657, y=519)
# 3 IMPORTAR A BASE DE DADOS
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=560, y=237)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    pyautogui.press("enter") # cadastra o produto (botao enviar)
        # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim