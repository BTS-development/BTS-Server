# BTS-Server

한전KDN, 2020 빛가람 에너지밸리 소프트웨어 작품 경진대회 출전작품

## 개발 스택
- **개발** : Django
- **배포** : AWS EC2, RDS, Docker
- **DB** : MySQL
- **기타** : ubuntu

## 사용법
`root`디렉터리 에 진입해서 `python ./src/manage.py runserver`를 입력한다.
그리고 아래의 route들의 형식에 맞게 요청을 한다.
## User

- GET /users/{user_id}: 회원 정보 with JWT Token

    ```bash
    response
    {
        "pk": 11,
        "username": "habi",
        "email": "gkql0128@naver.com"
    }
    ```

- POST /users/account/signup:회원가입 API

    ```json
    request
    {
        "username": "hanbin2",
        "email": "gksqls01281@naver.com",
        "password1": "0128gksqls",
        "password2":"0128gksqls"
    }
    ```

    ```json
    response
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJ1c2VybmFtZSI6ImdrcWwxMmFzYXNkZDAxMjhAbmF2ZXIuY29tIiwiZXhwIjoxNjAwMDgxNTMyLCJlbWFpbCI6ImdrcWwxMmFzYXNkZDAxMjhAbmF2ZXIuY29tIiwib3JpZ19pYXQiOjE2MDAwODEyMzJ9.iieXoCKO-9cEJDDF4l_RWTzqBRDC17pwK85HsIhEtcc",
        "user": {
            "pk": 1,
            "username": "hanbin",
            "email": "gksqls0128@naver.com"
        }
    }
    ```
    - POST /users/account/login: 로그인 API

    ```json
    request
    {
        "email": "gksqls0128@naver.com",
        "password" : "0128gksqls"
    }
    ```

    ```json
    response
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMCwidXNlcm5hbWUiOiJna3NxbHMwMTI4QG5hdmVyLmNvbSIsImV4cCI6MTYwMDE1NjcyNywiZW1haWwiOiJna3NxbHMwMTI4QG5hdmVyLmNvbSIsIm9yaWdfaWF0IjoxNjAwMTU2NDI3fQ.VA7Zk7Od5RbED2DD_CvSQpEPSDyyAyxVKW_u6t99oXs"
    }
    ```
    ## Group

- POST /groups/ : 그룹 생성

    ```json
    -request-
    {
    	"name":"그룹명"
    }

    -response-
    {
        "id": 그룹아이디,
        "name": "그룹명",
        "code": "그룹코드",
        "created_at": "그룹생성일",
        "owner": 그룹장아이디
    }
    ```

- POST /groups/join : 그룹 가입

    ```json
    -request-
    {
    	"code":"그룹코드"
    }
    -response-
    {
        "id": 1,
        "joined_at": "2020-09-15",
        "group": 1,
        "member": 11
    }
    ```

- GET /groups/mygroup : 가입 그룹 조회

    ```bash
    [
        {
            "id": 1,
            "name": "hanbin-test",
            "code": "SYVVLSS2",
            "created_at": "2020-09-15",
            "owner": 10
        },
    		{
            "id": 2,
            "name": "asd-test",
            "code": "asdaf",
            "created_at": "2020-09-15",
            "owner": 10
        }
    ]
    ```

- GET /groups/ : 생성 그룹 조회

    위와 동일

- GET /groups/{group_id} : 해당 그룹 멤버 리스트

    ```json
    [
    	{
    	    "pk": 11,
    	    "username": "habi",
    	    "email": "gkql0128@naver.com"
    	},
    	{
    	    "pk": 11,
    	    "username": "habi",
    	    "email": "gkql0128@naver.com"
    	},
    	{
    	    "pk": 11,
    	    "username": "habi",
    	    "email": "gkql0128@naver.com"
    	}
    ]
    ```

## Temperature

- POST /temperatures : 체온 전송

    ```bash
    request
    {
        "value":36.5
    }
    ```

    ```bash
    response
    {
        "id": 1,
        "value": 36.5,
        "created_at": "2020-09-15",
        "owner": 10
    }
    ```

- GET /temperatures/{user_id} : 체온 정보

    ```bash
    response
    {
        "id": 1,
        "value": 36.5,
        "created_at": "2020-09-15",
        "owner": 10
    }
    ```

- GET /temperatures/my/: 나의 체온정보 기록들 모두

    ```bash
    response
    [
        {
            "id": 1,
            "value": 36.5,
            "created_at": "2020-09-15",
            "owner": 10
        },
    		{
            "id": 2,
            "value": 23.5,
            "created_at": "2020-09-15",
            "owner": 10
        }
    ]
    ```

- GET /temperatures/group/{group_id} : 해당 그룹의 체온정보 기록들 모두

    ```bash
    response
    [
        {
            "id": 1,
            "value": 36.5,
            "created_at": "2020-09-15",
            "owner": 11
        },
    		{
            "id": 2,
            "value": 36.5,
            "created_at": "2020-09-15",
            "owner": 11
        }
    ]
    ```
