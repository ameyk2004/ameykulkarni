class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.graph:
            self.graph[from_node] = {}
        if to_node not in self.graph:
            self.graph[to_node] = {}
        self.graph[from_node][to_node] = weight

    def get_neighbors(self, node):
        if node in self.graph:
            return self.graph[node]
        return {}

def add_transaction(graph, payer, payee, amount):
    graph.add_edge(payer, payee, amount)

def cash_flow_minimizer(transactions):
    balances = {}
    for transaction in transactions:
        payer, payee, amount = transaction
        balances[payer] = balances.get(payer, 0) - amount  #it gets the current balance of payer if not present, returns 0
        balances[payee] = balances.get(payee, 0) + amount

    balances_array = [(person, balance) for person, balance in balances.items()]   #So, after this line executes, balances_array contains a list of tuples where each tuple consists of a person and their corresponding balance.
    balances_array.sort(key=lambda x: x[1]) #sorting according to second value

    transactions_list = []

    while len(balances_array) > 1:
        debtor, debtor_balance = balances_array[0]
        creditor, creditor_balance = balances_array[-1]

        min_transaction = round(min(-debtor_balance, creditor_balance), 2)

        transactions_list.append(f"{debtor} pays {min_transaction} to {creditor}")

        debtor_balance += min_transaction
        creditor_balance -= min_transaction

        if debtor_balance == 0:
            balances_array.pop(0)
        else:
            balances_array[0] = (debtor, debtor_balance)

        if creditor_balance == 0:
            balances_array.pop()
        else:
            balances_array[-1] = (creditor, creditor_balance)

    return transactions_list


# transactions = [
#     ['A', 'B', 5],
#     ['B', 'C', 10],
#     ['C', 'A', 15],
#
# ]

# Get minimized cash flow
# minimized_cash_flow = cash_flow_minimizer(transactions)
# for transaction in minimized_cash_flow:
#     print(transaction)
