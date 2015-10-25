import requests
import stock
from flask import Flask, request, redirect, render_template, session
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__) 

@app.route('/')
def index():
    queryStarted= False
    return render_template('index.html',queryStarted=queryStarted )

    
@app.route('/compare', methods=['POST'])
def compare():
	symbols = stock.unicode_to_str(request.form.getlist('symbol'))
	results = stock.stock_results(symbols) 
	queryStarted=True
	return render_template('index.html', quotes=results,queryStarted=queryStarted)


if __name__ == "__main__":
    app.run(debug=True)
