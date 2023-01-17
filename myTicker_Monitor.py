
import pandas_datareader as web
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print
from yahoo_fin.stock_info import get_dividends
from utils.logo import logo

logo("TICKER-MONITOR")
print(Panel.fit("Desenvolvido por: Vinícius Azevedo"))

while True:
    # Ticker de FII e Ações
    tickers = ["MXRF11.SA", "MCCI11.SA", "HGRU11.SA", "DEVA11.SA", "PETR4.SA", "TAEE11.SA", "BBAS3.SA"]
    current_price = web.get_quote_yahoo(tickers)

    ##############################################
    # FUNDOS IMOB
    ##############################################
    table_fii = Table(title="Fundos Imobiliários + Ações")
    table_fii.add_column(" ", justify="right", style="blue")
    table_fii.add_column("MXRF11", justify="center", style="cyan")
    table_fii.add_column("MCCI11", justify="center", style="magenta")
    table_fii.add_column("HGRU11", justify="center", style="green")
    table_fii.add_column("DEVA11", justify="center", style="yellow")
    
    ##############################################
    # AÇÕES
    ##############################################
    table_fii.add_column("PETR4", justify="center", style="white")
    table_fii.add_column("TAEE11", justify="center", style="white")
    table_fii.add_column("BBAS3", justify="center", style="white")


    # Funções para monitoramento dos valores
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

    # Chamando as funções
    preços = current_price(tickers)
    mud_reg_merc = regular_market_change(tickers)
    high = regular_market_high(tickers)
    low = regular_market_low(tickers)

    # Input de dados na linha da tabela
    table_fii.add_row("Preço Atual (R$)", str(preços[0]), str(preços[1]), str(preços[2]), str(preços[3]), str(preços[4]), str(preços[5]), str(preços[6]))
    table_fii.add_row("Variação +-", str(round(mud_reg_merc[0],2)), str(round(mud_reg_merc[1],2)), str(round(mud_reg_merc[2],2)), str(round(mud_reg_merc[3],2)), str(round(mud_reg_merc[4],2)), str(round(mud_reg_merc[5],2)), str(round(mud_reg_merc[6],2)))
    table_fii.add_row("Maior Preço ⬆", str(high[0]), str(high[1]), str(high[2]), str(high[3]), str(high[4]), str(high[5]), str(high[6]))
    table_fii.add_row("Menor Preço ⬇", str(low[0]), str(low[1]), str(low[2]), str(low[3]), str(low[4]), str(low[5]), str(low[6]))
    

    ##############################################
    # DIVIDENDOS
    ##############################################
    table_div = Table(title="Dividendos")
    table_div.add_column(" ", justify="right", style="blue")
    table_div.add_column("MXRF11", justify="center", style="cyan")
    table_div.add_column("MCCI11", justify="center", style="magenta")
    table_div.add_column("HGRU11", justify="center", style="green")
    table_div.add_column("DEVA11", justify="center", style="yellow")
    table_div.add_column("PETR4", justify="center", style="white")
    table_div.add_column("TAEE11", justify="center", style="white")
    table_div.add_column("BBAS3", justify="center", style="white")

    # Iteração dos valores dos dividendos referente ao último mes
    dividends =[]
    for i in tickers:
        div_data = get_dividends(i, "2022/12/28")
        data = div_data.values
        dividends.append(data)

    # Input de dados na linha da tabela
    table_div.add_row(
        "Último Div. (R$)", 
        str(dividends[0][0][0]),
        str(dividends[1][0][0]), 
        str(dividends[2][0][0]), 
        str(dividends[3]),
        str(dividends[4]),
        str(dividends[5][0][0]),
        str(dividends[6])
        )

    console = Console()
    console.print(table_fii)
    console.print(table_div)
    print("=" * 80)
    time.sleep(10)
