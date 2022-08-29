# curly-memory
A suite of personal financial tools.

`statement_writer.py` will create my financial statement listing my assets, liabilities and net worth 
in an Excel workbook.  It will read data from my bank statement, stock portfolio and insurance policies statement.
These documents are in HTML and PDF format.

`reports_creator.py` will create various reports from my financial data.  Reports include:
1. a line chart to track the values of my total assets, liabilities and net worth over time
2. a stacked bar chart to display cash vs loan amount
3. a pie chart to display stock allocation in my portfolio with respect to share count
4. a pie chart to display stock allocation in my portfolio with respect to total cost
5. a bar chart to display the profitability of each stock in my portfolio
6. a line chart to display my portfolio's performance over time

Execute the unit tests with:

`pytest --cov . tests/ --cov-report html:tests/results/cov_html -v > tests/results/results.txt`

Test results will be in `tests/results/results.txt`.
Coverage report will be in `tests/results/cov_html/index.html`.