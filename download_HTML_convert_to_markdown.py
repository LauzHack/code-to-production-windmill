from bs4 import BeautifulSoup
import requests
import markdownify


def download_and_convert_to_markdown(url: str) -> str:
    # Download the content from the given URL
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Convert the HTML to Markdown
    markdown_text = markdownify.markdownify(str(soup), heading_style="ATX")

    return markdown_text


def main(url: str) -> str:
    # Call the function to download and convert content to markdown
    return download_and_convert_to_markdown(url)
