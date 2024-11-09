# SSD-AI-Server

## **기능**

머신러닝 알고리즘을 활용하여 사용자에게 맞춤형 체육 활동을 추천.

**세부 사항**

- **추천 알고리즘**: 사용자의 신체 데이터와 성향 데이터를 분석하여 적합한 운동 추천.
- **스포츠 강좌 연계**: 초반은 위치 기반으로 제공, 시간 가용시 추천된 운동에 해당하는 강좌나 이용 가능한 스포츠 강좌 이용권과 연계하여 제공.

---

## 사용 프레임워크

1. fastapi
2. scikit-learn
3. docker

---

## **실행 방법**

### **git clone**

```
git clone https://github.com/SSD117/SSD-AI-Server.git
```

### **AI Server Start**

```
docker compose up
```

### **Iocalhost**

```
http://localhost:8000
```

### **API 명세서**

```
http://localhost:8000/redoc
```

---

## 해야할 일

- [x]  fastapi & docker 세팅
- [ ]  사용할 추천 모델 선택하기
- [ ]  사용자 맞춤 데이터 설문 완성하기
- [ ]  운동 종류별로 분류하기
- [ ]  모델 설계 후 테스트

---

### API 명세서(v1)

**🌸 Overview**

| HTTP METHOD | End Point | Description |
| --- | --- | --- |
| POST | /v1/user | 유저 정보 전송 |
| POST | /v1/recommendation | 추천 결과 조회 |

---

유저 정보 전송 (POST /v1/user)

**📌 Request Body**

```json
{
  "username": "잼민이",
  "age": 13,
  "gender": "m",
  "height": 160,
  "weight": 50,
  "preference": "solo" or "team",
  "frequency": 3,
  "intensity": "low" or "high",
  "goal": ""
  ...
}
```

**📌 Server Response**

✅ Success

```json
{
  "status": 200,
  "message": "성공"
}
```

❌ Error

```json
{
  "status": 400,
  "error": "유저 정보가 잘못 입력 되었습니다"
}
```

---

추천 결과 조회 (POST /v1/recommendation)

**📌 Request Body**

```json
{
	"username": "잼민이"
}
```

**📌 Server Response**

✅ Success

```json
{
  "status": 200,
  "sports": ["축구", "야구", "아이스하키", "헬스"],
  "coures": ["축구 자세 강좌", "야구 변화구 던지는 법". "데드리프트 맛있게 먹는법"]
}
```

❌ Error

```json
{
  "status": 400,
  "error": "추천받을 유저가 존재하지 않습니다"
}
```

---