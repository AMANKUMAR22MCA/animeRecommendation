import requests

def search_anime(query):
    url = 'https://graphql.anilist.co'
    payload = {
        'query': '''
        query ($search: String) {
            Page(perPage: 10) {
                media(search: $search, type: ANIME) {
                    id
                    title {
                        romaji
                    }
                    genres
                    popularity
                }
            }
        }''',
        'variables': {'search': query}
    }
    response = requests.post(url, json=payload)
    return response.json()
