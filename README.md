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
