import requests
from constant import app_id, app_secret

data = {'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': app_secret}
token = requests.post('https://api.yelp.com/oauth2/token', data=data)
access_token = token.json()['access_token']
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'bearer %s' % access_token}
params = {'location': 'San Francisco',
          'term': 'Restaurant',
          'sort_by': 'review_count',
          'bounds': '37.900000,-122.500000|37.788022,-122.399797',
          'limit': 5
         }

resp = requests.get(url=url, params=params, headers=headers)
print resp.json()['businesses']
