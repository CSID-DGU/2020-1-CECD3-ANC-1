import dialogflow_v2 as dialogflow

intents_client = dialogflow.IntentsClient()
parent = intents_client.project_agent_path('kobaksa-1b59d')

part = dialogflow.types.Intent.TrainingPhrase.Part(
  text = "훈련할 문장(training phrases) 넣기!!")
training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])

messages = []

#이게 default message
text = dialogflow.types.Intent.Message.Text(text = ["First message"])
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
    messages = messages
)

response = intents_client.create_intent(parent, intent)
