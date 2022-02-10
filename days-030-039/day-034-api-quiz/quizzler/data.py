import requests


response_params = {
    "amount":10,
    "difficulty":"medium",
    "type":"boolean"
}

response = requests.get("https://opentdb.com/api.php", params = response_params)
response.raise_for_status()
data = response.json()

question_data = data["results"]

#question_data = [question for question in data["results"]]

# for _ in data["results"]:
#     question_data.append(_)
    
# print(question_data)