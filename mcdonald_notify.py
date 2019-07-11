#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

office_orders_channel_id = "CH9R3B128"  # office_orders
test_id = "CA9FU10N4"  # sean-testroom

sean_slack_token = "xoxp-2151498087-342741108625-350366769909-de1330f405b0f954a5c62bc8fa33b0ad"

def send_mcdonald_notification(event, context):
    message = "\n".join([
        "*早安，您好。感恩，讚嘆！*",
        "星期三速食日又到了，@jane 準備好來份速食了嗎？",
    ])

    json_payload = {
        "channel": office_orders_channel_id,
        "parse": "full",
        "username": "麥當勞提醒器",
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
    return requests.post(post_msg_url, json=json_payload).content

# def get_last_message():
#     channel_history_url = "https://slack.com/api/channels.history"
#     history_payload = {
#         "token": sean_slack_token,
#         "channel": channel_id,
#         "count": 1
#     }
#     response = requests.post(channel_history_url, json=history_payload)
#     return response.json_payload

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
