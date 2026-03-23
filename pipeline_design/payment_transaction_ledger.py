"""
Author: Manav Gurnani

Problem: Payment Transaction Ledger
"""

from collections import defaultdict

# ---------------------- Part II: Rejected Transactions ----------------------

"""
EXAMPLE
Input:
transactions = [
    "acct_001,1,500",
    "acct_002,2,300",
    "acct_001,3,-200",
    "acct_002,4,-300"
]

Output:
["acct_001,300"]
"""

# 1. Process transactions into hashmap {acct_id -> {recent timestamp -> amount}}
# 2. Sort transactions (by account ID)
# 3. Traverse transactions and print account information if balance > 0 (print utility function)

def processTransactions(transactions: list[str]) -> dict:
	transaction_map = defaultdict(dict)
	rejected = []
	for entry in transactions:
		transaction_data = entry.split(",")
		if len(transaction_data) < 4:
			continue # skip entries that don't have all the required information
		acct_info = transaction_data[0].split("_")
		acct_id = acct_info[-1]
		currency = transaction_data[2]
		print(f"t: {transaction_data[1]} Account: {acct_id} Currency: {transaction_data[2]} Amount: {int(transaction_data[3])}")
		if acct_id in transaction_map.keys() and currency in transaction_map[acct_id].keys():
			currBalance = transaction_map[acct_id][currency]["balance"] + int(transaction_data[3])
			print(transaction_map[acct_id])
			print(transaction_data[2])
			if currBalance <= 0:
				rejected.append(entry)
				continue
		else:
			currBalance = int(transaction_data[3])
		transaction_map[acct_id][currency] = { # creating hashmap entry for data storing
			"timestamp": int(transaction_data[1]),
			"balance": currBalance
		}

		transaction_map[acct_id] = dict(sorted(transaction_map[acct_id].items()))
	return dict(sorted(transaction_map.items())), rejected

def printLedger(accounts):
	output = []
	for account_id in accounts.keys():
		for currency in accounts[account_id].keys():
			if accounts[account_id][currency]["balance"] and accounts[account_id][currency]["balance"] != 0:
				output.append(printAcctInfo(account_id, currency, accounts[account_id][currency]["balance"]))
	return output

def printAcctInfo(acct_id: str, currency: str, balance: int):
	return str(f"acct_{acct_id},{currency},{balance}")

transactions = [
    "acct_001,1,usd,1000",
    "acct_001,2,eur,500",
    "acct_001,3,usd,-400",
    "acct_001,4,eur,-600",
    "acct_002,5,usd,200"
]

accounts, rejected = processTransactions(transactions)
ledger = printLedger(accounts)
print(ledger)
print(rejected)
