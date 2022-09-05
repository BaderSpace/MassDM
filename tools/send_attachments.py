import requests


token = ""

# under working


def send_attachment(token):
    header = {
        'authorization': token,
    }

    attachments = {
        "file": ("./images/logos/MassDM.png", open("./images/logos/MassDM.png", 'rb')),
        "file1": ("./images/logos/github_logo.png", open("./images/logos/github_logo.png", 'rb'))
    }

    payload = {
        "content": "test"
    }

    r = requests.post(
        "https://discord.com/api/v9/channels/test/messages", data=payload, headers=header, files=attachments)


send_attachment(token)
