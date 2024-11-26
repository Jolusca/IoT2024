import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Substitua pela connection string do seu dispositivo
CONNECTION_STRING = "HostName=TesteIotJlucas2002.azure-devices.net;DeviceId=TesteIotJL;SharedAccessKey=jILAh5EHenpe7JbHY8UTNnZMRViVYdGrZc7Zma2i2XU="

# Função para enviar dados
def send_random_number(client):
    number = input ("Digite aqui a sua mensagem:")
    message = Message(f'{{{number}}}')
    print(f"Enviando número: {number}")
    client.send_message(message)
    print("Número enviado com sucesso!")

# Função para receber mensagens
def message_handler(message):
    print(f"Mensagem recebida: {message.data}")
    if message.data:
        try:
            received_number = int(message.data)
            print(f"Mensagem processada como número: {received_number}")
        except ValueError:
            print("Mensagem não é um número válido.")

# Configurar o cliente
def main():
    print("Iniciando o simulador IoT...")
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    # Configurar handler para mensagens recebidas
    client.on_message_received = message_handler

    try:
        while True:
            send_random_number(client)
            #time.sleep(20)  # Envia números a cada 10 segundos
    except KeyboardInterrupt:
        print("Simulador encerrado.")
    finally:
        client.shutdown()

if __name__ == "__main__":
    main()