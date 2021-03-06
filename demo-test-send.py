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
        self.DATA_OFSET = 2000000000
        self.JSON_CONFIG = {
            "type": "service_account",
            "project_id": "sj2-dashboard-web",
            "private_key_id": "aeb12090b7dc1a33195741b6cfb7a941cc8caa98",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC02jcPJUGO1tMp\nW5C2frgkXQIFIy1cywDQarETnLcjDrAfg/jV9iMRDWm3oSY+TDpk7YN5859Ywd3U\n4lqp63/KQLwHHHUUEysmU78SMwiy7j/dNFKJOHiFxyek1ipTnoM53OimwCoNp/DD\nYN4GNfZTnUThmYITLhlnfftVc6lA1edtKrvpnBJG1grbo9KFS+9nbehrgU7Y/pYZ\nIfsIhiMyVP8pvtJQMMINLxSxxvs5bpC8dz7aA4J5n1UGB+bU4bCKXHtC9Io7pAfk\nEr1e2rjXt86ZcFx59BxJQdkloeoHYzgaQALP5Mnscyav8w4/7Vq02wpkl16PJONi\nUBEDjbuDAgMBAAECggEAG3+2sYHbtwlpMDexCF66RyUxQnC33A0uAYLHjBDfM+Bu\n3Uvm0TnM2THt6jMBqqVSl7gZrrhheVB5F36XhJC/bJRtQrOMBdJoVDqVqgHCh9p8\nMXlcN2szwDupBoJeCzrl/y1c3sYHXu4zSLH48H7SBqK6L4d05M+0oyzfw32DtczP\nIxLu7Krr2jhNjiZ0epX97QEsoTbE0C6D6/uQu8ngacxU1fXaqHAuRNrxN56SP1ya\nnYgdSwqzpxGLVcHIqnh3V2GJfhbubmrys85t0O4NCSsnEyns2G1yqiVHGUcWfoWV\nfDghUnKvzJDeYV16Cwh7PbWz8mbfN10zw2guQERpAQKBgQDattSkoTLrF8X0Xtqt\nwtxa/Lah8lciokCgd3ry98jSpWlb3zS2K314rYjad+vhng7FBoPWzBZioCqDUaFp\nboCmdvkRSE+/dg6CTg09bo/7MY1rKR+QbaZgt4+MVY5wfyNi/1HphUV4SNU9Rced\ncbo8JpeF1mZaxL79YmAgB+hYAwKBgQDTrwNK2k7IJzkyjgyQPry9NmifRfrtomz7\nc0UIIiQ/u1/XvhMzfOx0Rl1yMJzofVIhGbzEvVZOiK6jBLQ3dyaz0BwM9yopJch2\nOtGkOrGAWOlCHFxonnjCzGZAan5MnE+oQXL6k8LkoV1auhg9YwiYcw8/ZT8Ttlli\nWVbw5Ph2gQKBgF9V6LTmS0Ksty4BFsM9OD41AArxjsfa/96ylhZIqfIgBh/02I47\nwNKUmh3Yvio3cmqxn1BG388Xz9A0Ce7iKxPkska1RYXImSR1j1Hi2sH85I78evTC\nxw5LlTfvp0okMTGa54KqBBEddk3iF9PqWeqUS+IcBbu1HSdn9UyhBccvAoGBAJCb\nRCKEU8FDmj1A8LAxS3nuizYS9kIT7WMw8X2G5UBsXiLhg/huZJFh6EAzmVzxD4Px\nMxUrSqRHlxViB0LEsLmxdxgcWL7XQsQRllkch1loY6B4A2CssU5Rl6B1n2XyejA0\n1bj76+2HlmB+NETrPFn4b/gc0CRFM3aOFWhm4p0BAoGANLWdjAGJDZGcoXHfgEpL\nboWOf5qbjexamhWByKRxvXrL22y5s0JaoKFLTkHnFI9IWN4rghcikLaYVH5IzlEc\nMeSBvFWpgHjIoYM2tJu/cVtz/rFYdBR/q4baY9S+hVDcmC8Y2uF+782zGHUgWr8a\nBGa/KmihfOBboKSyE9BgjgU=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-adzvd@sj2-dashboard-web.iam.gserviceaccount.com",
            "client_id": "104648854302579403876",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-adzvd%40sj2-dashboard-web.iam.gserviceaccount.com"
        }

    def sendMessage(self, data_name, data_text):
        cred = credentials.Certificate(self.JSON_CONFIG)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d - %b - %Y ( %H : %M : %S )")
        # secondsSinceEpoch = 1
        secondsSinceEpoch = time.time()
        secondsSinceEpoch = self.DATA_OFSET - secondsSinceEpoch
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
    msg_name = sys.argv[1]
    msg_text = "5"
    #  send data to fireabse
    protocol.sendMessage(msg_name, msg_text)
