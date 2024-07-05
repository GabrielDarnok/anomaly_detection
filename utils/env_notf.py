import requests

def formatMessage(webhook_url, mensagem):
    # Inicia a mensagem formatada
    formatted_message = f"```Attention:\n{mensagem}\n```"

    # Prepara o payload para o envio
    payload = {
        "attachments": [
            {
                "color": "FF0000",
                "text": formatted_message,
                "mrkdwn_in": ["text"]
            }
        ]
    }

    # Envia a notificação para o webhook
    response = requests.post(webhook_url, json=payload)

    # Verifica se a notificação foi enviada com sucesso
    if response.status_code == 200:
        print("Success!")
    else:
        print("Error:", response.status_code)
