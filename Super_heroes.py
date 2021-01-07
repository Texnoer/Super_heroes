import requests
response_Hulk = requests.get("https://superheroapi.com/api/2619421814940190/search/Hulk")
response_Captain = requests.get("https://superheroapi.com/api/2619421814940190/search/Captain America")
response_Thanos = requests.get("https://superheroapi.com/api/2619421814940190/search/Thanos")
id_Hulk = response_Hulk.json()['results'][0]['id']
id_Captain = response_Captain.json()['results'][0]['id']
id_Thanos = response_Thanos.json()['results'][0]['id']
print(f"id Thanos {id_Thanos},id Captain America {id_Captain},id Hulk {id_Hulk}")
powerstats_Thanos = requests.get(
  "https://superheroapi.com/api/2619421814940190/655/powerstats"
)
powerstats_Hulk = requests.get(
  "https://superheroapi.com/api/2619421814940190/332/powerstats"
)
powerstats_Captain = requests.get(
  "https://superheroapi.com/api/2619421814940190/149/powerstats"
)
intelligence_Thanos = powerstats_Thanos.json()['intelligence']
intelligence_Hulk = powerstats_Hulk.json()['intelligence']
intelligence_Captain = powerstats_Captain.json()['intelligence']
if int(intelligence_Captain)< int(intelligence_Hulk) > int(intelligence_Thanos):
  print ('The best intelligence Hulk')
elif int(intelligence_Captain) < int(intelligence_Thanos) > int(intelligence_Hulk):
  print('The best intelligence Thanos')
else:
  print('The best intelligence Captain')