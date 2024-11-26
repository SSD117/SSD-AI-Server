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

### API 명세서

**🚨 Local Server URL (Server Host) 🚨**

```
http://127.0.0.1:8000
```

**🌸 Overview**

| HTTP METHOD | End Point | Description |
| --- | --- | --- |
| POST | / | 추천 결과 전송 및 조회 |

---

### AI 설문조사 전송 및 조회 (POST / )

| 컬럼 한글명 | 컬럼 영문명 | 데이터 타입 | 필수여부 | 데이터 예시 |
| --- | --- | --- | --- | --- |
| 운동 선호도 | preference | number | Y | 10 |
| 운동 강도 | intense | number | Y | 5 |
| 운동 주당 빈도(정기성) | frequency | number | Y | 5 |
| 운동 친구 유무 | friend | number | Y | 10 |
| 운동 목표 | goal | number | Y | 10 |
| 운동 방식 | method | number | Y | 10 |
| 활동성 | activity | number | Y | 5 |
| 실내 vs 실외 | place | number | Y | 10 |
| 운동 시간대 | time | number | Y | 5 |
| 운동 종류 | type | number | Y | 10 |

**📌 Request Body**

```json
{
	"preference": 10,
	"intense": 5,
	"frequency": 5,
	"friend": 10,
	"goal": 10,
	"method": 10,
	"activity": 5,
	"place": 10,
	"time": 5,
	"type": 10
}
```

**📌 Server Response**

✅ Success

```json
{
  "status": 201,
  "sports": ["철인반", "순환운동", "체조", "장애인스포츠"]
}
```

❌ Error

```json
{
  "status": 400,
  "error": "AI 설문조사 전송 실패"
}
```
