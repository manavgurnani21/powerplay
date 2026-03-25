"""
Author: Manav Gurnani

Problem: Active Users
Description: Given a list of (user_id, login_timestamp) tuples, return all users who logged in on at least 5 distinct days.
"""

from collections import defaultdict
from datetime import date, timedelta

# Given: List of login events [(user_id: str, login_date: str)]
# Login Date Format: YYYY-MM-DD (multiple possible logins per day)

# Function that returns list of users who logged in on at least k distinct days
def activeUsers(logins: list[tuple[str, str]], k: int) -> list[str]:
	login_directory = defaultdict() # set <- distinct dates

	active = []

	if logins == []:
		return []
	
	# for each login attempt
	for (login_id, login_date) in logins:
		if login_id not in login_directory.keys():
			login_directory[login_id] = set()
		date_split = login_date.split("-")
		year = int(date_split[0])
		month = int(date_split[1])
		day = int(date_split[2])
		date_obj = date(year, month, day)
		login_directory[login_id].add(date_obj)
	
	for user in login_directory.keys():
		login_dates_sorted = sorted(login_directory[user]) # sort the set of dates
		print(login_dates_sorted)
		# check for the following:
			# the kth element should be (oldest + k)
		for i in range(len(login_dates_sorted)-k+1):
			print(login_dates_sorted[i+k-1])
			print(login_dates_sorted[i] + timedelta(days=k-1))
			if login_dates_sorted[i+k-1] == login_dates_sorted[i] + timedelta(days=k-1) and user not in active:
				active.append(user)

	return active
	
logins = [
    ("alice", "2024-01-01"),
    ("alice", "2024-03-10"),
    ("alice", "2024-03-11"),
    ("alice", "2024-03-12"),
]

print(activeUsers(logins, k=4))
