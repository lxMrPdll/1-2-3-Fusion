import requests
import json

def get_repositories(username):
    """
    Returns a list of repositories for a given username
    """
    url = "https://api.github.com/users/{}/repos".format(username)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_repository_names(username):
    """
    Returns a list of repository names for a given username
    """
    repositories = get_repositories(username)
    if repositories:
        return [repo["name"] for repo in repositories]
    else:
        return None

lxMrPdll = get_repository_names("lxMrPdll")

print(lxMrPdll)

# def get_repositories(user):
#     """List all names of GitHub repositories for a user."""
#     url = 'https://api.github.com/users/' + user + '/repos'
#     request = urllib.request.Request(url)
#     response = urllib.request.urlopen(request)
#     data = json.loads(response.read().decode())
#     return [repo['name'] for repo in data]

# lxMrPdll = get_repositories('lxMrPdll')

# print(lxMrPdll)