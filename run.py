import os
#실행 dir 설정
os.chdir('/home/ubuntu/codef_python_transaction/')
from codef_function import *
from datetime import datetime
from db_utils import *
from pytz import timezone

with open('connectinfo.py','r')as f:
    client_id = f.readline().splitlines()[0]
    client_secret = f.readline().splitlines()[0]
    pubkey = f.readline().splitlines()[0]
    connected_id = f.readline().splitlines()[0]
    derFile = f.readline().splitlines()[0]
    keyFile = f.readline().splitlines()[0]

token_f = open('token.txt' ,'r')
try:
    token = token_f.read().splitlines()[0]
except:
    token = ''
finally:
    token_f.close()

if __name__ == "__main__":
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    codef_fmt = '%Y%m%d'
    UTC = datetime.now(timezone('UTC'))
    KST = datetime.now(timezone('Asia/Seoul'))

today = KST.strftime(codef_fmt)
token_url = 'https://oauth.codef.io/oauth/token'

tx_url = 'https://development.codef.io/v1/kr/bank/b/account/transaction-list'

tx_body = {
    "connectedId": connected_id,
    "organization": "0003",
    "account": '47707448704011',
    "startDate": today,
    "endDate": today,
    "orderBy": "1",
    "inquiryType": "1"
}



tx_response = http_sender(tx_url, token, tx_body)
if tx_response.status_code == 200:
    r_dict = json.loads(urllib.parse.unquote_plus(tx_response.text))
    if 'data' in r_dict and str(r_dict['data']) != '{}':
        pass
    else:
        print('조회오류1')
elif tx_response.status_code == 401:
    response_oauth = request_token(token_url, client_id, client_secret)
    if response_oauth.status_code == 200:
        r_dict = json.loads(response_oauth.text)
        token = r_dict['access_token']
        with open('token.txt','w+')as f_t:
            f_t.write(token)
        tx_response = http_sender(tx_url, token, tx_body)
    else:
        print('client Id 변경')
else:
    print('조회오류2')


origin_tx = json.loads(urllib.parse.unquote_plus(tx_response.text))['data']['resTrHistoryList']
for i in range(0,len(origin_tx)):
    hist_json= origin_tx[i]
    for key, val in hist_json.items():
        globals()[key] = "{value}".format(value=val)
    serialNumber = resAccountTrDate + str(i+1).zfill(5)
    resTime = resAccountTrDate + resAccountTrTime[:4]
    try:
        insert_db(serialNumber, resAccountIn, resAccountDesc1, resAccountDesc2, resAccountDesc3, resTime, resAfterTranBalance)
    except pymysql.err.IntegrityError:
        pass
    except:
        print("이건 모르겠당")
