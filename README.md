# FanFixiv 관리자 서버

> 현재 더이상 개발이 진행되지 않습니다.

## 컨벤션

```
# 파일, 변수, 함수
snake_case
# 클래스명
CamelCase
# db
snake_case (테이블 앞에는 무조건 tb_를 붙입니다)
```

## 기술 스택

- Python 3.9
- FastAPI

## 설치

```
./docker-install.sh
```

## 실행

```
Local 환경

docker-compose up -d

```

## 빌드

> 관리자 서버의 경우 따로 빌드 과정이 존재하지 않습니다.

## 테스트

> 테스트의 경우 e2e 테스트만 작성합니다.

```
pytest
```
