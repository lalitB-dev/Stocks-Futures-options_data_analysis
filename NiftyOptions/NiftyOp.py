import requests
import pandas as pd




def getData():
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    # data = requests.get(url)

    headers = {

        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': "en-US,en;q=0.9"
    }

    session=requests.Session()
    request= session.get(url,headers=headers)
    cookies=dict(request.cookies)
    response= session.get(url,headers=headers,cookies=cookies).json()
    return response


