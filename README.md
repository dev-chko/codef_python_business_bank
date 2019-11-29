# codef_python_transaction
codef_python_수시입출금 API 사용

<br>
## 환경구성<br> 
1.ubuntu 16.04LTS<br>
2.Python -v 3.5.2<br>
3.pip -v 19.3.1 <br>

## 의존성<br><br>
`pip install requests`<br>
`pip install pycrypto`<br>
`pip install pytz`<br>
<br>
<br>
<br>
## MySQL 테이블 생성
테이블 이름 : codef_Transaction				
이름	타입/크기	column	설명	Option
고유넘버	varchar(20)	serialNumber	날짜 + 0000(넘버링)	PK, NOT NULL, UQ
금액	BIGINT	resAccountIn	resAccountIn	NOT NULL
입금자	varchar(45)	resName	resAccountDesc1	NOT NULL
이체종류	varchar(45)	resTraType	resAccountDesc2	NOT NULL
표기	varchar(45)	resType	resAccountDesc3	NOT NULL
시간	BIGINT	resTime	YYYYMMDDHHmm(resAccountTrDate + resAccountTrtime[:4])	NOT NULL
잔액	BIGINT	resBalance	resAccountTranBalance	NOT NULL

## 진행 순서
<br>
1. connectinfo_sample.py참고하여 connectinfo.py 생성
2. python3 run.py 실행
<br>
<br>
