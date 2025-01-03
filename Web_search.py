import webbrowser

def google_search(query):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    url = f"https://www.google.com/search?q={query}"
    webbrowser.get(chrome_path).open(url)

search_query = input("Enter your search query: ")
google_search(search_query)
