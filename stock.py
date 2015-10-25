import requests
import urllib

# Builds the Yahoo API request URL, given a list of stock symbols, i.e. ["YHOO", "FB"]
# symbol list needs to be at least size 1
def stock_url(symbols):
	SEARCH_URL = 'https://query.yahooapis.com/v1/public/yql?'
	params = {
		'q': 'select * from yahoo.finance.quotes where symbol in {}'.format(format_symbols(symbols)),
		'format': 'json',
		'diagnostics': 'true',
		'env': 'store://datatables.org/alltableswithkeys'
	}
	stock_request = SEARCH_URL+urllib.urlencode(params)
	return stock_request
	
# Helper function to stock_req_url()
# Convert a symbol list, i.e. ["YHOO", "FB"] to ("YHOO", "FB")
# symbol list needs to be at least size 1
def format_symbols(symbols):
	strng = '{}'.format(symbols)
	strng = strng.replace('[', '(')
	strng = strng.replace(']', ')')
	return strng

# Given a list of stock symbols, returns the API response in JSON
def stock_results(symbols):
	result = requests.get(stock_url(symbols))
	return result.json()

print stock_url(['FB'])
print '\n'
print stock_url(['FB', 'YHOO', 'GOOG'])





