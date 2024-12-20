from . import ConnectKIS
from pykis import PyKis, KisAuth, KisBalance, KisQuote
from . import models

class Stock:
    def __init__(self, parameter = None):
        self.Cpk_tmp = None
        self.api_kis = None
        self.StockNameData = None
        self.SearchedData = []

    def connectStockToken(self, kistoken):
        self.Cpk_tmp = kistoken
        self.api_kis = self.Cpk_tmp.getKis()

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

    def connectSql(self):
        for stock_data in self.SearchedData:
            try:
                nasdaq_stock, _ = models.Nasdaq.objects.get_or_create(
                    code = stock_data["NAME"] # 추후 코드로 변경 예정
                )
                models.Nasdaq_Stock.objects.update_or_create(
                    stock = nasdaq_stock,
                    defaults={
                        'per': stock_data["PER"],
                        'pbr': stock_data["PBR"],
                        'eps': stock_data["EPS"],
                        'bps': stock_data["BPS"]
                    }
                )
            except Exception as e:
                print(f"데이터 저장/업데이트 중 오류 발생: {e}")
                continue

    def filter_stock_data(self, threshold, compare_func):
        result = []
        for item in self.SearchedData: #Searched data를 불러와서
            if compare_func(item) >= threshold:# threshold 값 보다 높으면 item을 result에 포함
                result.append(item)
        return result

    def compare_per(item): # Searched data 값을 받아서 원하는 것에 따라 per, pbr, 등 불러옴
        return item.per

    def compare_pbr(item):
        return item.pbr

    def compare_eps(item):
        return item.eps

    def compare_bps(item):
        return item.bps

# commit 변경을 알아보기 위한 주석