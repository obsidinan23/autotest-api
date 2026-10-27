import httpx
from tools.fakers import get_random_email

payload = {
  "email": get_random_email(),
  "password": "123",
  "lastName": "lastname",
  "firstName": "firstname",
  "middleName": "middlename"
}

response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())

# test.1793113126.8952103@test.com
