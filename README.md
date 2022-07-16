# curly-memory
A suite of personal financial tools.

`statement_writer.py` will create my financial statement listing my assets, liabilities and net worth 
in an Excel workbook.  It will read data from my bank statement, stock portfolio and insurance policies statement.
These documents are in HTML and PDF format.

`reports_creator.py` will create various reports from my financial data.  Reports include a chart to track the values 
of my total assets, liabilities and net worth over time, and a pie chart to display stock allocation in my portfolio, 
with respect to share count and total cost.

Execute the unit tests with:

`pytest --cov . tests/ --cov-report html:tests/results/cov_html -v > tests/results/results.txt`

Test results will be in `tests/results/results.txt`.
Coverage report will be in `tests/results/cov_html/index.html`.