# JJK-Spoiler-Report
Jujutsu Kaisen Spoiler Tracker
This project is a Twitter scraper that tracks spoilers for the Jujutsu Kaisen (JJK) manga. The script runs weekly on Wednesday night/Thursday morning, scrapes tweets with specific hashtags related to JJK spoilers, sorts them by the number of likes, and sends an email with the tweet links.

Features

* Scrapes tweets with hashtags: #JJKSpoilers, #JJKLeaks, #JujutsuKaisenLeaks
* Includes retweets
Sorts tweets by the number of likes
Saves scraped data to a CSV file
Sends a weekly email with the links to the tweets

Prerequisites
Python 3.x
Tweepy
Pandas
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/jjk-spoiler-tracker.git
cd jjk-spoiler-tracker
Install the required libraries:

bash
Copy code
pip install tweepy pandas
Update the script with your credentials:

Twitter API credentials (API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
Email credentials (EMAIL_ADDRESS, EMAIL_PASSWORD, RECIPIENT_EMAIL)
Usage
Run the script manually:

bash
Copy code
python3 script.py
Schedule the script to run weekly:

On Unix-based systems (Linux, macOS):

Open the crontab file:

bash
Copy code
crontab -e
Add the following line to schedule the script (adjust the path to your script):

bash
Copy code
0 2 * * 4 /usr/bin/python3 /path/to/your/script.py
On Windows:

Open Task Scheduler and create a new task.
Set the trigger to run weekly on Thursday at the desired time.
Set the action to start a program and browse to your Python executable.
Add the script path as an argument.
