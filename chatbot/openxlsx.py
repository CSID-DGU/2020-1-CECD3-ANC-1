# -*- coding: utf-8 -*-
import openpyxl


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
    
wb = openpyxl.load_workbook(u"qnalist.xlsx")

ws = wb.active

conversations = []

#시트내 존재하는 모든 데이터 객체로 담음
for r in ws.rows:
    c = Conversation(r[0].value, r[1].value, r[2].value, r[3].value)
    
    conversations.append(c)

wb.close()

for c in conversations:
    print(str(c))