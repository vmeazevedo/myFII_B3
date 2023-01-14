
import pandas_datareader as web
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print
from yahoo_fin.stock_info import get_dividends
from utils.logo import logo

logo("MyFII-MONITOR")
print(Panel.fit("Desenvolvido por: Vinícius Azevedo"))

while True:
    ##############################################
    # FUNDOS IMOB
    ##############################################
    tickers = ["MXRF11.SA", "MCCI11.SA", "HGRU11.SA", "DEVA11.SA"]
    current_price = web.get_quote_yahoo(tickers)

    table_fii = Table(title="Fundos Imobiliários")
    table_fii.add_column(" ", justify="right", style="blue")
    table_fii.add_column("MXRF11", justify="center", style="cyan")
    table_fii.add_column("MCCI11", justify="center", style="magenta")
    table_fii.add_column("HGRU11", justify="center", style="green")
    table_fii.add_column("DEVA11", justify="center", style="yellow")


    def current_price(tickers):
        current_price = web.get_quote_yahoo(tickers)["price"]
        return current_price


    def regular_market_change(tickers):
        market_change = web.get_quote_yahoo(tickers)["regularMarketChange"]
        return market_change


    def regular_market_high(tickers):
        market_high = web.get_quote_yahoo(tickers)["regularMarketDayHigh"]
        return market_high


    def regular_market_low(tickers):
        market_low = web.get_quote_yahoo(tickers)["regularMarketDayLow"]
        return market_low

    preços = current_price(tickers)
    mud_reg_merc = regular_market_change(tickers)
    high = regular_market_high(tickers)
    low = regular_market_low(tickers)

    table_fii.add_row("Preço Atual (R$)", str(preços[0]), str(preços[1]), str(preços[2]), str(preços[3]))
    table_fii.add_row("Variação +-", str(round(mud_reg_merc[0],2)), str(round(mud_reg_merc[1],2)), str(round(mud_reg_merc[2],2)), str(round(mud_reg_merc[3],2)))
    table_fii.add_row("Maior Preço ⬆", str(high[0]), str(high[1]), str(high[2]), str(high[3]))
    table_fii.add_row("Menor Preço ⬇", str(low[0]), str(low[1]), str(low[2]), str(low[3]))

    ##############################################
    # DIVIDENDOS
    ##############################################
    table_div = Table(title="Dividendos")
    table_div.add_column(" ", justify="right", style="blue")
    table_div.add_column("MXRF11", justify="center", style="cyan")
    table_div.add_column("MCCI11", justify="center", style="magenta")
    table_div.add_column("HGRU11", justify="center", style="green")
    table_div.add_column("DEVA11", justify="center", style="yellow")

    dividends =[]
    for i in tickers:
        div_data = get_dividends(i, "2022/12/28")
        data = div_data.values
        dividends.append(data)

    table_div.add_row("Último Div. (R$)", str(dividends[0][0][0]), str(dividends[1][0][0]), str(dividends[2][0][0]), str(dividends[3]))

    console = Console()
    console.print(table_fii)
    console.print(table_div)
    print("\n==========================================================")
    time.sleep(10)
