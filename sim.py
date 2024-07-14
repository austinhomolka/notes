import requests

# URL to send the request to
url = "https://web-production-2a58d.up.railway.app"

# Headers to simulate an iPhone 8 Plus client
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}

# Send the request
response = requests.get(url, headers=headers)

# Print the response
print("Status Code:", response.status_code)
# print("Response Text:", response.text)
print("Response Content: ", response.content)