import requests

def formatMessage(webhook_url, mensagem):
    formatted_message = f"```Attention:\n{mensagem}\n```"

    payload = {
        "attachments": [
            {
                "color": "FF0000",
                "text": formatted_message,
                "mrkdwn_in": ["text"]
            }
        ]
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 200:
        print("Success!")
    else:
        print("Error:", response.status_code)
