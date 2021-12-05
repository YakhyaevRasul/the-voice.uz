import requests
import os

user_access_token = requests.get(f"https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&\
                        client_id={os.environ.get('APP_ID')}&\
                        client_secret={os.environ.get('APP_SECRET')}&\
                        fb_exchange_token={os.environ.get('SHORT_LIVED_USER_ACCESS_TOKEN')}").json()['access_token']

page_access_token = requests.get(f"https://graph.facebook.com/PAGE-ID?\
                        fields=access_token&\
                        access_token={user_access_token}")