from pykis import PyKis
from . import ManageToken


class PrivateKis:
    def __init__(self):
        self.kis = None

    def connectKis(self):
        self.kis = PyKis(
            id=ManageToken.key_info.id,
            account=ManageToken.key_info.account,
            appkey=ManageToken.key_info.appkey,
            secretkey=ManageToken.key_info.appsecret
        )
    def getKis(self):
        return self.kis