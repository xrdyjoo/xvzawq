import requests, random
from threading import Thread
def run():
    while(True):
        headersx = {
            'user-agent': 'Dart/2.7 (dart:io)',
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
            'accept-encoding': 'gzip',
            'content-length': '149',
            'host': 'app.fanzy.io',
        }
        datax = {
            'user_id': '376709',
            'wallet_address': '4a0bab95009aef65b626215e52cb8069da30ad8f6278596c12e3e9c8739e3f68',
            'email': 'netwezen@gmail.com',
            'org_video_id': 'eIAH-7dXt-Q'
        }
        responses = requests.post('https://app.fanzy.io/video_view/request', headers=headersx, data=datax)
        responsex = responses.json()
        headers = {
            'user-agent': 'Dart/2.7 (dart:io)',
            'coding': 'gzip',
            'content-length': '188',
            'host': 'app.fanzy.io',
        }
        data = {
            'user_id': '376709',
            'hash': '4a0bab95009aef65b626215e52cb8069da30ad8f6278596c12e3e9c8739e3f68',
            'email': 'netwezen@gmail.com',
            'org_video_id': 'eIAH-7dXt-Q',
            'duration': '%s'%(random.randint(100,200)),
            'started_at': responsex["result"]["result"]["updated_at"]#responsex["result"]["result"]["created_at"] 
        }
        response = requests.post('https://app.fanzy.io/video_reward/request', headers=headers, data=data).json()
        if response["code"] == 200:
          print("Success getting reward!!!")
        else:
          print(response)
for i in range(10):
    Thread(target=run,).start()
# run()
