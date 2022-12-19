import requests
import json
url = 'http://8655-35-197-110-255.ngrok.io/predict'
j = {"1": "Everything in the world is are fine"}

print("Enter english Statement and enter exit if you want to stop")

while(1):
    print("-"*50)
    inp = raw_input()
    if (inp == "exit"):
        break
    j["1"] = inp
    r = requests.post(url, json=j)
    print(r.json())




# print(r.json())