import requests
import json

url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return None

def get_answered_yes(data):
    answeredYes = 0
    for item in data['items']:
        if item['is_answered']:
            answeredYes += 1
    return answeredYes

def get_answered_no(data):
    answeredNo = 0
    for item in data['items']:
        if not item['is_answered']:
            answeredNo += 1
    return answeredNo

def get_topic_with_lower_view(data):
    views = 999999999
    title = ""
    for item in data['items']:
        if item['view_count'] < views:
            views = item['view_count']
            title = item['title']
    return views, title

def get_topic_with_higher_view(data):
    views = 0
    title = ""
    for item in data['items']:
        if item['view_count'] > views:
            views = item['view_count']
            title = item['title']
    return views, title

def get_oldest_topic(data):
    oldest = 999999999999999
    title = ""
    for item in data['items']:
        if item['creation_date'] < oldest:
            oldest = item['creation_date']
            title = item['title']
    return oldest, title

def get_newest_topic(data):
    newest = 0
    title = ""
    for item in data['items']:
        if item['creation_date'] > newest:
            newest = item['creation_date']
            title = item['title']
    return newest, title

def get_owners(data):
    owners = []
    for item in data['items']:
        if item['owner']['display_name'] not in owners:
            owners.append(item['owner'])
    return owners

def get_owner_with_most_reputation(owners):
    reputation = 0
    display_name = ""
    for owner in owners:
        if owner['reputation'] > reputation:
            reputation = owner['reputation']
            display_name = owner['display_name']
    return reputation, display_name

# def get_owner_with_most_reputations(data):
#     reputations = 0
#     owner = ""
#     for item in data['items']:
#         if item['owner']['reputation'] > reputations:
#             reputations = item['owner']['reputation']
#             owner = item['owner']['display_name']
#     return reputations, owner

data = get_data(url)
owners = get_owners(data)

print("Answered Yes: " + str(get_answered_yes(data)))
print("Answered No: " + str(get_answered_no(data)))
print("Topic with lower view: " + str(get_topic_with_lower_view(data)))
print("Topic with higher view: " + str(get_topic_with_higher_view(data)))
print("Oldest topic: " + str(get_oldest_topic(data)))
print("Newest topic: " + str(get_newest_topic(data)))
print("Owner with most reputations: " + str(get_owner_with_most_reputation(owners)))