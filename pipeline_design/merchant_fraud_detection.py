"""
Author: Manav Gurnani

Problem: Merchant Fraud Detection
"""

from collections import defaultdict

# ----------------------------- Part I: Count Fraudulent Transactions -----------------------------

fraud_codes = ["stolen_card", "do_not_honor"] # codes for fraud transactions

mccs = ["retail,0.5", "airline,3"] # merchant category codes to thresholds
merchants = ["merch_001,retail", "merch_002,airline", "merch_003,airline"] # merchant to category codes
minimum_transactions = 4 # minimum transactions to be evaluated

merchant_entries = defaultdict(dict)
other_entries = []

def merchantMCCMapping(merchants: list[str],mccs: list[str]) -> dict:
	mccs_dict = dict()
	merchant_dict = dict()
	for mcc in mccs: # updating MCCs into dictionary
		[category, threshold] = mcc.split(",")
		mccs_dict[category] = float(threshold) if "." in threshold else int(threshold)

	for merchant in merchants: # using dict to format merchant entries
		[merch_id, category] = merchant.split(",")
		merchant_dict[merch_id] = mccs_dict[category]

	return dict(sorted(merchant_dict.items()))

def transactionProcessor(transactions: list[str]):
	for entry in transactions:
		metadata = entry.split(",")
		if len(metadata) < 4:
			other_entries.append(entry)
			continue
		merchant_id = metadata[0]
		if "failure_count" not in merchant_entries[merchant_id].keys():
			merchant_entries[merchant_id]["failure_count"] = 0
		if metadata[3] in fraud_codes:
			merchant_entries[merchant_id]["failure_count"] += 1

		if "transactions" not in merchant_entries[merchant_id].keys():
				merchant_entries[merchant_id]["transactions"] = []

		merchant_entries[merchant_id]["transactions"].append({
			"transaction_id": metadata[1],
			"amount": metadata[2]
		})
		
def transactionAggregates():
	flagged = []
	for merchant_id in merchant_entries.keys():
		num_fraud_transactions = merchant_entries[merchant_id]["failure_count"]
		num_transactions = len(merchant_entries[merchant_id]["transactions"])
		if merchant_id not in merchant_mcc.keys() or num_transactions < minimum_transactions:
			print("Skipping this transaction...")
			continue
		if type(merchant_mcc[merchant_id]) is int:
			# handling threshold
			if num_fraud_transactions >= merchant_mcc[merchant_id]:
				flagged.append(merchant_id)
		elif type(merchant_mcc[merchant_id]) is float:
			# handling ratio
			if (num_fraud_transactions / num_transactions) >= merchant_mcc[merchant_id]:
				flagged.append(merchant_id)
	return flagged

transactions = [
    "merch_001,tx_1,100,stolen_card",
    "merch_001,tx_2,200,success",
    "merch_001,tx_3,150,stolen_card",
    "merch_001,tx_4,300,success",
    "merch_002,tx_5,50,stolen_card",
    "merch_002,tx_6,50,stolen_card"
]

merchant_mcc = merchantMCCMapping(merchants,mccs)
print(merchant_mcc)
transactionProcessor(transactions)
print(merchant_entries)
print(other_entries)
print(transactionAggregates())
