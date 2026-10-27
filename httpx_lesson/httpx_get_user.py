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
login_response_data = login_response.json()

print("Login data:", login_response_data)


get_user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

get_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_user_headers)
get_me_response_data = get_me_response.json()
print("ME Status code:", get_me_response.status_code)


get_user_by_id_response = httpx.get(f"http://localhost:8000/api/v1/users/{user_create_response_data['user']['id']}", headers=get_user_headers)
get_user_by_id_response_data = get_user_by_id_response.json()

print("USER Status code:", get_user_by_id_response.status_code)
print("Get user data:", get_user_by_id_response_data)


