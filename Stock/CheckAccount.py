import SearchStock
from pykis import KisBalance

def check():
    CheckedAccount = None
    CheckedAccount = SearchStock.Stock.api_kis
    result = CheckedAccount.account()
    balance: KisBalance = result.balance()
    return balance

