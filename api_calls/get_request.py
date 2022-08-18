from requests import request

response = request(
    "GET",
    "http://localhost:8080/login",
    headers={},
    json={
        "username": "mikello",
        "password": "1234"
    }
)

a = dict(response.json())
for k, v in a.items():
    if k == "blog":
        print("blog>>>>")
        q = dict(v)
        for i, j in q.items():
            print(f"{i} -> {j}")
        continue
    print(f"{k} -> {v}")
