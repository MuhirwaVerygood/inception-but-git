import os
import time
from datetime import datetime, timedelta
from random import randint

# Start 3 years ago
start_date = datetime.now() - timedelta(days=365 * 1)
now = datetime.now()

for i in range(1000):  # Number of commits
    random_days = randint(0, (now - start_date).days)
    commit_date = start_date + timedelta(days=random_days)

    # Ensure commit date does not exceed current time
    if commit_date > now:
        commit_date = now

    commit_date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    with open("hello.txt", "a") as f:
        f.write(f"Commit {i+1} on {commit_date_str}\n")

    os.system("git add .")
    os.system(f'GIT_COMMITTER_DATE="{commit_date_str}" git commit --date="{commit_date_str}" -m "Initial commit"')
    os.system("git push origin main")
    time.sleep(2)  # Avoid rate limiting

print("All commits pushed successfully without exceeding today’s date!")
