import requests
import restfulAPI

test_url = "https://api.duckduckgo.com"

def test_DDG_0():
    resp = requests.get(test_url + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]

def test_DDG_1():
    list_of_presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson",
    "Van Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", 
    "Johnson", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison", "McKinley", "Roosevelt",
    "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy", 
    "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Bush", "Obama", "Trump", "Biden"]

    assert list_of_presidents.sort() == restfulAPI.list_of_presidents.sort()