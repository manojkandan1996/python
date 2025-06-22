import requests

def fetch_top_headlines(api_key, country='in', category='technology'):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,
        'category': category,
        'apiKey': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == 'ok':
        print(f"\nTop {category.capitalize()} Headlines in {country.upper()}:\n")
        for i, article in enumerate(data['articles'], 1):
            print(f"{i}. {article['title']}")
    else:
        print("Failed to fetch news:", data.get('message'))

# ⬇️ New function here
def fetch_keyword_news(api_key, keyword='AI'):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': keyword,
        'sortBy': 'publishedAt',
        'apiKey': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == 'ok':
        print(f"\nTop news results for: {keyword}\n")
        for i, article in enumerate(data['articles'][:10], 1):
            print(f"{i}. {article['title']}")
    else:
        print("Error:", data.get('message'))

# Replace with your API key
api_key = 'fdf11c20a55947c291dc3f2a25fe0559'

# Choose which one to run:
# fetch_top_headlines(api_key, country='us', category='technology')
fetch_keyword_news(api_key, keyword='Java')