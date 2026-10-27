import httpx

# "user": {
#     "id": "eac4add3-adb8-46b6-ac9b-bd014f311a80",
#     "email": "nan@test.com",
#     "password": "123",
#     "lastName": "lastname",
#     "firstName": "firstname",
#     "middleName": "middlename"
#   }

login_payload = {
  "email": "nan@test.com",
  "password": "123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Status code:", login_response.status_code)
print("Login response:",login_response_data)


refresh_payload = {"refreshToken": login_response_data['token']['refreshToken']}

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print("Status code:", refresh_response.status_code)
print("Refresh response:",refresh_response_data)

