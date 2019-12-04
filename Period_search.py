import os
#실행 dir 설정
os.chdir('/home/ubuntu/codef_python_transaction/')
from codef_function import *
from db_utils import *


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

token_url = 'https://oauth.codef.io/oauth/token'

tx_url = 'https://api.codef.io/v1/kr/bank/b/account/transaction-list'
start_date= str(input("시작일자를 입력하시오.(ex: 20190210): "))
end_date= str(input("검색종료일자를 입력하시오.(ex: 20190217): "))


tx_body = {
    "connectedId": connected_id,
    "organization": "0003",
    "account": '47707448704011',
    "startDate": start_date,
    "endDate": end_date,
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


date_compare = ''
origin_tx = json.loads(urllib.parse.unquote_plus(tx_response.text))['data']['resTrHistoryList']
for i in range(0,len(origin_tx)):
    hist_json= origin_tx[i]
    for key, val in hist_json.items():
        globals()[key] = "{value}".format(value=val)
    if date_compare != resAccountTrDate:
        count_date =1
        date_compare = resAccountTrDate
    else:
        count_date +=1
    serialNumber = resAccountTrDate + str(count_date).zfill(5)
    resTime = resAccountTrDate + resAccountTrTime[:4]   
    print(serialNumber, resAccountIn, resAccountDesc1, resAccountDesc2, resAccountDesc3, resTime, resAfterTranBalance)
    try:
        insert_db(serialNumber, resAccountIn, resAccountDesc1, resAccountDesc2, resAccountDesc3, resTime, resAfterTranBalance)
    except pymysql.err.IntegrityError:
        pass
    except:
        print("이건 모르겠당")
