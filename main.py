import requests
import smtplib

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

querystring = {"lat":"19.033049","lon":"73.029663"}

headers = {
	"X-RapidAPI-Key": "f2b1123709msh2a86b29c16fae58p10b040jsn7d22ba3230b8",
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()

weather = response['data'][1]['weather']
description = weather['description']
code = weather['code']
my_mail = "YouMAil"
my_password = "YOurPassword"
if int(code) <= 650:
	connection = smtplib.SMTP('smtp.gmail.com')
	connection.starttls()
	connection.login(user=my_mail, password=my_password)
	connection.sendmail(from_addr=my_mail, to_addrs=my_mail, msg=f"SUBJECT:IT MIGHT RAIN\n\n"
																 f"Take an umbrella it is {description}")
	connection.close()


