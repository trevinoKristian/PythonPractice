import requests

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print "Status code:", r.status_code

# Store API response in a variable
response_dict = r.json()

#Process results
print response_dict.keys()