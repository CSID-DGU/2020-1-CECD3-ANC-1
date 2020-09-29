# -*- coding: utf-8 -*-

# 파일로 출력하기
i = 1
# 출력, 입력 값 JSON 파일을 생성합니다.
prev = str(conversations[0].contentName) + str(conversations[0].contentType)
f = open(prev + '.json', 'w', encoding='UTF-8')
f.write('{ "id": "10d3155d-4468-4118-8f5d-15009af446d0" , \n "name": "' + prev + '", \n "auto": true,\n"contexts": [],\n "responses": [ { "resetContexts": false, \n"affectedContexts": [], \n"parameters": [], \n"messages": [ { "type": 0,\n"lang": "ko", \n"speech": "' + str(conversations[0].answer) + '" } ], \n"defaultResponsePlatforms": {}, \n"speech": [] } ], \n"priority": 500000,\n "webhookUsed": false,\n "webhookForSlotFilling": false,\n "fallbackIntent": false, \n"events": [] }')
f.close()
f = open(prev + '_usersays_ko.json', 'w', encoding='UTF-8')
f.write("[")
f.write('{ "id": "3330d5a3-f38e-48fd-a3e6-000000000001",\n "data": [ { "text": "' + str(conversations[0].question) + '", \n"userDefined": false } ],\n "isTemplate": false,\n "count": 0 }')

while True:
    if i >= len(conversations):
        f.write("]")
        f.close()
        break;
    c = conversations[i]
    if prev == str(c.contentName) + str(c.contentType):
        f.write('{ "id": "3330d5a3-f38e-48fd-a3e6-000000000001", "data": [ { "text": "' + str(c.question) + '", "userDefined": false } ], "isTemplate": false, "count": 0 }')
    else:
        f.write("]")
        f.close()
        # 출력, 입력 값 JSON 파일을 생성합니다.
        prev = str(c.contentName) + str(c.contentType)
        f = open(prev + '.json', 'w', encoding='UTF-8')
        f.write('{ "id": "10d3155d-4468-4118-8f5d-15009af446d0", \n"name": "' + prev + '",\n "auto": true, \n"contexts": [],\n "responses": [ { "resetContexts": false, \n"affectedContexts": [],\n "parameters": [], \n"messages": [ { "type": 0, \n"lang": "ko", \n"speech": "' + str(c.answer) + '" } ],\n "defaultResponsePlatforms": {}, \n"speech": [] } ], \n"priority": 500000, \n"webhookUsed": false,\n "webhookForSlotFilling": false,\n "fallbackIntent": false,\n "events": [] }')
        f.close()
        f = open(prev + '_usersays_ko.json', 'w', encoding='UTF-8')
        f.write("[")
        f.write('{ "id": "3330d5a3-f38e-48fd-a3e6-000000000001", \n"data": [ { "text": "' + str(c.question) + '",\n "userDefined": false } ], \n"isTemplate": false, \n"count": 0 }')
    i = i + 1