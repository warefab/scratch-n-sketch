from requests import *

requests.post(url + 50)

if requests.status_codes == 200:
    print('success')
else:
    print('Fail')
