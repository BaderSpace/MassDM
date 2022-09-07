import requests as r
import json

# Enter Token

token = ""

# under working


def get_members(token, channel_id, proxy=None):

    headers = {'authorization': token}

    members_json = r.get(
        f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50', headers=headers)

    members_data = json.loads(members_json.text)

    with open("members.txt", 'w+', encoding="utf-8") as file:
        membersList = []
        for value in members_data:

            if value['author']['id'] not in membersList:
                membersList.append(value['author']['id'])
                print(value['author']['id'], value['author']['username'])
                file.writelines(value['author']['id']+":"
                                + value['author']['username'] + '\n')
            else:
                pass
        membersList.clear()
    return members_json.status_code, members_json.text


if __name__ == "__main__":

    chnl = "1017143498035691621"
    get_members(token, chnl)
