import webbrowser

def openBrowser(text,prepand):
    query = text + prepand 
    search_url = "https://www.google.com/search?q=" + '+'.join(query.split())
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Path to Chrome executable may vary
    webbrowser.get(chrome_path).open(search_url)

# Example usage:
search_text = input("Enter text to search on Google: ")
openBrowser(search_text)
