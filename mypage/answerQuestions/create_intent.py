import dialogflow_v2 as dialogflow
import os


GOOGLE_AUTHENTICATION_FILE_NAME = "kobaksa.json"
current_directory = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
intents_client = dialogflow.IntentsClient()
parent = intents_client.project_agent_path('kobaksa-1b59d')


def create_intent(question, answer,q_id):
  #dialogflow_setting()

    #text phrases에 문제 추가
  """part = dialogflow.types.Intent.TrainingPhrase.Part(
    text = "유소영의 테스트")"""
  part = dialogflow.types.Intent.TrainingPhrase.Part(
      text=question)
  training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])

  messages = []

  #이게 default message
  #text = dialogflow.types.Intent.Message.Text(text = ["First message2"])#responses에 답변 추가
  text = dialogflow.types.Intent.Message.Text(text=[answer])  # responses에 답변 추가
  text_message = dialogflow.types.Intent.Message(text=text)
  messages.append(text_message)

  # 이미지로 답변 가능하도록
  """image = dialogflow.types.Intent.Message.Image(image_uri="https://s3.amazonaws.com/com.niches.production/niche_pages/square_images/000/001/619/giantc/sous-vide-ribeye-white-bean-puree-17.jpg")
  image_message = dialogflow.types.Intent.Message(image=image)
  messages.append(image_message)"""

  # 요거는 빠른 대답 가능하도록!
  """quick_reply = dialogflow.types.Intent.Message.QuickReplies(
      title="Reply Prompt",
      quick_replies=["reply1", "reply2"])
  quick_reply_message = dialogflow.types.Intent.Message(quick_replies=quick_reply)
  messages.append(quick_reply_message)"""
  intentN="UQ"
  intentN=intentN+str(q_id)

  intent = dialogflow.types.Intent(
      #display_name = "Jason's New Intent22",
      display_name=intentN,
      training_phrases = [training_phrase],
      messages = messages
  )

  response = intents_client.create_intent(parent, intent)

# 매개변수 설정해서 코드 수정 필요
# 해당 인텐트에 trainging phrases 추가하기
# 이와 같이 코드로 default 답을 수정 할 수도 있을듯

def update_intent(question, answer, q_id):
  #dialogflow_setting()
  intentN="UQ"
  intentN=intentN+str(q_id)


  intents=intents_client.list_intents(parent)
  intent_path=[
      intent.name for intent in intents
      #if intent.display_name=="getDataFromMySQL"
      if intent.display_name == intentN
  ]
  print(intent_path)
  training_phrases = []
  intent= intents_client.get_intent(intent_path[0], intent_view=dialogflow.enums.IntentView.INTENT_VIEW_FULL)
  #intent = intents_client.get_intent(intent_path[0])

  """part = dialogflow.types.Intent.TrainingPhrase.Part(
      text = "업뎃 확인")"""
  part = dialogflow.types.Intent.TrainingPhrase.Part(
      text=question)
  training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
  training_phrases.append(training_phrase)
  # training_phrases가 여러개일 경우
  '''for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)'''

  messages = []

  # 이게 default message
  # text = dialogflow.types.Intent.Message.Text(text = ["First message2"])#responses에 답변 추가
  #text = dialogflow.types.Intent.Message.Text(text=[answer])  # responses에 답변 추가
  #text_message = dialogflow.types.Intent.Message(text=text)

  text = dialogflow.types.Intent.Message.Text(text=[answer])  # responses에 답변 추가
  text_message = dialogflow.types.Intent.Message(text=text)
  # 이전 답 제거
  intent.messages.pop()
  messages.append(text_message)


  intent.training_phrases.extend(training_phrases)
  intent.messages.extend(messages)
  #dialogflow.types.Intent.Message=messages

  #---------------추가
  """intent = dialogflow.types.Intent(
      # display_name = "Jason's New Intent22",
      display_name=intentN,
      training_phrases=[training_phrase],
      messages=messages
  )"""



  response  = intents_client.update_intent(intent, language_code='ko')

# 저장된 entity 목록 불러오기
def get_entity_list():
    entity_type_client = dialogflow.EntityTypesClient()
    parent = entity_type_client.project_agent_path('kobaksa-1b59d')

    entity_types = entity_type_client.list_entity_types(parent)

    for entity_type in entity_types:
        print(entity_type)
        #print(entity_type.name)
        #print(entity_type.display_name)
        
        # entity에서 value 값 출력하기
        #entities = entity_type.entities
        #entity_values = [entity.value for entity in entities]
        #for enti in entity_values:
            #print(enti, "\n")
            
