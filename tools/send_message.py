import requests

# Enter Token
token = ""

# under working


def send_message(token, channel_id, message="", files=[], proxy=None):

    header = {
        'authorization': token,
    }
    attachments = {}
    num = 0
    if len(files) > 0:
        for file in files:
            file_name = "file" if num == 0 else f"file{num}"
            attachments[file_name] = (file, open(file, "rb"))
            num += 1
    else:
        pass

    payload = {
        "content": message
    }

    message_post = requests.post(
        f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=header, files=attachments)

    return message_post.status_code, message_post.text


if __name__ == "__main__":

    msg = "Discord: https://discord.gg/5ykdz7nW\nGithub: https://github.com/BaderSpace/MassDM"
    fis = ["./images/logos/MassDM_Big.png"]
    chnl = "1017143498035691621"
    print(send_message(token, chnl, msg, fis))
