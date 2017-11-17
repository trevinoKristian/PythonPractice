import requests

"""
#My code 
#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response_object = requests.get(url)
print ("Status code:", response_object.status_code)

# Store API response to a dictionary variable
response_dict = response_object.json()

#Process results
print (response_dict.keys()) 
print ("\n")

#prints out the value for total_count, which is the number of repos
print (response_dict['total_count'])

#stores the repos and its info into a list
repositories = response_dict["items"]

#print out the number of repos
print (len(repositories))
print ("")

#examine the first repository
repo = repositories[0]
print ("\nNumber of Repo Keys: ", len(repo))
print ("\nEach Repo has the follwoing keys:")

#for key in sorted(repo.keys()):
#   print (key)

print (repo["name"])
"""

#----------------------------------------------------------------------------------------------
#book code

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print ("Status code:", r.status_code)

#Store API response in a variable
response_dict = r.json()

"""
#Process results
print (response_dict.keys())
print ("")
print ("Total Repositories:", response_dict["total_count"])
"""
#Explore information about the repositories
repo_dicts = response_dict['items']
#print ("Repositories returned:", len(repo_dicts))

#Examine the first repository
repo_dict = repo_dicts[0]
"""
print ("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print ("\nSelected information about first repository:")
print("Name:", repo_dict['name'])
print('Owner', repo_dict['owner']['login'])
print("Stars:", repo_dict['stargazers_count'])
print("Repositories:", repo_dict['html_url'])
print("Created:", repo_dict['created_at'])
print("Updated:", repo_dict['updated_at'])
print("Description:", repo_dict['description'])
"""

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("Name:", repo_dict['name'])
    print('Owner', repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repositories:", repo_dict['html_url'])
    print("Created:", repo_dict['created_at'])
    print("Updated:", repo_dict['updated_at'])
    print("Description:", repo_dict['description'])
    print("")
