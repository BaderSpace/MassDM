import requests as r
import json


token = ""

headers = {'authorization': token}

re = r.get(
    'https://discord.com/api/v9/channels/Channel/messages?limit=100', headers=headers)
print(re, re.text)

jsonn = json.loads(re.text)

with open("members.txt", 'w+', encoding="utf-8") as file:
    membersList = []
    for value in jsonn:

        if value['author']['id'] not in membersList:
            membersList.append(value['author']['id'])
            print(value['author']['id'], value['author']['username'])
            file.writelines(value['author']['id']+":"
                            + value['author']['username'] + '\n')
        else:
            pass
    membersList.clear()
