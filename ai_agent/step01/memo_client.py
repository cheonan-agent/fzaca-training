# step01/memo_client.py
import requests

BASE = "http://127.0.0.1:8000"

r = requests.post(f"{BASE}/memos", json={"title": "출장 보고서", "content": "복귀 후 5영업일 이내 제출"}, timeout=5)
print(r.status_code, r.json())
requests.post(f"{BASE}/memos", json={"title": "연차 신청", "content": "사용일 3일 전까지 전자결재"}, timeout=5)

r = requests.get(f"{BASE}/memos", timeout=5)
print(r.status_code, [m["title"] for m in r.json()])

r = requests.get(f"{BASE}/memos", params={"keyword": "연차"}, timeout=5)
print(r.status_code, [m["title"] for m in r.json()])

r = requests.get(f"{BASE}/memos/1", timeout=5)
print(r.status_code, r.json()["title"])

r = requests.put(f"{BASE}/memos/1", json={"title": "출장 보고서", "content": "복귀 후 5영업일 이내, 팀장 결재"}, timeout=5)
print(r.status_code, r.json()["content"])

r = requests.delete(f"{BASE}/memos/2", timeout=5)
print(r.status_code)

r = requests.get(f"{BASE}/memos/2", timeout=5)
print(r.status_code, r.json())

r = requests.post(f"{BASE}/memos", json={"title": "", "content": "제목 없음"}, timeout=5)
print(r.status_code, r.json()["detail"][0]["msg"])