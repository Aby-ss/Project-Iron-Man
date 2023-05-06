import requests
from rich.console import Console
from rich.panel import Panel
from rich import box

from rich.traceback import install
install(show_locals=True)

NEWS_API_KEY = "d88f50af7b21490889c52621330e9a2c"
news_source = "bbc-news"  # Replace with your preferred news source

# Build the API request URL
url = f"https://newsapi.org/v2/top-headlines?sources={news_source}&apiKey={NEWS_API_KEY}"

# Send a GET request to the API and parse the response
response = requests.get(url)
articles = response.json()["articles"]

# Create a new console instance from Rich
console = Console()

# Loop through the articles and create a panel for each one
for article in articles:
    title = article["title"]
    description = article["description"]
    url = article["url"]
    panel = Panel(f"[bold]{title}[/bold]\n{description}\nLink: {url}\n", title=title, style = "Bold white", box = box.SQUARE)
    console.print(panel)
