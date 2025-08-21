import requests

# Example URL
url = "https://jsonplaceholder.typicode.com/todos/1"

# Send GET request
response = requests.get(url)

# Print response status and content
print("Status code:", response.status_code)
print("Response body:", response.json())