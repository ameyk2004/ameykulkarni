from flask import request, render_template, Blueprint
from cash_flow_manager.transaction_minimizer import cash_flow_minimizer

cashflowminimizer = Blueprint("cashflowminimizer", __name__,static_folder="static", template_folder="templates")
@cashflowminimizer.route('/')
def home():
    return render_template('index2.html')

@cashflowminimizer.route('/min-flow', methods=['POST'])
def getminFlow():
    if request.method == 'POST':
        data = request.json
        print(data)
        transactions = []
        # ['A', 'B', 5]

        for transaction in data['transactions']:
            curr_trans = []
            curr_trans.append(transaction['payer'])
            curr_trans.append(transaction['payee'])
            curr_trans.append(transaction['amount'])
            transactions.append(curr_trans)

        print(transactions)
        result = cash_flow_minimizer(transactions)
        print({'result' : result})


    return {'result' : result}
