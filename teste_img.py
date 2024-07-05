import requests
import json
from utils.config import webhook

def send_slack_message_with_image(webhook_url, message, image_url):
    payload = {
        "text": message,
        "attachments": [
            {
                "fallback": "Imagem",
                "image_url": image_url
            }
        ]
    }
    
    headers = {'Content-type': 'application/json'}
    
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        print("Mensagem enviada com sucesso para o Slack!")
    else:
        print(f"Erro ao enviar mensagem para o Slack: {response.status_code}, {response.text}")

# Exemplo de uso
message = 'Mensagem com imagem'
image_url = '/home/gabrielsilva/Documentos/codigos/MLT/anomaly_pt.png'

send_slack_message_with_image(webhook, message, image_url)