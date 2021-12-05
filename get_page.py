import requests
from fb_page_access_token import page_access_token

rating = requests.get('https://graph.facebook.com/v12.0/{page-id}/ratings/', 
                      headers = {'Authorization': f"Bearer {page_access_token}"})