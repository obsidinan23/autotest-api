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
    print("User created successfully. Current email:", user_create_response_data['user']['email'])
else:
    print("User creation failed")


user_login_payload = {
  "email": user_create_payload["email"],
  "password": user_create_payload["password"],
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=user_login_payload)

if login_response.status_code == 200:
    print("Login success")
    print()
else:
    print("Login failed")


update_user_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
headers = {"Authorization": f'Bearer {login_response.json()['token']['accessToken']}'}
update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_create_response_data["user"]["id"]}", json=update_user_payload, headers=headers)

print("Update result:")
print(update_user_response.status_code)
print(update_user_response.json())
