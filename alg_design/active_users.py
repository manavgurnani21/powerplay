"""
Author: Manav Gurnani

Problem: Active Users
Description: Given a list of (user_id, login_timestamp) tuples, return all users who logged in on at least 5 distinct days.
"""

from collections import defaultdict
from datetime import datetime, timedelta, date

# Given: List of login events [(user_id: str, login_date: str)]
# Login Date Format: YYYY-MM-DD (multiple possible logins per day)

def extractDatetimeObj(date_time: str):
	[date_split, time_split] = date_time.split(" ")
	year, month, day = date_split.split("-")
	hours, mins, seconds = time_split.split(":")
	date_obj = datetime(int(year), int(month), int(day), int(hours), int(mins), int(seconds))
	return date_obj

# Function that returns list of users who logged in on at least k distinct days
def activeUsers(logins: list[tuple[str, str, str]], k: int) -> list[str]:
	login_directory = defaultdict() # set <- distinct dates

	active = []

	# no logins
	if logins == []:
		return []  
	
	# for all pairs of login events
	# 1. extract the login date
	# 2. extract the logout date (next entry)
	# 3. for the range of dates, add all dates to the set
	for i in range(0,len(logins)-1,2):
		# looking at current and next events (login/logout)
		(curr_login_id, curr_login_date, curr_event_type) = logins[i]
		(curr_logout_id, curr_logout_date, future_event_type) = logins[i+1]
		if future_event_type != "LOGOUT" or curr_login_id != curr_logout_id:
			break # inconsistency in login/logout
		if curr_login_id not in login_directory.keys():
			login_directory[curr_login_id] = set()
		login_date = extractDatetimeObj(curr_login_date)
		logout_date = extractDatetimeObj(curr_logout_date)
		while login_date <= logout_date:
			login_directory[curr_login_id].add(login_date.date())
			login_date += timedelta(days=1)
	
	for user in login_directory.keys():
		login_dates_sorted = sorted(login_directory[user]) # sort the set of dates
		print(login_directory[user])
		# check for the following:
			# the kth element should be (oldest + k)
		for i in range(len(login_dates_sorted)-k+1):
			print(login_dates_sorted[i+k-1])
			print(login_dates_sorted[i] + timedelta(days=k-1))
			if login_dates_sorted[i+k-1] == login_dates_sorted[i] + timedelta(days=k-1) and user not in active:
				active.append(user)

	return active
	
logins = [
    ("alice", "2024-01-01 08:00:00", "LOGIN"),
    ("alice", "2024-01-01 17:00:00", "LOGOUT"),
    ("alice", "2024-01-02 08:00:00", "LOGIN"),
    ("alice", "2024-01-02 17:00:00", "LOGOUT"),
    ("alice", "2024-01-03 08:00:00", "LOGIN"),
    ("alice", "2024-01-03 17:00:00", "LOGOUT")
]

print(activeUsers(logins, k=4))
