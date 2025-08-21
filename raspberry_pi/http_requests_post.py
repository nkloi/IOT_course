import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Example payload
data = {
    "title": "IoT Test",
    "body": "Hello from Raspberry Pi",
    "userId": 1
}

# Send POST request
response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response body:", response.json())