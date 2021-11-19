from __init__endpoint import *
import pandas
#import database endpoint
search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
start_date='2021-11-15T00:00:00Z'
end_date='2021-11-14T00:00:00Z'
crypto_search_term=['$COW','CaashCow']
search_params = {
    'q': crypto_search_term,
    #'result_type': 'recent',
    'count': 100,  #max 100
    'since': start_date,
    'until': end_date

}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

tweet_data = search_resp.json()

for x in tweet_data['statuses']:
    print(x['text'] + '\n')
#print(tweet_data['statuses']['text']['created_at']['screen_name'])

#write data to CSV for easier manipulation
#https://developer.twitter.com/en/docs/tutorials/five-ways-to-convert-a-json-object-to-csv
df = pandas.DataFrame(tweet_data['data'])
df.to_csv('tweet_data_python.csv')
