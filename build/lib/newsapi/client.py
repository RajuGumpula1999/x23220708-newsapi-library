# Main module for NewsAPI functionality


import requests

class NewsApiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://newsapi.org/v2/'

    def get_top_headlines(self, country='us', category=None, sources=None, q=None):
        """Fetch top headlines from the NewsAPI."""
        url = f"{self.base_url}top-headlines"
        params = {
            'apiKey': self.api_key,
            'country': country,
            'category': category,
            'sources': sources,
            'q': q  # query term, like 'bitcoin'
        }
        response = requests.get(url, params={k: v for k, v in params.items() if v})
        return response.json()

    def get_everything(self, q=None, sources=None, domains=None, exclude_domains=None, from_param=None, to=None, language='en', sort_by='publishedAt'):
        """Fetch all articles matching the parameters."""
        url = f"{self.base_url}everything"
        params = {
            'apiKey': self.api_key,
            'q': q,
            'sources': sources,
            'domains': domains,
            'excludeDomains': exclude_domains,
            'from': from_param,
            'to': to,
            'language': language,
            'sortBy': sort_by
        }
        response = requests.get(url, params={k: v for k, v in params.items() if v})
        return response.json()

    def get_sources(self, category=None, language='en', country=None):
        """Fetch the available news sources."""
        url = f"{self.base_url}sources"
        params = {
            'apiKey': self.api_key,
            'category': category,
            'language': language,
            'country': country
        }
        response = requests.get(url, params={k: v for k, v in params.items() if v})
        return response.json()
