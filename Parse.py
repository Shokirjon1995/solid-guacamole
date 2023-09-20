import requests

link = 'https://httpbin.org/post'
data = {"comments": "fast and fury",
    "custemail": "shio@gmail.com",
    "custname": "Ilon",
    "custtel": "78777777777",
    "delivery": "21:00",
    "size": "large",
    "topping": "cheese"}
response = requests.post(link, data = data)
print(response.status_code)