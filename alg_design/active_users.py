"""
Author: Manav Gurnani

Problem: Active Users
Description: Given a list of (user_id, login_timestamp) tuples, return all users who logged in on at least 5 distinct days.
"""

from collections import defaultdict

# Given: List of login events [(user_id: str, login_date: str)]
# Login Date Format: YYYY-MM-DD (multiple possible logins per day)

# Function that returns list of users who logged in on at least k distinct days
def activeUsers(logins: list[tuple[str, str]], k: int) -> list[str]:
	login_directory = defaultdict() # set <- distinct dates

	active = []

	if logins == []:
		return []
	
	# for each login attempt
	for (login_id, date) in logins:
		if login_id not in login_directory.keys():
			login_directory[login_id] = set()
		login_directory[login_id].add(date)
	
	for user in login_directory.keys():
		if len(login_directory[user]) >= k:
			active.append(user)

	return active
	
logins = [
    ("alice", "2024-01-01"),
    ("alice", "2024-01-01"),
    ("alice", "2024-01-03"),
    ("alice", "2024-01-05"),
    ("bob", "2024-01-01"),
    ("bob", "2024-01-02"),
]

print(activeUsers(logins, k=2))
