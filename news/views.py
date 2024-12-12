import requests
from django.shortcuts import render

# Define the API key directly in the code
API_KEY = '3012cf51d0c845ad890c9b51c2ff338f'  # Replace with your actual API key
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'

# About page view
def about(request):
    return render(request, 'news/about.html')

# Contact page view
def contact(request):
    return render(request, 'news/contact.html')

# Fetch news from the API and render it
def fetch_news(request):
    try:
        # Send GET request to the NewsAPI endpoint
        response = requests.get(url)
        response.raise_for_status()  # Will raise an error for bad HTTP responses (e.g., 404 or 500)

        # Parse the JSON response
        data = response.json()
        
        # Extract articles from the response
        articles = data.get('articles', [])
    except requests.exceptions.RequestException as e:
        # Handle any request errors (e.g., network issues, API down)
        articles = []
        print(f"Error fetching news: {e}")
    except ValueError:
        # Handle JSON parsing errors
        articles = []
        print("Error parsing the API response")

    # Render the articles in the HTML template
    return render(request, 'news/index.html', {'articles': articles})
