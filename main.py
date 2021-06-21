import requests

response = requests.get("https://api.github.com/users/isagesse/repos")
my_repository = response.json()

for repo in my_repository:
    print(f"Project Name: {repo['name']} \nProject Url: {repo['html_url']} \n")

