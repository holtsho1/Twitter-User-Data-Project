from __init__endpoint import *

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

crypto_search_term='Cryptocurrency'
search_params = {
    'q': crypto_search_term,
    'result_type': 'recent',
    'count': 2
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

tweet_data = search_resp.json()

for x in tweet_data['statuses']:
    print(x['text'] + '\n')
