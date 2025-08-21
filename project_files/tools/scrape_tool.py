import trafilatura

def scrape_url(url):
    """Download and extract main text from a web page."""
    downloaded = trafilatura.fetch_url(url)
    if downloaded:
        return trafilatura.extract(downloaded)
    return ""