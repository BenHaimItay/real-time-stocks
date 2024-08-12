import logging
import queue

import pandas as pd
from lightweight_charts import Chart

logger = logging.getLogger(__name__)


class ChartManager:
    def __init__(self, symbol: str):
        self.queue = queue.Queue()
        self.chart = Chart(toolbox=True, width=1000, inner_width=0.6, inner_height=1)
        self.chart.legend(True)
        self.chart.topbar.textbox("symbol", symbol)
        self.chart.watermark(symbol)

    def insert_candle(self, data: dict):
        self.queue.put(data)

    def update_chart(self, data: pd.DataFrame = None):
        print("***ITAYBE Updating chart!")
        try:
            bars = []
            while True:
                data = self.queue.get_nowait()
                print(f"***ITAYBE Appending data: {data}")
                bars.append(data)
        except queue.Empty:
            logger.info("data queue is empty")
        finally:
            df = pd.DataFrame(bars)
            print(f"***ITAYBE Updating chart with df of shape {df.shape}")
            logger.info(f"updated chart: {df}")
            self.chart.set(df)
            self.chart.show(block=True)
