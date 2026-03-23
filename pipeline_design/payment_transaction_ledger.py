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
	transaction_map = {}
	rejected = []
	for entry in transactions:
		transaction_data = entry.split(",")
		if len(transaction_data) < 3:
			continue # skip entries that don't have all the required information
		acct_info = transaction_data[0].split("_")
		acct_id = acct_info[-1]
		print(f"t: {transaction_data[1]} Account: {acct_id} Amount: {int(transaction_data[2])}")
		if acct_id in transaction_map.keys():
			print("Key found")
			currBalance = transaction_map[acct_id]["balance"] + int(transaction_data[2])
			if currBalance <= 0:
				rejected.append(entry)
				continue
		else:
			print("Key not found")
			currBalance = int(transaction_data[2])
		transaction_map[acct_id] = { # creating hashmap entry for data storing
			"timestamp": int(transaction_data[1]),
			"balance": currBalance
		}
	return dict(sorted(transaction_map.items())), rejected

def printLedger(accounts: dict):
	output = []
	for account in accounts.keys():
		if accounts[account]["balance"] and accounts[account]["balance"] != 0:
			output.append(printAcctInfo(account, accounts[account]))
	return output

def printAcctInfo(acct_id: str, acct_info: any):
	return str(f"acct_{acct_id},{acct_info["balance"]}") if "balance" in acct_info.keys() else ""

transactions = [
    "acct_001,1,500",
    "acct_001,2,-700",
    "acct_002,3,100",
    "acct_002,4,-50",
    "acct_002,5,-80"
]

accounts, rejected = processTransactions(transactions)
ledger = printLedger(accounts)
print(ledger)
print(rejected)
