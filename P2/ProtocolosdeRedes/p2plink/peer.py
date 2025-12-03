import socket
import threading
import time

#Confirmação de recebimento da mensagem
def receber_mensagens (conn):
    while True:
        try:
            mensagem = conn.recv(1024) .decode()
            if mensagem:
                print(f"\n[Recebido] {mensagem}")
        except:
            break

#Inicia o peer   
def iniciar_peer(meu_ip, minha_porta, ip_remoto, porta_remota):
    servidor = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    #Evitar problemas de conexão com a porta após fechar o app, mesmo que esteja em uso
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    servidor.bind((meu_ip, minha_porta))
    servidor.listen(1)
    time.sleep(1)
    print(f"[Esperando conexão em {meu_ip} : {minha_porta}]...")

#Aceita a conexão    
    def aceitar_conexao():
        conn, addr = servidor.accept()
        print(f"[Conectado por {addr}]")
        threading.Thread (target=receber_mensagens, args=(conn,), daemon=True) .start()
        time.sleep(1)
        return conn

#Cria um socket TCP/IP (orientado à conexão)
    cliente = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((ip_remoto, porta_remota))
        print(f"[Conectado ao peer {ip_remoto} : {porta_remota}]")
    except Exception as e:
        print(f"[Erro ao conectar: {e}]")
        cliente = None

    conexao_recebida = aceitar_conexao()

    while True:
        msg = input("Você: ")
        if cliente:
            try:
                cliente.send(msg.encode())
            except:
                print(f"[Erro ao enviar para peer remoto.]")
            try:
                conexao_recebida.send(msg.encode())
            except:
                print(f"[Erro ao enviar para conexão recebida.]")

#Informa portas para conexão
if __name__ == "__main__":
    meu_ip = "localhost"
    ip_remoto = "localhost"
    #Permite usuário informar qual porta deseja usar
    minha_porta = int(input("Digite a sua porta: "))
    porta_remota = int(input("Digite a porta do peer remoto: "))
    iniciar_peer(meu_ip, minha_porta, ip_remoto, porta_remota)