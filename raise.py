import requests

URL='http://ip.taobao.com/service/getIpInfo.php'	#the ip resouces frome taobao
try:
	r=requests.get(URL,params={'ip':'8.8.8.8'},timeout=1)
	r.raise_for_status() #if code !=200 throw exceptions
except requests.RequestException as e:
	print(e)
else:
	result=r.json()
	print(type(result),result)
