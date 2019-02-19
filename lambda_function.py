#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

channel_id = "C0BU52LDQ" #mage-research-room
test_id = "CA9FU10N4" #sean-testroom

message = "\n".join([
    "*早安，您好!*",
    "星期三速食日又到了，準備好來份速食了嗎？",
])

json_payload = {
    "channel": channel_id,
    "parse": "full",
    "unfurl_media":True,
    "unfurl_links":True,
    "text": "@here https://imgur.com/a/tkGDiMP",
    "attachments":[{
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
requests.post(post_msg_url, json=json_payload)
