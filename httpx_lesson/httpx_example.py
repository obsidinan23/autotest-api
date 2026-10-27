import httpx

# response = httpx_lesson.get('https://jsonplaceholder.typicode.com/todos/1')
#
# print(response.status_code)
# print(response.json())
#
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
# response = httpx_lesson.post('https://jsonplaceholder.typicode.com/todos', json=data)
#
# print(response.status_code)
# print(response.json())
#
# data = {"username":"test", "password":"123456"}
# response = httpx_lesson.post('https://httpbin.org/post', json=data)
#
# print(response.status_code)
# print(response.json())
#
# headers = {"Authorization": "Bearer secret_token"}
# response = httpx_lesson.get('https://httpbin.org/get', headers=headers)
#
# print(response.request.headers)
# print(response.json())
#
# params = {"userId": 1}
# response = httpx_lesson.get('https://jsonplaceholder.typicode.com/todos', params=params)
#
# print(response.url)
# print(response.json())
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
#
# response = httpx_lesson.post('https://httpbin.org/post', files=files)
#
# print(response.json())
#
# with httpx_lesson.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response1.json())
# print(response2.json())
#
#
# client = httpx_lesson.Client(headers={"Authorization": "Bearer secret_token"})
# response = client.get("https://httpbin.org/get")
#
# print(response.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
    print(response.status_code)
except httpx.HTTPError as e:
    print(f"Ошибка запроса: {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout as e:
    print("Запрос превысил лимит времени")