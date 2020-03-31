#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os


office_orders_channel_id = "CH9R3B128"  # office_orders
test_id = "CA9FU10N4"  # sean-testroom


def send_mcdonald_notification(event, context):
    message = "\n".join([
        "<!here> *早安，您好。感恩，讚嘆！*",
        "每週速食日又到了，<@U6FK11X5E> 準備好來份速食了嗎？",
    ])

    json_payload = {
        "channel": office_orders_channel_id,
        "username": "麥當勞提醒器",
        "attachments": [{
            "text": message,
            "image_url": "https://i.imgur.com/lhmIWHQ.jpg",
            "actions": [
                {
                    "text": "麥當勞",
                    "type": "button",
                    "url": "https://www.mcdelivery.com.tw/tw/browse/menu.html"
                },
                {
                    "text": "肯德基",
                    "type": "button",
                    "url": "https://www.kfcclub.com.tw/tw/Menu/hot-meal/hot-menu"
                }
            ]
        }]
    }
    return requests.post(
        # for security issue, url will define in lambda environment variables
        os.environ.get("slack_hooks_url"),
        json=json_payload
    ).content
