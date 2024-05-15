class Menu:
    @staticmethod
    def escolha_modelo():
        while True:
            print("Qual modelo usar")
            print("1. Regreção Linear")
            print("2. KNN")
            escolha = input("Escolha o modelo (1 ou 2)\n")
            
            if escolha == "1":
                print ("Usando Regreção")
                return 'Linear', None
            elif escolha == "2":
                while True:
                    try:
                        n_neighbors = int(input("Digite o número de vizinhos para o KNN\n"))
                        if n_neighbors < 1:
                            print("O número não pode ser menor que 1")
                        else:
                            print(f"Usando KNN com k={n_neighbors}")
                            return 'KNN', n_neighbors
                    except ValueError:
                        print("Por favor coloque um número inteiro")
                        
            else:
                print("Porfavor escolha entre (1 ou 2)\n")