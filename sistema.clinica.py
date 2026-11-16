# PROJETO INTEGRADO - CLÍNICA VIDA+
pacientes = []
while True:
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        print("\n--- Novo Cadastro ---")
        nome = input("Nome do paciente: ")
    
        while True:
            try:
                idade = int(input("Idade: "))
                break  
            except ValueError:
                print("Erro: Digite apenas números para a idade!")
        
        telefone = input("Telefone: ")
        novo_paciente = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        }
        pacientes.append(novo_paciente)
        print("Paciente cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- Estatísticas da Clínica ---")
        total = len(pacientes)

        if total == 0:
            print("Nenhum paciente cadastrado ainda!")
        else:
            soma_idades = sum(p["idade"] for p in pacientes)
            media = soma_idades / total

            mais_novo = min(pacientes, key=lambda p: p["idade"])
            mais_velho = max(pacientes, key=lambda p: p["idade"])

            print(f"Total de pacientes cadastrados: {total}")
            print(f"Idade média dos pacientes: {media:.1f} anos")
            print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
            print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

    elif opcao == "3":
        print("\n--- Buscar Paciente ---")
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            busca = input("Digite o nome para buscar: ").lower()
            encontrado = False
            for p in pacientes:
                if busca in p["nome"].lower():
                    print(f"Encontrado: Nome: {p['nome']} | Idade: {p['idade']} | Tel: {p['telefone']}")
                    encontrado = True
            
            if not encontrado:
                print("Nenhum paciente encontrado com esse nome.")

    elif opcao == "4":
        print("\n--- Lista de Todos os Pacientes ---")
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            for i, p in enumerate(pacientes, start=1):
                print(f"{i}. Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")

    elif opcao == "5":
        print("\nSaindo do sistema... Até logo!")
        break
    else:
        print("Opção inválida! Escolha um número de 1 a 5.")