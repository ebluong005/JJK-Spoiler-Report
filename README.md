# Jujutsu Kaisen Spoiler Tracker

This project is a Twitter scraper that tracks spoilers for the Jujutsu Kaisen (JJK) manga. The script runs weekly on Wednesday night/Thursday morning, scrapes tweets with specific hashtags related to JJK spoilers, sorts them by the number of likes, and sends an email with the tweet links.

## Features

- Scrapes tweets with hashtags: `#JJKSpoilers`, `#JJKLeaks`, `#JujutsuKaisenLeaks`
- Includes retweets
- Sorts tweets by the number of likes
- Saves scraped data to a CSV file
- Sends a weekly email with the links to the tweets

## Prerequisites

- Python 3.x
- Tweepy
- Pandas

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/jjk-spoiler-tracker.git
   cd jjk-spoiler-tracker

2. Install the required libraries:
   ```bash
   pip install tweepy pandas

3. Update the script with your credentials:
   ```bash
   Twitter API credentials (API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
   Email credentials (EMAIL_ADDRESS, EMAIL_PASSWORD, RECIPIENT_EMAIL)
    
