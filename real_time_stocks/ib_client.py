import logging
import time
from datetime import datetime
from threading import Thread

from ibapi.client import Contract
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

from real_time_stocks.chart_manager import ChartManager
from real_time_stocks.config import settings

logger = logging.getLogger(__name__)


class IBClient(EClient, EWrapper):
    def __init__(self, host, port, client_id, symbol):
        EClient.__init__(self, self)
        self.connect(host, port, client_id)
        self.chart_manager = ChartManager(symbol=symbol)
        thread = Thread(target=self.run)
        thread.start()

    def error(self, reqId, errorCode, errorString):
        if errorCode in [2104, 2106, 2158]:
            logger.info(f"Non-Error: {errorCode} - {errorString}")
        else:
            logger.error(f"Error: {errorCode} - {errorString}")

    def historicalData(self, req_id, bar):
        t = datetime.fromtimestamp(int(bar.date))

        data = {
            "date": t,
            "open": bar.open,
            "high": bar.high,
            "low": bar.low,
            "close": bar.close,
            "volume": int(bar.volume),
        }

        self.chart_manager.insert_candle(data)

    def historicalDataEnd(self, reqId, start, end):
        logger.info(f"end of data {start} {end}")
        self.chart_manager.update_chart(data=None)

    def get_bar_data(self, symbol: str, timeframe: str):
        logger.info(f"getting bar data for {symbol} {timeframe}")

        contract = Contract()
        contract.symbol = symbol
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        what_to_show = "TRADES"

        self.reqHistoricalData(2, contract, "", "7 D", timeframe, what_to_show, True, 2, False, [])
        time.sleep(1)


def show_chart(symbol: str):
    client = IBClient(settings.ib_host, settings.ib_port, settings.ib_client_id, symbol)

    contract = Contract()
    contract.symbol = symbol
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    what_to_show = "TRADES"

    client.reqHistoricalData(2, contract, "", "30 D", "5 mins", what_to_show, True, 2, False, [])

    time.sleep(1)

    client.get_bar_data(symbol, "8 hours")
