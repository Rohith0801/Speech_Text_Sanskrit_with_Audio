import urllib3

http = urllib3.PoolManager()
r = http.request('get', 'https://translate.google.co.in/?sl=en&tl=sa&text=dharmasya%20glanir%20bhavati%20Bharata',timeout=10)

with open('page_source.html', 'w') as fid:
    print(r.data)