import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "ph": 7.2,
    "Hardness": 180,
    "Solids": 21000,
    "Chloramines": 7.5,
    "Sulfate": 360,
    "Conductivity": 580,
    "Organic_carbon": 10.0,
    "Trihalomethanes": 82,
    "Turbidity": 3.1
}

response = requests.post(url, json=data)
print(response.json())
