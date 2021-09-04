import requests, json


headers = {"Content-Type": "application/json"}

base_url = "http://127.0.0.1:5000/"

conversion_url = base_url + '/conversion'
request_data = {
    "conversion_id": 123,
    "conversion_name": "testst"
}

res = requests.post(conversion_url, headers=headers, data=json.dumps(request_data))

print(res.json())