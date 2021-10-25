import requests

def searchDDG():
    url_DDG = "https://api.duckduckgo.com"
    response = requests.get(url_DDG + "/?q=presidents of the united states&format=json")
    site_json = response.json()
    results = site_json['RelatedTopics']
    list_of_related_results = []
    for answer in results:
        if (answer["Text"].find("president") != -1):
            list_of_related_results.append(answer["Text"])

    list_of_presidents_lastname_only = []
    for result in list_of_related_results:
        name = result.split("-")
        if (len(name[0].split(" ")) <= 5):
            president = name[0].strip().split(" ")
            list_of_presidents_lastname_only.append(president[len(president)-1])

    return(list_of_presidents_lastname_only)

list_of_presidents = searchDDG()
print(list_of_presidents)