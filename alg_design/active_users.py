"""
Author: Manav Gurnani

Problem: Active Users
Description: Given a list of (user_id, login_timestamp) tuples, return all users who logged in on at least 5 distinct days.
"""

from collections import defaultdict
from datetime import datetime, timedelta, date

# Given: List of login events [(user_id: str, login_date: str)]
# Login Date Format: YYYY-MM-DD (multiple possible logins per day)

class ActiveUserTracker:

	login_directory = defaultdict()

	def __init__(self, k: int):
		self.k = k
	
	def extractDatetimeObj(self, date_time: str): # do I even need this here?
		[date_split, time_split] = date_time.split(" ")
		year, month, day = date_split.split("-")
		hours, mins, seconds = time_split.split(":")
		date_obj = datetime(int(year), int(month), int(day), int(hours), int(mins), int(seconds))
		return date_obj
	
	def process_event(self, user_id: str, timestamp: str, event_type: str) -> None:
		# processing a singular event (adding to user login directory)
		if user_id not in self.login_directory.keys():
			if event_type != "LOGIN":
				return
			self.login_directory[user_id] = defaultdict()
		
		curr_date = self.extractDatetimeObj(timestamp)
		prev_date = self.login_directory[user_id]["last_date"] if "last_date" in self.login_directory[user_id].keys() else curr_date
		curr_streak = self.login_directory[user_id]["streak"] if "streak" in self.login_directory[user_id].keys() else 1
		delta = (curr_date - prev_date).days
		if delta == 1: # update current streak if logged in yesterday
			curr_streak += 1
		elif delta >= 1:
			curr_streak = 1 # reset streak if broken
		print(curr_streak)
		login_data = {
			"last_date": curr_date,
			"streak": curr_streak
		}
		self.login_directory[user_id] = login_data

	# Checks to see in login directory for streaks of k+ days
	def activeUsers(self) -> list[str]:
		active = []
		for user in self.login_directory.keys():
			if self.login_directory[user]["streak"] >= self.k:
				active.append(user)
		return active
	
tracker = ActiveUserTracker(k=3)
tracker.process_event("alice", "2024-01-01 08:00:00", "LOGIN")
tracker.process_event("alice", "2024-01-02 08:00:00", "LOGIN")
tracker.process_event("alice", "2024-01-03 08:00:00", "LOGIN")
print(tracker.activeUsers())
