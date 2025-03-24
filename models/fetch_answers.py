import requests

GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"

def search_answer(question):
    """Fetches the top answer from Google Search API."""
    url = f"https://www.googleapis.com/customsearch/v1?q={question}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(url).json()
    if "items" in response:
        return response["items"][0]["snippet"]
    return "No answer found."

if __name__ == "__main__":
    print(search_answer("What is a neural network?"))
