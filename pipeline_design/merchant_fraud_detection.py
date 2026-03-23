"""
Author: Manav Gurnani

Problem: Merchant Fraud Detection
"""

from collections import defaultdict

# ----------------------------- Part I: Count Fraudulent Transactions -----------------------------

fraud_codes = ["stolen_card", "do_not_honor"]

merchant_entries = defaultdict(dict)
other_entries = []

def transactionProcessor(transactions: list[str]):
	for entry in transactions:
		metadata = entry.split(",")
		if len(metadata) < 4:
			other_entries.append(entry)
			continue
		merchant_id = metadata[0].split("_")[-1]
		if metadata[3] in fraud_codes:	
			if "failure_transactions" not in merchant_entries[merchant_id].keys():
				merchant_entries[merchant_id]["failure_transactions"] = []

			merchant_entries[merchant_id]["failure_transactions"].append({
				"transaction_id": metadata[1],
				"amount": metadata[2]
			})
		elif metadata[3] == "success":
			if "success_transactions" not in merchant_entries[merchant_id].keys():
				merchant_entries[merchant_id]["success_transactions"] = []

			merchant_entries[merchant_id]["success_transactions"].append({
				"transaction_id": metadata[1],
				"amount": metadata[2]
			})
		else:
			other_entries.append(entry)
			continue
		
def transactionAggregates():
	aggregates = []
	for merchant_id in merchant_entries.keys():
		num_fraud_transactions = len(merchant_entries[merchant_id]["failure_transactions"])
		if num_fraud_transactions >= 1:
			aggregates.append(f"merch_{merchant_id},{num_fraud_transactions}")
	return aggregates

transactions = [
    "merch_001,tx_1,100,success",
    "merch_001,tx_2,200,stolen_card",
    "merch_002,tx_3,150,insufficient_funds",
    "merch_001,tx_4,300,do_not_honor",
    "merch_002,tx_5,50,stolen_card"
]

transactionProcessor(transactions)
print(merchant_entries)
print(other_entries)
print(transactionAggregates())
