fila_processos = []

while True:
    comando = input("Digite um comando (adicionar, remover, fim): ")

    if comando == "adicionar":
        processo =  input("Digite o nome do processo: ")
        fila_processos.append(processo)
        print("Fila de processos:", fila_processos)

    elif comando == "remover":
        if len(fila_processos) > 0:
            processo_removido = fila_processos.pop(0)
            print(f"Processo removido: {processo_removido}" )
            print("Fila de processos:" , fila_processos)

        else:
            print("A fila está vazia . Nenhum processo será removido.")

    elif comando == "fim":
        print("Encerrando o programa")
    break
    
else:
    print("Comando inválido. Digite 'adicionar' , 'remover' , 'fim'.")
