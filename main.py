import yfinance as yf
from rich import print
import pandas as pd

data = yf.Ticker("RS")
# print(dat)

income_statement = data.financials.transpose()
income_statement.index = pd.to_datetime(income_statement.index)
income_statement = income_statement.infer_objects()
income_statement['Year'] = income_statement.index.year


ebitda_2023 = float(income_statement.query('Year == 2023')['EBITDA'].dropna())
print(ebitda_2023)
