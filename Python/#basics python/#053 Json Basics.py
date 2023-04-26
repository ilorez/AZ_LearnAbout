import json
personal_data = '''
{
  "name": "zobair najdaoui",
  "country": "Maroc",
  "phone Number": "0615331474",
  "CIN": "EE672326",
  "age": 19
}
'''

data = json.loads(personal_data)
print(data)