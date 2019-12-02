# codef_python_transaction
codef_python_수시입출금 API 사용

<br>
## 환경구성<br> 
1.ubuntu 16.04LTS<br>
2.Python -v 3.5.2<br>
3.pip -v 19.3.1 <br><br><br>

## 의존성<br><br>
`pip install requests`<br>
`pip install pycrypto`<br>
`pip install pytz`<br>
<br>
<br>
<br>
## MySQL 테이블 생성
테이블 이름 : codef_Transaction<br>
이름	타입/크기	column	설명	Option<br>
고유넘버	varchar(20)	serialNumber	날짜 + 0000(넘버링)	PK, NOT NULL, UQ<br>
금액	BIGINT	resAccountIn	resAccountIn	NOT NULL<br>
입금자	varchar(45)	resName	resAccountDesc1	NOT NULL<br>
이체종류	varchar(45)	resTraType	resAccountDesc2	NOT NULL<br>
표기	varchar(45)	resType	resAccountDesc3	NOT NULL<br>
시간	BIGINT	resTime	YYYYMMDDHHmm(resAccountTrDate + resAccountTrtime[:4])	NOT NULL<br>
잔액	BIGINT	resBalance	resAccountTranBalance	NOT NULL<br>
확인  INT   enable_system NOT NULL default '0'<br>
<br>
## derFile, keyFile 생성방법<br>
```
import base64
der_f = open('signCert.der', 'rb')
der_b = der_f.read()
derFile = str(base64.b64encode(der_b))[2:-1]
der_f.close()
key_f = open('signPri.key', 'rb')
key_b = key_f.read()
keyFile =  str(base64.b64encode(key_b))[2:-1]
key_f.close()
```
## crontab 설정
`crontab -e`<br>
`*/5 * * * * /usr/bin/python3.5 /home/ubuntu/codef_python_transaction/run.py`<br>
`#5분에 한번씩 실행`

## 진행 순서
<br>
1. connectinfo_sample.py참고하여 connectinfo.py 생성<br>
2. python3 run.py 실행<br>
<br>
<br>
