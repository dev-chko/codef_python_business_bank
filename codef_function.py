import requests, json, base64
import urllib

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5



def http_sender(url, token, body):
    headers = {'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }
    response = requests.post(url, headers = headers, data = urllib.parse.quote(str(json.dumps(body))))
    return response


def request_token(url, client_id, client_secret):
    authHeader = stringToBase64(client_id + ':' + client_secret).decode("utf-8")
    headers = {
        'Acceppt': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + authHeader
        }
    response = requests.post(url, headers = headers, data = 'grant_type=client_credentials&scope=read')
    return response

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')



def publicEncRSA(pubKey, data):
    keyDER = base64.b64decode(pubKey)
    keyPub = RSA.importKey(keyDER)
    cipher = Cipher_PKCS1_v1_5.new(keyPub)
    cipher_text = cipher.encrypt(data.encode())
    encryptedData = base64.b64encode(cipher_text).decode("utf-8")
    print('encryptedData = ' + encryptedData)
    return encryptedData