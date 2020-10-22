# -*- coding: utf-8 -*-
import openpyxl
import re

#한 건의 대화에 대한 정보를 담는  객체
class Conversation:
    #질문, 응답 두 변수로 구성됩니다. 
    def __init__(self, contentName, contentType, question, answer):
        self.contentName = contentName
        self.contentType = contentType
        self.question = question
        self.answer = answer

    def __str__(self):
        textQ = self.question
        textA = self.answer
        
        if type(textQ) == str and type(textA) == str: 
            textQ_mod = textQ.replace("\n","")
            textA_mod = textA.replace("\n","")
            self.question = textQ_mod
            self.answer = textA_mod
        return "질문 : " + str(self.question) + "\n대답 : " + str(self.answer)
    
wb = openpyxl.load_workbook(u"qnalist.xlsx", data_only = True)

ws = wb.active

conversations = []

#시트내 존재하는 모든 데이터 객체로 담음
try:
    for r in ws.rows:
#엑셀 시트내 큰따옴표 제거   
        if r[0].value is not None:
            q = r[2].value
            qq = re.sub("[\"]", "", str(q))
        
            a = r[3].value
            aa = re.sub("[\"]", "", str(a))
        
            c = Conversation(r[0].value, r[1].value, qq, aa)
    
            conversations.append(c)
        else: continue
except Exception as e:
    print(e)
        
wb.close()

for c in conversations:
    print(str(c))