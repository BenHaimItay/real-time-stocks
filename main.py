import logging
import sys

import typer

from real_time_stocks.ib_client import show_chart

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
root.addHandler(handler)

app = typer.Typer()


@app.command()
def show_stock(symbol: str):
    show_chart(symbol)


if __name__ == "__main__":
    app()
