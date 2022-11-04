
# Criando form e usando botões
import PySimpleGUI as pg
from controllerGUI import salvarAlunos, salvarProfessor, salvarCursos


# Passo 1: Setar o theme
pg.theme('SandyBeach')

# Passo 2: Criar layout

def menu():    
    pg.theme('SandyBeach')
    telaInicial = [
        [pg.Text('Selecione a opção para continuar com os cadastros: ')],
        [pg.Button('Aluno'), pg.Button('Professor'), pg.Button('Cursos') ,pg.Button('Sair')],
        [pg.Text('')]
    ]
    window = pg.Window('Cadastros', layout = telaInicial)
    while True:
        event, values = window.read()
        if event == "Sair" or event == pg.WIN_CLOSED:
            break
        if event == "Aluno":
            telaAluno = aluno()
            telaInicial.close()
        if event == "Professor":
            telaProfessor = professor()
            telaInicial.close()
        if event == "Cursos":
            telaCursos= cursos()
            telaInicial.close()
    window.close()


#-------------------------------------------------------------------------------
# TELA ALUNO

def aluno():
    telaAluno = [
        [pg.Text("Nome: ", size=(9,1), key='aluno_nome'),pg.InputText(do_not_clear=False)],
        [pg.Text("Idade: ", size=(9,1), key='aluno_idade'),pg.InputText(do_not_clear=False)],
        [pg.Text("CPF: ", size=(9,1), key='aluno_cpf'),pg.InputText(do_not_clear=False)],
        [pg.Text("Matrícula: ", size=(9,1), key='aluno_matricula'),pg.InputText(do_not_clear=False)],
        [pg.Text("Cursos: "),pg.Listbox(["Python", "Java", "JavaScript", "C++"], size=(30,5), select_mode=pg.LISTBOX_SELECT_MODE_MULTIPLE)],

        [pg.Button("Cadastrar"),pg.Button("Sair")]
    ]

# Passo 3: Criar Window
    window = pg.Window("TELA DE CADASTRO DE ALUNO", layout = telaAluno)

# Passo 4: Event Loop
    while True:
        event, values = window.read()

        if event == pg. WIN_CLOSED or event == "Sair":
            break

        elif event == "Cadastrar":
            # mostrando em tela os dados de cadastro
            print(f"Nome: {values[0]}")
            print(f"Idade: {values[1]}")
            print(f"CPF: {values[2]}")
            print(f"Matrícula: {values[3]}")
            print(f"Curso(s): {values[4]}")
            # passando os dados de cadastro para a funcao salvarAlunosTeste salvar o txt.
            dados_aluno = {}                        
            dados_aluno['nome'] = values[0]
            dados_aluno['idade'] = values[1]
            dados_aluno['CPF'] = values[2]
            dados_aluno['matricula'] = values[3]
            dados_aluno['cursos'] = values[4]
            salvarAlunos(dados_aluno)

            for item in values:
                values[item]: None                

            # Passo 5: Close Windows
            window.close()
            exit()

#-------------------------------------------------------------------------------
# TELA PROFESSOR

def professor():
    telaProfessor = [
        [pg.Text("Nome: ", size=(9,1), key='professor_nome'),pg.InputText(do_not_clear=False)],
        [pg.Text("Idade: ", size=(9,1), key='professor_idade'),pg.InputText(do_not_clear=False)],
        [pg.Text("CPF: ", size=(9,1), key='professor_cpf'),pg.InputText(do_not_clear=False)],
        [pg.Text("Salário: ", size=(9,1), key='professor_salario'),pg.InputText(do_not_clear=False)],
        [pg.Text("Cursos ministrados: "),pg.Listbox(["Python", "Java", "JavaScript", "C++"], size=(30,5), select_mode=pg.LISTBOX_SELECT_MODE_MULTIPLE)],

        [pg.Button("Cadastrar"),pg.Button("Sair")]
    ]

# Passo 3: Criar Window
    window = pg.Window("TELA DE CADASTRO DE PROFESSOR", layout = telaProfessor)

# Passo 4: Event Loop
    while True:
        event, values = window.read()

        if event == pg. WIN_CLOSED or event == "Sair":
            break

        elif event == "Cadastrar":
            # mostrando em tela os dados de cadastro
            print(f"Nome: {values[0]}")
            print(f"Idade: {values[1]}")
            print(f"CPF: {values[2]}")
            print(f"Salário: {values[3]}")
            print(f"Curso(s): {values[4]}")
            # passando os dados de cadastro para a funcao salvarProfessorTest salvar o txt.
            dados_professor = {}                        
            dados_professor['nome'] = values[0]
            dados_professor['idade'] = values[1]
            dados_professor['CPF'] = values[2]
            dados_professor['matricula'] = values[3]
            dados_professor['cursos'] = values[4]
            salvarProfessor(dados_professor)

            for item in values:
                values[item]: None                

            # Passo 5: Close Windows
            window.close()
            exit()

#-------------------------------------------------------------------------------
# TELA CURSOS

def cursos():
    telaCursos = [
        [pg.Text("Curso: ", size=(9,1), key='curso_nome'),pg.InputText(do_not_clear=False)],
        [pg.Text("Carga-horária: ", size=(9,1), key='curso_horas'),pg.InputText(do_not_clear=False)],
        [pg.Text("Modalidade: "),pg.Listbox(["Presencial", "EAD", "Misto"], size=(30,4), select_mode=pg.LISTBOX_SELECT_MODE_MULTIPLE)],
        [pg.Button("Cadastrar"),pg.Button("Sair")]
    ]

# Passo 3: Criar Window
    window = pg.Window("TELA DE CADASTRO DE PROFESSOR", layout = telaCursos)

# Passo 4: Event Loop
    while True:
        event, values = window.read()

        if event == pg. WIN_CLOSED or event == "Sair":
            break

        elif event == "Cadastrar":
            # mostrando em tela os dados de cadastro
            print(f"Curso: {values[0]}")
            print(f"Carga-horária: {values[1]}")
            print(f"Modalidade: {values[2]}")

            dados_curso = {}                        
            dados_curso['Curso'] = values[0]
            dados_curso['Carga-horaria:'] = values[1]
            dados_curso['Modalidade'] = values[2]

            salvarCursos(dados_curso)

            for item in values:
                values[item]: None                

            # Passo 5: Close Windows
            window.close()
            exit()


menu()