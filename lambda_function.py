#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

channel_id = "C0BU52LDQ"  # mage-research-room
test_id = "CA9FU10N4"  # sean-testroom
sean_slack_token = "xoxp-2151498087-342741108625-350366769909-de1330f405b0f954a5c62bc8fa33b0ad"

def send_notification():
    message = "\n".join([
        "*早安，您好!*",
        "星期三速食日又到了， @jane 準備好來份速食了嗎？",
    ])

    json_payload = {
        "channel": channel_id,
        "parse": "full",
        "unfurl_media": True,
        "unfurl_links": True,
        "text": "@here https://imgur.com/a/tkGDiMP",
        "attachments": [{
            "image_url": "https://imgur.com/a/tkGDiMP",
            "text": message,
            "actions": [
                {
                    "text": "麥當勞",
                    "type": "button",
                    "url": "https://www.mcdelivery.com.tw/tw/browse/menu.html"
                },
                {
                    "text": "漢堡王",
                    "type": "button",
                    "url": "http://www.burgerking.com.tw/menu.php"
                },
                {
                    "text": "肯德基",
                    "type": "button",
                    "url": "https://www.kfcclub.com.tw/tw/Menu/hot-meal/hot-menu"
                }
            ]
        }]
    }
    post_msg_url = "https://hooks.slack.com/services/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"
    return requests.post(post_msg_url, json=json_payload)


def get_last_message():
    channel_history_url = "https://slack.com/api/channels.history"
    history_payload = {
        "token": sean_slack_token,
        "channel": channel_id,
        "count": 1
    }
    response = requests.post(channel_history_url, json=history_payload)
    return response.content

def lambda_handler(event, context):
    send_notification()

    # print(get_last_message())

    # reactions_add_url = "https://slack.com/api/reactions.add"
    #
    # for emoji in [":mcdonalds:"]:
    #     emoji_payload = {
    #         "token": "tKLwoecuqJQO74D8VEnToucV",
    #         "name": emoji,
    #         "channel": channel_id,
    #         "timestamp": timestamp
    #     }
    #     response = requests.post(reactions_add_url, json=emoji_payload)
    #     print(response.content)

lambda_handler(None, None)