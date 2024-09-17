import random
import sqlite3

# Função para configurar o banco de dados
def configurar_banco():
    conn = sqlite3.connect('quiz_grunge.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pontuacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            pontuacao INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Função para salvar a pontuação no banco de dados
def salvar_pontuacao(nome, pontuacao):
    conn = sqlite3.connect('quiz_grunge.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pontuacoes (nome, pontuacao) VALUES (?, ?)', (nome, pontuacao))
    conn.commit()
    conn.close()

# Função para exibir a pontuação geral
def exibir_pontuacoes_gerais():
    conn = sqlite3.connect('quiz_grunge.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome, pontuacao FROM pontuacoes')
    resultados = cursor.fetchall()
    conn.close()
    
    if resultados:
        print("\n===== Pontuações Gerais =====")
        for resultado in resultados:
            print(f"{resultado[0]}: {resultado[1]} pontos")
    else:
        print("\nAinda não há pontuações armazenadas.")

# Perguntas e respostas do quiz
perguntas = [
    {"pergunta": "Qual banda é conhecida por lançar a música 'Dirt'?", "opcoes": "(A) Pearl Jam\n(B) Nirvana\n(C) Alice in Chains\n(D) Soundgarden", "resposta": "C"},
    {"pergunta": "Qual o nome do vocalista da banda Pearl Jam?", "opcoes": "(A) Kurt Cobain\n(B) Eddie Vedder\n(C) Chris Cornell\n(D) Layne Staley", "resposta": "B"},
    {"pergunta": "Em que ano o vocalista Kurt Cobain se matou?", "opcoes": "(A) 1990\n(B) 1994\n(C) 1998\n(D) 2000", "resposta": "B"},
    {"pergunta": "Qual banda é famosa por lançar o álbum 'Superunknown'?", "opcoes": "(A) Soundgarden\n(B) Nirvana\n(C) Pearl Jam\n(D) Stone Temple Pilots", "resposta": "A"},
    {"pergunta": "Qual banda lançou o álbum 'Ten'?", "opcoes": "(A) Pearl Jam\n(B) Alice in Chains\n(C) Nirvana\n(D) Stone Temple Pilots", "resposta": "A"},
    {"pergunta": "Qual banda gravou o álbum 'Nevermind'?", "opcoes": "(A) Pearl Jam\n(B) Soundgarden\n(C) Nirvana\n(D) Mudhoney", "resposta": "C"},
    {"pergunta": "Qual música de Nirvana foi tocada no MTV Unplugged?", "opcoes": "(A) Heart-Shaped Box\n(B) Smells Like Teen Spirit\n(C) About a Girl\n(D) In Bloom", "resposta": "C"},
    {"pergunta": "Qual é o nome do álbum de estreia do Soundgarden?", "opcoes": "(A) Louder Than Love\n(B) Badmotorfinger\n(C) Superunknown\n(D) Ultramega OK", "resposta": "D"},
    {"pergunta": "Qual o nome do vocalista da banda Alice in Chains?", "opcoes": "(A) Layne Staley\n(B) Chris Cornell\n(C) Kurt Cobain\n(D) Eddie Vedder", "resposta": "A"},
    {"pergunta": "Qual banda gravou o álbum 'In Utero'?", "opcoes": "(A) Nirvana\n(B) Pearl Jam\n(C) Soundgarden\n(D) Alice in Chains", "resposta": "A"},
    {"pergunta": "Qual foi o último álbum de estúdio do Nirvana?", "opcoes": "(A) Nevermind\n(B) Bleach\n(C) In Utero\n(D) Unplugged in New York", "resposta": "C"},
    {"pergunta": "Qual banda lançou a música 'Black'?", "opcoes": "(A) Alice in Chains\n(B) Pearl Jam\n(C) Nirvana\n(D) Soundgarden", "resposta": "B"},
    {"pergunta": "Qual vocalista era conhecido por sua luta contra o vício?", "opcoes": "(A) Kurt Cobain\n(B) Eddie Vedder\n(C) Layne Staley\n(D) Chris Cornell", "resposta": "C"},
    {"pergunta": "Em que cidade o movimento grunge se originou?", "opcoes": "(A) Los Angeles\n(B) Seattle\n(C) Nova York\n(D) Portland", "resposta": "B"},
    {"pergunta": "Qual banda grunge lançou o álbum 'Dirt'?", "opcoes": "(A) Nirvana\n(B) Soundgarden\n(C) Alice in Chains\n(D) Pearl Jam", "resposta": "C"},
    {"pergunta": "Qual álbum do Pearl Jam tem a música 'Jeremy'?", "opcoes": "(A) Vs.\n(B) Vitalogy\n(C) Ten\n(D) Yield", "resposta": "C"},
    {"pergunta": "Qual foi o primeiro álbum do Nirvana?", "opcoes": "(A) In Utero\n(B) Bleach\n(C) Nevermind\n(D) Incesticide", "resposta": "B"},
    {"pergunta": "Qual banda lançou o álbum 'Core'?", "opcoes": "(A) Nirvana\n(B) Stone Temple Pilots\n(C) Pearl Jam\n(D) Alice in Chains", "resposta": "B"},
    {"pergunta": "Qual dessas bandas não é considerada grunge?", "opcoes": "(A) Pearl Jam\n(B) Stone Temple Pilots\n(C) Nirvana\n(D) The Smashing Pumpkins", "resposta": "D"},
    {"pergunta": "Qual é o nome do baterista do Nirvana?", "opcoes": "(A) Dave Grohl\n(B) Krist Novoselic\n(C) Matt Cameron\n(D) Jack Irons", "resposta": "A"},
    {"pergunta": "Qual banda lançou a música 'Man in the Box'?", "opcoes": "(A) Alice in Chains\n(B) Soundgarden\n(C) Nirvana\n(D) Pearl Jam", "resposta": "A"},
    {"pergunta": "Qual música de Alice in Chains fala sobre vício?", "opcoes": "(A) Man in the Box\n(B) Rooster\n(C) Would?\n(D) Them Bones", "resposta": "C"},
    {"pergunta": "Qual banda lançou a música 'Plush'?", "opcoes": "(A) Stone Temple Pilots\n(B) Pearl Jam\n(C) Alice in Chains\n(D) Nirvana", "resposta": "A"},
    {"pergunta": "Qual música do Nirvana ficou famosa no álbum 'Nevermind'?", "opcoes": "(A) Lithium\n(B) Smells Like Teen Spirit\n(C) Come as You Are\n(D) Polly", "resposta": "B"},
    {"pergunta": "Qual banda lançou o álbum 'Temple of the Dog'?", "opcoes": "(A) Soundgarden\n(B) Pearl Jam\n(C) Temple of the Dog\n(D) Nirvana", "resposta": "C"},
    {"pergunta": "Qual dessas bandas não fazia parte do movimento grunge de Seattle?", "opcoes": "(A) Soundgarden\n(B) Nirvana\n(C) Pearl Jam\n(D) The Smashing Pumpkins", "resposta": "D"},
]

# Função principal do quiz
def quiz():
    nome = input("Digite seu nome: ")
    
    print(f"Bem-vindo ao Quiz Grunge, {nome}!")

    while True:
        opcao = input("Escolha uma opção:\n1. Iniciar o quiz\n2. Exibir pontuações gerais\n3. Sair\nDigite o número da opção: ").strip()
        
        if opcao == "1":
            # Iniciar o quiz com 7 perguntas
            pontuacao = 0
            perguntas_selecionadas = random.sample(perguntas, 7)  # Seleciona 7 perguntas aleatórias
            random.shuffle(perguntas_selecionadas)  # Embaralha as perguntas selecionadas

            for pergunta in perguntas_selecionadas:
                print(f"\n{pergunta['pergunta']}")
                print(pergunta['opcoes'])
                resposta = input("Sua resposta: ").strip().upper()
                if resposta == pergunta['resposta']:
                    print("Resposta correta!")
                    pontuacao += 1
                else:
                    print("Resposta incorreta.")
            
            print(f"\n{nome}, sua pontuação final é {pontuacao}/7.")
            salvar_pontuacao(nome, pontuacao)
        
        elif opcao == "2":
            # Exibir pontuações gerais
            exibir_pontuacoes_gerais()
        
        elif opcao == "3":
            # Sair
            print("Obrigado por jogar! Até a próxima.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Configurar o banco de dados
configurar_banco()

# Executar o quiz
quiz()



 