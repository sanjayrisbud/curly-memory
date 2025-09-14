# curly-memory
A personal financial statement generator.

`statement_writer.py` will create my financial statement listing my assets, liabilities 
and net worth in an Excel workbook.  

<p align="left">
    <img src="assets/01 - summary.jpg" height="75" width="128"/>
    <img src="assets/02 - assets.jpg" height="75" width="128"/>
    <img src="assets/03 - liabilities.jpg" height="75" width="128"/> 
</p>nshots

It will read data from my bank statement, stock portfolio, loan statement of account, mutual 
funds' statement and insurance policies' statement. These documents are in 
HTML, CSV, JSON and PDF formats.

`db_interface.py` acts as an interface to a SQLite database where all data collected from the
different data sources is saved.

`reports_creator.py` will create various reports from my financial data.  Reports include:
1. a line chart to track the values of my total assets, liabilities and net worth over time

<img src="assets/04 - saln chart.jpg" height="75" width="128"/> 

2. a pie chart to display the breakdown of my assets and liabilities
3. a pie chart to display the allocation of my assets
4. a pie chart to display the ratio of cash vs other financial instruments

<img src="assets/05 - summaries.jpg" height="75" width="128"/> 

5. a stacked bar chart to display cash vs loan amount

<img src="assets/06 - cash vs loan amount.jpg" height="75" width="128"/> 

6. a pie chart to display stock allocation in my portfolio with respect to share count
7. a pie chart to display stock allocation in my portfolio with respect to total cost

<img src="assets/07 - portfolio allocation.jpg" height="75" width="128"/> 

8. a bar chart to display the profitability of each stock in my portfolio

<img src="assets/08 - profitability.jpg" height="75" width="128"/> 

9. a line chart to display my portfolio's performance over time

<img src="assets/09 - portfolio performance.jpg" height="75" width="128"/> 

10. a line chart to compare the performances of my portfolio and mutual funds over time

<img src="assets/10 - fund performance.jpg" height="75" width="128"/> 


After generating the financial statement, the data files, SQLite database and generated statement 
are archived to a predefined location. 

Sample Excel output is in `assets/sample_output.xlsx`

Execute the unit tests with:

`pytest --cov . tests/ --cov-report html:tests/results/cov_html -v > tests/results/results.txt`

Test results will be in `tests/results/results.txt`.
Coverage report will be in `tests/results/cov_html/index.html`.