import http.client

conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
ip = conn.getresponse().read()
fixed = ip.decode("utf-8").strip()
# print (fixed)

import requests

def get_user_region(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json?lang=ru")
        data = response.json()
        return data.get("region")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return None

user_region = get_user_region(fixed)

if user_region:
    print(f"Ваш регион: {user_region}")
else:
    print("Не удалось определить регион.")