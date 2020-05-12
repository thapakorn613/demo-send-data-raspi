# import classes.aarApi as aar
import sys
import time
import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore


class aarApi:
    def __init__(self):
        self.version = 1
        self.DATA_NAME_COLLECTION = "messages"
        self.DATA_PATH_JSON_FILE = "./Admin_SDK.json"
        self.DATA_TEXT = ""
        self.JSON_CONFIG = {
            "type": "service_account",
            "project_id": "site-web-aar",
            "private_key_id": "d1cfee1f52f314f5240615f6b6f512126c3c0090",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDr4hNUo7YFBCag\nOOhkp8C+t6hKXWpF1mr2kLNwLsdXj26neYX47LHJEYBJJh4dPolvLKuGKkUvL9SO\nMlQhqZvXMelovwmsKTYRhlta/MMpPxa5EXuzEzQ+v3oABac/u18IzA/vcgZxzIYo\n+BTp1QsuWTczjJn4M/nwslE+gwVITjhn9L8+IZRZz6aqiZDJnuO1WE3CMZqgwlg4\nly8bJIJ5A3CGmAJamaMOFjiM78YrBXfAnOuIHhnh8hwAeVr8aELeahF5AScs4M/H\nYp5ySJw0QNM1FDM+wiECVfRvhkm70o1dMP6sULkHwri/j6wPAYHltCM06LBk8FMG\nftAqh6iFAgMBAAECggEAAyEpO36+i/t9nbOTlb5KBt297Fqn7cxF+AZ8cvkT6Pv8\nrlkk52QQicfjKVVJof6x6RkxH2MRLuqWCdruFdI/wI+ndp3OPYwAbSQYszDWUAZH\nwWXTe9E96LU2o6hvix9rx9yZO4aKQllB0GpWMLIEZ3WEj3kGk+3wm3pqLIelesuU\nW2cxNZV4LVw+OuiAAw6ldY0zu9sSKkO7xGmYTzyRLS+XeWcTtNYW81IAgivEsjb8\nbQ9LvlCDJXNIBvN9CzeOhwPEZCgKAbzZDe94Rpalutv2gvwFpmScPeR9xc6nLbNJ\nT18+1xu1NEnF8Z38XSKPaZZMHV4wkjPwfkxF2B998QKBgQD6oJLAs/oOvRyV4PFO\nWoEBTD3f75dQOJCdMHNb2uRY0pQi2wakhNiHLoUlwKnyOLMLgoSn2M2iilqGa8Dl\nYeQ6IVM5hf6V19yG+/sUHhETsfdusQwRXKtldd2d88I6mjQw+BO/yiyFcsz46Vhk\nMt7nRU5sFS4bLX0PJNbF3p56LQKBgQDw8JZeSvK+VqaGqLLtn6ZYHwIzzfMNgpMs\nyHApkPVnst5mjO7QPlWPdeIXBCGnMwqK2VZMVniE5YZeA5DccY+9MsV2qk7sFG8S\n1PdNqS4qSrs5i61DeOdKfWLL3raqxsy6teqwksfO5ATYAv0jUOVZqcHPXXfEWxJ9\nXwB44feWuQKBgQDTjidSMpmpR0iR20bVdN/gUJMKLBv1w0mO5g76QlLuBxK0OV3q\nEZkUwtfxfif2JpY76PhBFmi+AztWrC4vcepMh0TREaJMqeGkr57I5HhVv6u07A3b\nufWTt2JSqigRf4j+rOk+w1HBc55BnfbW3Xn6ji4cXeSFXGhsGBSTAc+UIQKBgQCl\nCmg2FujIcNqJCy3lj6KGYldD3SNMcdEWsAYEswMnEWM+o/NCOjCpoHpKgc37lf72\ntYFjsSfFAORVqeOk3TU0yH5ylp6RID4ljDQKwoSY+6/b7020FjF42QK/28MMoDjE\n/K/SW/j6Qz7+KK31bwhrrtjPjprnqeq0bksIguDyIQKBgHDLRbgaSgPWAzAzpw4g\nZPS5QMkVpEdsgpNNBfQ4JPo/Jv3cQ/cieBrMSDTFQZy372IqZaWDn4XoJ1N6LLQS\nY9eGHsJIwC5mL15mlQpHeJdAZLWKpbVZYkfkw5Mmk+IrMjBw2Xdmzt67HPED7Osh\ntc2jGnUOnk2089D2Gn6G2B+y\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-hrznb@site-web-aar.iam.gserviceaccount.com",
            "client_id": "116940754708158294111",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-hrznb%40site-web-aar.iam.gserviceaccount.com"
        }

    def sendMessage(self, data_name, data_text):
        cred = credentials.Certificate(self.JSON_CONFIG)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d - %b - %Y ( %H : %M : %S )")
        secondsSinceEpoch = time.time()
        doc_ref = db.collection(
            u'' + self.DATA_NAME_COLLECTION).document(str(secondsSinceEpoch))
        data = {
            u'name': u''+data_name,
            u'timestamp': u''+str(timestampStr),
            u'text': u''+data_text,
            u'createAt': secondsSinceEpoch
        }
        doc_ref.set(data)


if __name__ == "__main__":
    #  init api library
    protocol = aarApi()
    # set var to send
    # msg_name = "art"
    msg_name = sys.argv[1]
    msg_text = "5"
    #  send data to fireabse
    protocol.sendMessage(msg_name, msg_text)
