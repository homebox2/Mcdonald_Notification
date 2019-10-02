#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import requests

office_orders_channel_id = "CH9R3B128"  # office_orders
test_id = "CA9FU10N4"  # sean-testroom


def send_happy_food_notification(event, context):
    message = "\n".join([
        "<!here> *午安，您好。*",
        "<@U0QLXH31U> : 星期四中午要吃一日樂食嗎～",
        "今天 *17:00* 收單 +1請留言+多少錢",
        "*除了燉牛肉和鷹嘴豆，要記得選醬哦！*",
    ])

    json_payload = {
        "channel": office_orders_channel_id,
        "attachments": [{
            "image_url": "https://i.imgur.com/TXSv3IP.jpg",
            "text": message,
            "actions": [
                {
                    "text": "-----菜單請點我-----",
                    "type": "button",
                    "url": "https://deliexpress.oddle.me/zh_TW/"
                }
            ]
        }]
    }
    post_msg_url = "https://hooks.slack.com/services/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"
    return requests.post(post_msg_url, json=json_payload).content
