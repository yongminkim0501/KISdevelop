import ConnectKIS
from pykis import PyKis, KisAuth, KisBalance, KisQuote


class Stock:
    def __init__(self):
        Cpk_tmp = ConnectKIS.PrivateKis()
        Cpk_tmp.connectkis()
        self.api_kis = Cpk_tmp.getkis()
        self.StockNameData = None
        self.SearchedData = []

    def ConnectStockName(self, name):
        stock = self.api_kis.stock(name)

        quote: KisQuote = stock.quote()
        quote: KisQuote = stock.quote(extended=True)  # 주간거래 시세

        self.StockNameData = quote

    def StockDataToJson(self):
        dic_data = {
            "NAME": self.StockNameData.indicator.name,
            "PER": float(self.StockNameData.indicator.per),
            "PBR": float(self.StockNameData.indicator.pbr),
            "EPS": float(self.StockNameData.indicator.eps),
            "BPS": float(self.StockNameData.indicator.bps)
        }
        self.SearchedData.append(dic_data)

    def SearchStockPer(self, thresholdPer):
        result = []
        for item in self.SearchedData:
            if item.per >= thresholdPer:
                result.append(item)
        return result
'''
같은 형식의 per, pbr, eps, bps 만들 예정
따라서 super 클래스로 상속받아서 만들 예정이며 그에 따라 해당 연결은
factory로 구현 후, 그곳에서 책임 부여
'''