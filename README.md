# 원격강의를 위한 보조 챗봇 시스템

## 팀명
익명의 냥고양이 (Anonymous Nyan Cat)
## 팀원
김영미 (0meeee)
문예진 (yejindaye)
유소영 (wka99)
이민주 (Minjoo-L)

## 설치하기
### [시스템 실행]
1. Python 설치
- Windows 10에 맞는 Python 3.x 버전을 설치한다. 
- 설치과정에서 Add Python 3.5 to PATH를 체크하여 cmd창의 모든 경로상에서 Python 명령어를 사용할 수 있도록 한다. 
- 설치가 완료되면 cmd창에서 다음 명령어로 실행되는지 확인한다.
```sh
pip -V
```

2. Django 설치
Python를 설치한 다음 cmd 창에서 다음 명령어를 입력하여 Django를 설치한다. 
```sh
pip install django
```

3. 시스템 실행
- https://github.com/CSID-DGU/2020-1-CECD3-ANC-1에서 프로젝트 폴더를 원하는 경로에 다운받는다.
- 2020-1-CECD3-ANC-1/mypage/mypage 경로에 my_settings.py 파일을 추가하여 AWS EC2 ubuntu 18.04에 설치된 moodle MySQL 데이터베이스를 시스템과 연동한다. 아래 그림은 my_setting.py 이다. 각 필드에 해당되는 값을 입력한다.
<img width="361" alt="DB" src="https://user-images.githubusercontent.com/45723998/102689223-b9a67980-423f-11eb-9caa-eb4de3a3ade7.png">
- 2020-1-CECD3-ANC-1/mypage/chatbot 경로에 .json의 확장자를 갖는 Dialogflow 에이전트의 키 파일을 추가한다.
- 2020-1-CECD3-ANC-1/requirements.txt 파일에 작성된 라이브러리를 설치하기 위해 cmd창에 다음 명령을 입력한다.
```sh
pip3 install -r requirements.txt
```
- 다음 명령으로 서버를 구동시킨후 http://127.0.0.1:8000/mypage 로 접속한다.
```sh
python3 manage.py runserver
```

### [AWS EC2 ubuntu 18.04 에 Moodle MySQL 데이터베이스 설치]
1. AWS EC2 ubuntu 18.04 생성
- AWS EC2 ubuntu 18.04 인스턴스를 생성하고 인바운드 규칙에 포트번호 3306을 추가한다.

2. Moodle 설치
- Moodle MySQL을 사용하기위해 Moodle을 설치한다.
- /etc/mysql/mysql.conf.d/mysqld.cnf 경로로 이동하여 bind-address를 0.0.0.0으로 수정한다. 
- 그 후 다음 명령어를 순서대로 입력하여 외부에서 접근 가능하도록 한다.
```sh
sudo service mysql restart
```
```sh
GRANT ALL PRIVILEGES ON *.* TO ‘root’@’%’ IDENTIFIED BY ‘mysql 설치시 설정한 비밀번호';
```

3. Moodle MySQL 데이터베이스 설계
- 기존 데이터베이스에 생성되어 있는 mdl_user, mdl_role_assignments, mdl_user_enrolments, mdl_enrol, mdl_course 테이블을 사용한다.
- 다음 사진을 참고하여 learningLevel_homework, s_comment, indexKeyword, question 테이블을 추가 생성한다.
<img width="750" alt="tables" src="https://user-images.githubusercontent.com/45723998/102689293-49e4be80-4240-11eb-8000-7398965b2517.png">

### [Moodle MySQL 데이터베이스와 Dialogflow 연동]
1. kobaksa 에이전트 추가
- Github에서 다운 받은 kobaksa 에이전트를 자신의 Dialogflow에 import한다. 

2. kobaksa와 Moodle MySQL 데이터베이스 연동
- kobaksa 에이전트의 Fulfillment의 Inline Editor에서 index.js에 아래 코드를 추가한다.
<img width="343" alt="db_1" src="https://user-images.githubusercontent.com/45723998/102689278-33d6fe00-4240-11eb-9052-ff9cd59c0467.png">

3. 파일 내 코드 수정
- 2020-1-CECD3-ANC-1/mypage/chatbot/views.py에서 GOOGLE_AUTHENTOCATION_FILE_NAME 변수 값을 2020-1-CECD3-ANC-1/mypage/chatbot 경로에 .json의 확장자를 갖는 Dialogflow kobaksa 에이전트의 키 파일명으로 한다.
- GOOGLE_PROJECT_ID 변수 값도 알맞게 수정한다.
