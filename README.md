# BTS-Server
2020 스마틴 앱 챌린지 출전작 "BTS(Bluetooth Temperature Submitter)"의 API서버입니다

## 실행 방법
`python src/manage.py runserver --settings="config.settings.<세팅 모드>"`

로 서버를 실행합니다

https://www.notion.so/API-569f68f03af642ab86e8e7d7dbb611c4
위 링크를 클릭하여 API 명세서를 보고 API를 사용합니다

## 개발 내역
### **로그인 / 회원가입 기능 개발**
- `Django`의 `User Model`을 커스텀하여 `email`를 기본키로 하는 Model 제작
- `Authentication` 방식을 `JWT` 사용
- `JSONWebTokenAuthentication` 을 직접 만들어 반환 자료형 변경
- `rest_framework_jwt` 라이브러리로 로그인 구현
- `rest_auth` 라이브러리로 회원가입 구현

### **체온 정보 CRUD 구현**

- `generics` 의 여러 view를 상속하여 제작
- `permissions.py` 파일을 만들어 그룹 관리자 권한 체크

### **배포 및 앱과 연동**

- 처음에는 `AWS EC2`에 `SCP`로 파일을 업로드해 배포했으나, 버전 관리의 필요성을 느껴 `Docker`로 변경
- `Notion`에 [API명세서](https://www.notion.so/API-569f68f03af642ab86e8e7d7dbb611c4)를 작성
- `Docker Hub`를 사용해 [버전 관리](https://hub.docker.com/repository/docker/gksqls0128/bts-webserver)
