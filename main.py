import tweepy
import pandas as pd
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Email credentials
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_email_password'
RECIPIENT_EMAIL = 'recipient_email@gmail.com'

# Setup Tweepy API authentication
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Keywords to search for
keywords = ['#JJKSpoilers', '#JJKLeaks', '#JujutsuKaisenLeaks']

# CSV file to store the data
csv_file = 'jjk_leaks.csv'

# Function to scrape tweets
def scrape_tweets(keywords):
    tweets_list = []
    for keyword in keywords:
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode='extended').items(100):
            tweet_info = {
                'date': tweet.created_at,
                'user': tweet.user.screen_name,
                'text': tweet.full_text,
                'link': f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}",
                'likes': tweet.favorite_count
            }
            tweets_list.append(tweet_info)
    return tweets_list

# Function to save tweets to CSV
def save_to_csv(tweets_list, csv_file):
    df = pd.DataFrame(tweets_list)
    df = df.sort_values(by='likes', ascending=False)
    df.to_csv(csv_file, mode='a', header=not pd.read_csv(csv_file).empty, index=False)

# Function to send email
def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

# Main function
def main():
    tweets_list = scrape_tweets(keywords)
    save_to_csv(tweets_list, csv_file)
    print(f'Scraped and saved {len(tweets_list)} tweets.')
    
    # Sort tweets by likes and create email body with links to tweets
    sorted_tweets = sorted(tweets_list, key=lambda x: x['likes'], reverse=True)
    body = f'Scraped and saved {len(tweets_list)} tweets.\n\n'
    body += 'Links to the tweets (sorted by likes):\n\n'
    for tweet in sorted_tweets:
        body += f"{tweet['date']} - {tweet['user']} ({tweet['likes']} likes): {tweet['text'][:50]}...\n{tweet['link']}\n\n"
    
    subject = 'Weekly JJK Spoiler Tracker Report'
    send_email(subject, body)

if __name__ == "__main__":
    main()
