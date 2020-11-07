from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import dialogflow
import os
import json
from django.views.decorators.csrf import csrf_exempt
from learningLevel.models import *
# Create your views here.

@require_http_methods(['GET'])
def index_view(request):
    return render(request, 'index3.html')

def convert(data):
    if isinstance(data, bytes):
        return data.decode('utf-8')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data

@csrf_exempt
@require_http_methods(['POST'])
def chat_view(request):
    print('Body', request.body)
    input_dict = convert(request.body)
    input_text = json.loads(input_dict)['text']

    GOOGLE_AUTHENTICATION_FILE_NAME = "kobaksa.json"
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path

    GOOGLE_PROJECT_ID = "kobaksa-1b59d"
    session_id = "1234567891"
    context_short_name = "does_not_matter"

    context_name = "projects/" + GOOGLE_PROJECT_ID + "/agent/sessions/" + session_id + "/contexts/" + \
               context_short_name.lower()

    parameters = dialogflow.types.struct_pb2.Struct()

    context_1 = dialogflow.types.context_pb2.Context(
        name=context_name,
        lifespan_count=2,
        parameters=parameters
    )
    query_params_1 = {"contexts": [context_1]}

    language_code = 'ko'
    
    response = detect_intent_with_parameters(
        request=request,
        project_id=GOOGLE_PROJECT_ID,
        session_id=session_id,
        query_params=query_params_1,
        language_code=language_code,
        user_input=input_text
    )
    
    return HttpResponse(response.query_result.fulfillment_text, status=200)

def detect_intent_with_parameters(request, project_id, session_id, query_params, language_code, user_input):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversaion."""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    text = user_input

    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input,
        query_params=query_params
    )

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))

    #ask, CH, UQ 관련 인텐트 일때만 참여도 점수 +1
    if "ask" in response.query_result.intent.display_name or "CH" in response.query_result.intent.display_name or "UQ" in response.query_result.intent.display_name:
        # 여기에 해당 학생 참여도 점수에 +1 하는 코드 작성.
        enrolid=(MdlEnrol.objects.get(courseid=4,enrol='manual')).id
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        uinstance = MdlUserEnrolments.objects.filter(enrolid=enrolid, userid=userid)[0]
        uinstance.grade = uinstance.grade+1
        uinstance.save()

    # Default Fallback Intent일 때 
    if response.query_result.intent.display_name == "Default Fallback Intent":
        # 질문 entity, page 예시
        entity = "오토마타"
        page = "1"
        # if문: mysql에 분류해서 얻은 단어 페이지가 있어서 제공해줄 수 있는경우.. 이 반대의 경우는 코드 작성할 필요X
        # 밑에 답도 예시
        response.query_result.fulfillment_text = " 무슨 말인지 잘 모르겠네요.." +entity+"는 "+ page+"페이지 설명을 참고해보세요. 참고해도 모르겠다면 미해결 질문답변 게시판에 미해결 질문으로 등록해주세요. 하시겠어요?"
    
    #사용자가 '응' 이라고 답하여 미해결 질문 게시판으로 이동
    if response.query_result.intent.display_name == "Default Fallback Intent - yes":
        response.query_result.fulfillment_text = "미해결 질문 게시판 url제공"
    return response

def index3(request):
    if request.session.get('user',False) :
        user=(MdlUser.objects.get(username=request.session.get('user',False)))
        userid=user.id
        if MdlRoleAssignments.objects.filter(userid=userid, roleid=5):
            enrolList=MdlEnrolFlatfile.objects.filter(userid=userid)
            return render(request, 'chatbot/index3.html',{'enrolList':enrolList})
        else :
            return render(request, 'chatbot/index3.html')
    return render(request, 'signin.html')
