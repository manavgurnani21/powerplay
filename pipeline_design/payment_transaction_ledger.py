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
    "acct_001,1,usd,1000",
    "acct_001,2,eur,500",
    "acct_001,3,usd,-400",
    "acct_001,4,eur,-600",
    "acct_002,5,usd,200"
]

Output:
balances: ["acct_001,eur,500", "acct_001,usd,600", "acct_002,usd,200"]
rejected: ["acct_001,4,eur,-600"]

"""

# 1. Process transactions into hashmap {acct_id -> {recent timestamp -> amount}}
# 2. Sort transactions (by account ID)
# 3. Traverse transactions and print account information if balance > 0 (print utility function)

accounts_directory = defaultdict(dict)
rejected_entries = []

def processEvents(events: list[str]) -> dict:
	for entry in events:
		transaction_data = entry.split(",")
		if transaction_data[0] == "TX" :
			if len(transaction_data) < 5:
				rejected_entries.append(entry)
				continue # skip entries that don't have all the required information
			acct_info = transaction_data[1].split("_")
			acct_id = acct_info[-1]
			currency = transaction_data[3]
			if acct_id in accounts_directory.keys() and currency in accounts_directory[acct_id].keys():
				currBalance = accounts_directory[acct_id][currency]["balance"] + int(transaction_data[4])
				if currBalance <= 0:
					rejected_entries.append(entry)
					continue
			else:
				currBalance = int(transaction_data[4])
			accounts_directory[acct_id][currency] = { # creating hashmap entry for data storing
				"timestamp": int(transaction_data[2]),
				"balance": currBalance
			}
			print(accounts_directory)
		elif transaction_data[0] == "TRANSFER":
			if len(transaction_data) < 6:
				rejected_entries.append(entry)
				continue # skip entries that don't have all the required information
			src_acct_id = transaction_data[2].split("_")[-1]
			dst_acct_id = transaction_data[3].split("_")[-1]
			currency = transaction_data[4]
			amt = int(transaction_data[5])
			status = processTransfer(src_acct_id,dst_acct_id,currency,amt)
			if status == 1:
				rejected_entries.append(entry)
		else:
			rejected_entries.append(entry)
		accounts_directory[acct_id] = dict(sorted(accounts_directory[acct_id].items()))

def processTransfer(src_acct_id: str, dst_acct_id: str, currency: str, amt: int) -> int:
	if amt >= 0 and (currency in accounts_directory[src_acct_id].keys()) and (currency in accounts_directory[dst_acct_id].keys()):
		if accounts_directory[src_acct_id][currency]["balance"] >= amt:
			accounts_directory[src_acct_id][currency]["balance"] -= amt
			accounts_directory[dst_acct_id][currency]["balance"] += amt
			return 0
	return 1

def printLedger():
	output = []
	for account_id in accounts_directory.keys():
		for currency in accounts_directory[account_id].keys():
			if accounts_directory[account_id][currency]["balance"] and accounts_directory[account_id][currency]["balance"] != 0:
				output.append(printAcctInfo(account_id, currency, accounts_directory[account_id][currency]["balance"]))
	return output

def printAcctInfo(acct_id: str, currency: str, balance: int):
	return str(f"acct_{acct_id},{currency},{balance}")

events = [
    "TX,acct_001,1,usd,1000",
    "TX,acct_002,2,usd,500",
    "TRANSFER,3,acct_001,acct_002,usd,300",
    "TRANSFER,4,acct_002,acct_001,usd,900"
]

processEvents(events)
ledger = printLedger()
print(ledger)
print(rejected_entries)
