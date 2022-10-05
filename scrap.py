import requests
r = requests.get('https://gaurav-api-practice.herokuapp.com/signals/?username=gaurav&password=gaurav1997')
print(r.json())