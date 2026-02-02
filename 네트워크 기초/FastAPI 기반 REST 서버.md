# FastAPI 기반 REST 서버

## 📁 프로젝트 구조 업데이트

```
network-practice/
│
├── 05_fastapi_server/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── requirements_fastapi.txt
│
└── ...
```

---

# 📌 1. FastAPI 서버 전체 코드

## 📄 `main.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Network Practice REST API")

# 데이터 모델
class Item(BaseModel):
    id: int
    name: str
    price: float

# 메모리 DB
items_db: List[Item] = []

@app.get("/")
def root():
    return {"message": "FastAPI REST Server Running!"}

@app.get("/items")
def get_items():
    return items_db

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items")
def create_item(item: Item):
    items_db.append(item)
    return {"message": "Item added", "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items_db
    items_db = [item for item in items_db if item.id != item_id]
    return {"message": "Item deleted"}
```

---

# 📄 `models.py` (선택사항)

```python
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
```

---

# 📄 `database.py` (선택사항)

```python
from typing import List
from models import Item

items_db: List[Item] = []
```

---

# 📄 `requirements_fastapi.txt`

```txt
fastapi
uvicorn
```

---

# 🏃‍♂️ 2. FastAPI 서버 실행 방법

프로젝트 루트에서:

```bash
pip install -r 05_fastapi_server/requirements_fastapi.txt
```

서버 실행:

```bash
uvicorn 05_fastapi_server.main:app --reload
```

---

# 🌐 3. API 테스트 방법

FastAPI는 자동으로 **Swagger UI**를 제공해.

브라우저에서 아래 주소로 접속:

```
http://127.0.0.1:8000/docs
```

여기서 GET/POST/DELETE 요청을 바로 테스트할 수 있어.

---

# 📌 4. 제공되는 API 목록

| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | `/` | 서버 상태 확인 |
| GET | `/items` | 모든 아이템 조회 |
| GET | `/items/{id}` | 특정 아이템 조회 |
| POST | `/items` | 아이템 추가 |
| DELETE | `/items/{id}` | 아이템 삭제 |

---

# 🎯 jong을 위한 마무리

이제 네 프로젝트는:

- TCP/UDP 소켓
- HTTP 요청
- REST API 클라이언트
- 웹 스크레이핑
- Selenium 자동화
- **FastAPI 기반 REST 서버**
