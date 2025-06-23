from firecrawl import FirecrawlApp, ScrapeOptions
import requests

# JSONPlaceholder API base URL
JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com"

def search_stocks(api_key, company_name, token):
    """
    Search for stock price and news using Firecrawl.
    """
    try:
        app = FirecrawlApp(api_key=api_key)
        return app.search(
            query=f"{company_name} {token} stock price and latest news",
            limit=8,
            scrape_options=ScrapeOptions(formats=["markdown", "html"])
        )
    except Exception as e:
        return {"error": str(e)}

def get_posts(post_id=None):
    """
    Make a GET request to fetch posts from JSONPlaceholder.
    """
    url = f"{JSONPLACEHOLDER_URL}/posts/{post_id}" if post_id else f"{JSONPLACEHOLDER_URL}/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def create_post(title, body, user_id):
    """
    Make a POST request to create a post on JSONPlaceholder.
    """
    url = f"{JSONPLACEHOLDER_URL}/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}