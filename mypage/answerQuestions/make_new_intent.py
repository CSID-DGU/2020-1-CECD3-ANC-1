# -*- coding: utf-8 -*-
import dialogflow_v2 as dialogflow
import os
from konlpy.tag import Kkma
from konlpy.utils import pprint


def dialogflow_setting():
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

  for entity_type in entity_types:
    #print(entity_type)
    # print(entity_type.name)
    # print(entity_type.display_name)
      
    #entity에서 value 값 출력하기
    entities = entity_type.entities
    # entity_values = [entity.value for entity in entities]
    entity_synonyms = [entity.synonyms for entity in entities]

    keys.append(entity_type.display_name) 

    #dic = dict.fromkeys(keys,entity_synonyms) 
    dic = dict.fromkeys(keys) 

  #print(dic)
  return dic    
  
####2. 입력값에 영어+한글 혼합인 경우가 많다... 심지어 딕셔너리의 키(entity의 display name)는 전부 영어 > nouns 대신 Pos로 대체
def set_intent_entity():
  
  entity_type_client = dialogflow.EntityTypesClient()
  parent = entity_type_client.project_agent_path('kobaksa-1b59d')
  entity_types = entity_type_client.list_entity_types(parent)
  intents_client = dialogflow.IntentsClient()
  
  training_phrases = []

  dic = get_entity_list()
  #print(dic, "\n")
  
  input = "Fruit 아침형 인간이라 새벽에는 아주 졸리네요"

  kkma = Kkma()
  input_tag = kkma.pos(input)

  for it in input_tag:
    if it[0] in dic.keys():
      et = "@" + it[0] + ":" + it[0]
      
####3. entity 부분적으로 설정 어떻게행.. 꼭 해야하나?
  part = dialogflow.types.Intent.TrainingPhrase.Part(text=input, entity_type=et)
  # #part = dialogflow.types.Intent.TrainingPhrase.Part(text=training_phrases_part, entity_type='@sys.given-name', alias='name')
  # # Here we create a new training phrase for each provided part.
  training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
  training_phrases.append(training_phrase)

  messages = []

#default message 설정
  text = dialogflow.types.Intent.Message.Text(text=["나도 그래", "나도 졸려"])
  text_message = dialogflow.types.Intent.Message(text=text)
# messages.append(text_message)

  intent = dialogflow.types.Intent(
    display_name = "asking fruit",
    training_phrases=training_phrases,
    messages=[text_message],
    # webhook_state = 'WEBHOOK_STATE_ENABLED'
    # training_phrases = [training_phrase],
    # messages = messages
  )

  try:
    response = intents_client.create_intent(parent, intent)
    #response = client.create_entity_type(parent, entity_type)
  except InvalidArgument:
    raise
# print('Intent created: {}'.format(response))


set_intent_entity()
#get_entity_list()


### 반쪽짜리 성공
def test_set_entity():
  parts = [
    dialogflow.types.Intent.TrainingPhrase.Part(text="오토마타", entity_type='@automata'),
    dialogflow.types.Intent.TrainingPhrase.Part(text="가 뭐야?")
  ]

  training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=parts)

  messages = []

  #이게 default message
  text = dialogflow.types.Intent.Message.Text(text = ["First message"])
  text_message = dialogflow.types.Intent.Message(text=text)
  messages.append(text_message)

  param = dialogflow.types.Intent.Parameter(
          display_name="automata",
          entity_type_display_name="@automata",
          mandatory=False,
          name="",
          value="$automata",
  )
  intent = dialogflow.types.Intent(
          display_name="aaaaaa",
          parameters=[param],
          training_phrases=[training_phrase],
          messages=messages,
  )

  response = intents_client.create_intent(parent, intent)
  print("Intent created: {}".format(response))
