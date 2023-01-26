Sending a request - url: https://www.slack.com/api/chat.postMessage, query_params: {}, body_params: {}, files: {},
json_body: {
    'channel': 'C04HA0XRFEU',
    'text': '<@U04FX011280> ',
    'team_id': 'T04F75F9SKV'
},
headers: {
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': '(redacted)',
    'User-Agent': 'Python/3.10.9 slackclient/3.19.5 Windows/10'
}
Received the following response - status: 200,
headers: {
    'date': 'Thu, 26 Jan 2023 12:59:22 GMT',
    'server': 'Apache',
    'x-powered-by': 'HHVM/4.153.1',
    'access-control-allow-origin': '*',
    'referrer-policy': 'no-referrer',
    'x-slack-backend': 'r',
    'x-slack-unique-id': 'Y9J5KoBkKzTEvpb7iFXfygAAEAg',
    'strict-transport-security': 'max-age=31536000; includeSubDomains; preload',
    'access-control-allow-headers': 'slack-route, x-slack-version-ts, x-b3-traceid, x-b3-spanid, x-b3-parentspanid, x-b3-sampled, x-b3-flags',
    'access-control-expose-headers': 'x-slack-req-id, retry-after',
    'x-oauth-scopes': 'app_mentions:read,chat:write,chat:write.customize,commands,im:history,im:read,im:write,links:read,links:write,reminders:read,reminders:write,users:read,mpim:history,groups:history,channels:history',
    'x-accepted-oauth-scopes': 'chat:write',
    'expires': 'Mon, 26 Jul 1997 05:00:00 GMT',
    'cache-control': 'private, no-cache, no-store, must-revalidate',
    'pragma': 'no-cache',
    'x-xss-protection': '0',
    'x-content-type-options': 'nosniff',
    'x-slack-req-id': 'b3f60fde24ceb69efb54a7cfc5ee45df',
    'vary': 'Accept-Encoding',
    'content-type': 'application/json; charset=utf-8',
    'x-envoy-upstream-service-time': '267',
    'x-backend': 'main_normal main_bedrock_normal_with_overflowmain_canary_with_overflow main_bedrock_canary_with_overflow main_control_with_overflow main_bedrock_control_with_overflow',
    'x-server': 'slack-www-hhvm-main-iad-prvn', 'x-slack-shared-secret-outcome': 'no-match', 'via': 'envoy-www-iad-p9ch, envoy-edge-bom-d97e',
    'x-edge-backend': 'envoy-www',
    'x-slack-edge-shared-secret-outcome': 'no-match',
    'connection': 'close',
    'transfer-encoding': 'chunked'
},
body = {
    "ok":True,
    "channel":"C04HA0XRFEU",
    "ts":"1674737962.064619",
    "message":{
        "bot_id":"B04JM11SYP4",
        "type":"message",
        "text":"<@U04FX011280>",
        "user":"U04J6EJGY6B",
        "ts":"1674737962.064619",
        "app_id":"A04JPDE8TB6",
        "blocks":[
            {
                "type":"rich_text",
                "block_id":"XAmm",
                "elements":[
                    {
                        "type":"rich_text_section",
                        "elements":[
                            {
                                "type":"user",
                                "user_id":"U04FX011280"
                            }
                        ]
                    }
                ]
            }
        ],
        "team":"T04F75F9SKV",
        "bot_profile":{
            "id":"B04JM11SYP4",
            "app_id":"A04JPDE8TB6",
            "name":"Mini_Zoom",
            "icons":{
                "image_36":"https:\/\/a.slack-edge.com\/80588\/img\/plugins\/app\/bot_36.png",
                "image_48":"https:\/\/a.slack-edge.com\/80588\/img\/plugins\/app\/bot_48.png",
                "image_72":"https:\/\/a.slack-edge.com\/80588\/img\/plugins\/app\/service_72.png"
            },
            "deleted":false,
            "updated":1673526397,
            "team_id":"T04F75F9SKV"
        }
    }
}
