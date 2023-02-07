import requests
import re

# my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
try:
    my_req = requests.get(input('Введите адрес сайта: '))
    if my_req.status_code == 200:
        data = my_req.text
        res = re.findall(r'<h3.*?>(.*?)</h3>', data)
        print(res)
    else:
        print(my_req)
except Exception as exc:
    print(exc)
