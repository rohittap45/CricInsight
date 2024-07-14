import requests

API_KEY = 'a33add3c-4010-41b9-a1a9-09af530094f0'
# API_KEY= '3cc5ce96-4caf-42e2-9eca-1bcaa292909b'
BASE_URL = 'https://api.cricapi.com/v1/'
# url='https://api.cricapi.com/v1/match_scorecard?apikey=3cc5ce96-4caf-42e2-9eca-1bcaa292909b&id=77a3092c-fbe6-4f28-80f7-69faafcbf3c6'

def get_live_matches():
    url = f'{BASE_URL}/currentMatches'
    params = {'apikey': API_KEY}
    response = requests.get(url, params=params)
    return response.json()


def get_live_match_data(match_id):
    url = f"https://api.cricapi.com/v1/match_scorecard?apikey={API_KEY}&id={match_id}"
    response = requests.get(url)
    return response.json()