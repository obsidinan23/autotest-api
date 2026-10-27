import httpx
from tools.fakers import get_random_email


user_create_payload = {
  "email": get_random_email(),
  "password": "123",
  "lastName": "lastname",
  "firstName": "firstname",
  "middleName": "middlename"
}

user_create_response = httpx.post("http://localhost:8000/api/v1/users", json=user_create_payload)
user_create_response_data = user_create_response.json()

if user_create_response.status_code == 200:
    print("User created successfully")
else:
    print("User creation failed")


user_login_payload = {
  "email": user_create_payload["email"],
  "password": user_create_payload["password"],
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=user_login_payload)

if login_response.status_code == 200:
    print("Login success")
else:
    print("Login failed")

token = login_response.json()["token"]["accessToken"]
headers = {"Authorization": f"Bearer {token}"}

user_delete_response = httpx.delete(f"http://localhost:8000/api/v1/users/{user_create_response_data["user"]["id"]}", headers=headers)
user_delete_response_data = user_delete_response.json()

print("User delete status code:", user_delete_response.status_code)
print()
print("Confirming deletion with GET deleted user by it's id...")


login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=user_login_payload)
if login_response.status_code == 401 and login_response.json()["detail"] == 'Invalid credentials':
    print("User not found. Deletion confirmed")
else:
    print("Unexpected response! Deletion is not confirmed.")
    print("Login status code:", login_response.status_code)
    print("Login response:", login_response.json())
