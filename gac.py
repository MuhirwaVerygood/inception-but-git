import os
import time
import subprocess
from datetime import datetime, timedelta
from random import randint

# Start 1 year ago
start_date = datetime.now() - timedelta(days=365)
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
    
    # Add files
    subprocess.run(["git", "add", "."], check=True)
    
    # Set environment variables for this process
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = commit_date_str
    
    # Commit with backdated timestamp
    subprocess.run(
        ["git", "commit", f"--date={commit_date_str}", "-m", f"Commit {i+1}"],
        env=env,
        check=True
    )
    
    # Push
    subprocess.run(["git", "push", "origin", "main"], check=True)
    
    print(f"Pushed commit {i+1} with date {commit_date_str}")
    time.sleep(2)  # Avoid rate limiting

print("All commits pushed successfully without exceeding today's date!")