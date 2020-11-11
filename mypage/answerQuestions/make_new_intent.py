# -*- coding: utf-8 -*-
import dialogflow_v2 as dialogflow
import os
from konlpy.tag import Kkma
from konlpy.utils import pprint
import datetime

#def dialogflow_setting():
GOOGLE_AUTHENTICATION_FILE_NAME = "kobaksa.json"
current_directory = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
intents_client = dialogflow.IntentsClient()
parent = intents_client.project_agent_path('kobaksa-1b59d')

def create_intent():
    dialogflow_setting()

    part = dialogflow.types.Intent.TrainingPhrase.Part(text = "유소영의 테스트")
    training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])

    messages = []

  #이게 default message
    text = dialogflow.types.Intent.Message.Text(text = ["First message2"])
    text_message = dialogflow.types.Intent.Message(text=text)
    messages.append(text_message)

  # 이미지로 답변 가능하도록
    image = dialogflow.types.Intent.Message.Image(image_uri="https://s3.amazonaws.com/com.niches.production/niche_pages/square_images/000/001/619/giantc/sous-vide-ribeye-white-bean-puree-17.jpg")
    image_message = dialogflow.types.Intent.Message(image=image)
    messages.append(image_message)

  # 요거는 빠른 대답 가능하도록!
    quick_reply = dialogflow.types.Intent.Message.QuickReplies(
    title="Reply Prompt",
    quick_replies=["reply1", "reply2"])
    quick_reply_message = dialogflow.types.Intent.Message(quick_replies=quick_reply)
    messages.append(quick_reply_message)


    intent = dialogflow.types.Intent(
        display_name = "Jason's New Intent",
        training_phrases = [training_phrase],
        messages = messages)

    response = intents_client.create_intent(parent, intent)

# 매개변수 설정해서 코드 수정 필요
# 해당 인텐트에 trainging phrases 추가하기
# 이와 같이 코드로 default 답을 수정 할 수도 있을듯
def update_intent():
    dialogflow_setting()

    intents=intents_client.list_intents(parent)
    intent_path=[
        intent.name for intent in intents
        if intent.display_name=="getDataFromMySQL"
    ]
    print(intent_path)
    training_phrases = []
    intent= intents_client.get_intent(intent_path[0], intent_view=dialogflow.enums.IntentView.INTENT_VIEW_FULL)
  #intent = intents_client.get_intent(intent_path[0])

    part = dialogflow.types.Intent.TrainingPhrase.Part(
        text = "업데이트 확인입니다!!!!")
    training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
    training_phrases.append(training_phrase)
  # training_phrases가 여러개일 경우
    '''for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)'''
    intent.training_phrases.extend(training_phrases)
    response  = intents_client.update_intent(intent, language_code='ko')




###1. 딕셔너리의 키 값으로 display_name 을, 값으로 동의어를 넣을 생각인데, 값에 각각의 리스트가 안들어감,,
# 저장된 entity 목록 불러오기
def get_entity_list():

  dic = {}  #entity 목록 저장할 딕셔너리 
  keys = [] #딕셔너리의 key값 저장할 리스트

  entity_type_client = dialogflow.EntityTypesClient()
  parent = entity_type_client.project_agent_path('kobaksa-1b59d')
  entity_types = entity_type_client.list_entity_types(parent)
  #print('entity_types')
  #print(entity_types)
  count=0

  for entity_type in entity_types:
    #print(entity_type)
    # print(entity_type.name)
    # print(entity_type.display_name)
    #print('entity_type')
    #print(entity_type)
    #print('entity_type.name')
    #print(entity_type)
      
    #entity에서 value 값 출력하기
    entities = entity_type.entities
    #print('entities')
    #print(entities)
    # entity_values = [entity.value for entity in entities]
    entity_synonyms = [entity.synonyms for entity in entities]
    #print('entitiy_synonyms')
    #print(entity_synonyms)
    #print('entity_synonyms[0]')
    #print(entity_synonyms[0])

    keys.append(entity_type.display_name)
    #print('keys')
    #print(keys)
    #print('keys[count]')
    #print(keys[count])

    #dic = dict.fromkeys(keys,entity_synonyms) 
    #dic = dict.fromkeys(keys)
    dic[keys[count]]=entity_synonyms
    #print('dic',dic)

    #print('dic[compiler]',dic['compiler'])

    count=count+1
#key-value로 저장된 값 출력
  #print('dic',dic)
  #print(dic)
  return dic    

  

##문장에서 단어로 entity 설정
# def test_set_entity():
#   parts = [
#     dialogflow.types.Intent.TrainingPhrase.Part(text="오토마타", entity_type='@automata',alias="automata"),
#     dialogflow.types.Intent.TrainingPhrase.Part(text="가 뭐야?")
#   ]

#   training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=parts)

#   messages = []

#   #이게 default message
#   text = dialogflow.types.Intent.Message.Text(text = ["First message"])
#   text_message = dialogflow.types.Intent.Message(text=text)
#   messages.append(text_message)

#   intent = dialogflow.types.Intent(
#           display_name="aaaaaa",
#           training_phrases=[training_phrase],
#           messages=messages,
#   )

#   response = intents_client.create_intent(parent, intent)
#   print("Intent created: {}".format(response))


# 전체 엔티티 딕셔너리의 value 리스트에서 질문 띄어쓰기 단위로 자른것과 같은 거 찾아 새로운 딕셔너리(text_key) 생성   
# 실제로 dialogFlow와 연동해 새로운 intent 저장하는 set_entity() 함수 호출
def reg_Intent_with_Entity(question, answer, q_id):
  entity_type_client = dialogflow.EntityTypesClient()
  parent = entity_type_client.project_agent_path('kobaksa-1b59d')
  entity_types = entity_type_client.list_entity_types(parent)
  intents_client = dialogflow.IntentsClient()
  
  training_phrases = []
  text_key = {}
  dic = get_entity_list()

  #input = "cross-compiler 아침형 인터프리터 새벽에는 아주 졸리네요"
  input = question
  #input_tag = input.split(" ")

  #영어 단어면 nouns에 안들어감, 따로 영어인 경우 더해줌
  
  #input_eng = kkma.pos(input)  
  # for it in input_eng:
  #   if it[1] in 'OL':
  #     input_tag.append(it[0])

  #morphs로 형태소분석
  kkma = Kkma()
  input_tag = kkma.morphs(input)

  # k : key 값, v : 2차원 리스트 value 저장 
  for k,v in dic.items():
    for i in range(len(v)):         # 세로 크기
      for j in range(len(v[i])):    # 가로 크기
        #print(vals[i][j], end=' ')

        for it in input_tag:
          # 질문의 키워드를 동의어 리스트에서 찾았을 때 text_key에 저장
          # text_key 내 key > text : 찾은 entity의 키 값, text_key 내 value > ettt : entity 설정할 질문의 일부

          if it == v[i][j]:
            text_key[k] = it

  parts=[]
  messages = []
  count = 0

  #사용자의 질문에서 엔티티와 매핑되지 않는 부분
  plain_list = [] 
  plain_list_dic = {}
  plain_list.append(input)
  #print(plain_list)
  value_key = {}


  # k : 엔티티의 키, v : 질문 내 키워드 
  # value_key 에 키와 값 반대로 저장함
  # 엔티티로 설정할 v 를 기준으로 split()
  for k,v in text_key.items():
    value_key[v] = k
    for pl in plain_list:
      plain_list = pl.split(sep = v)
      plain_list_dic[v] = plain_list
 

  keyList = plain_list_dic.keys()
  for item in list(keyList):
    k = value_key[item]
    et = "@" + k
    parts.append(
      dialogflow.types.Intent.TrainingPhrase.Part(text=plain_list_dic[item][0])
    )
    parts.append(
      dialogflow.types.Intent.TrainingPhrase.Part(text=item, entity_type=et, alias=k)
    )
  parts.append(
    dialogflow.types.Intent.TrainingPhrase.Part(text=plain_list_dic[item][1])
  )

  training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=parts)

  #default message

  #text = dialogflow.types.Intent.Message.Text(text = ["scanner와 parser로 전단부를 구성하는 이유는 ~입니다"])
  #text = dialogflow.types.Intent.Message.Text(text = ["잘 되나요?"])
  text = dialogflow.types.Intent.Message.Text(text=[answer])

  text_message = dialogflow.types.Intent.Message(text=text)
  messages.append(text_message)

  now = datetime.datetime.now()
  dName = now.strftime("%Y%m%d_%H%M%S")

  intent = dialogflow.types.Intent(
          display_name="ask_" + dName,
          training_phrases=[training_phrase],
          messages=messages,
  )

  try:
    response = intents_client.create_intent(parent, intent)
  except InvalidArgument:
    raise

#reg_Intent_with_Entity()