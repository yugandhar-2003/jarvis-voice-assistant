import datetime
import webbrowser
import urllib.parse
import wikipedia

def handle_jarvis_command(command):
    command = command.lower()

    # ✅ Time
    if "time" in command:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}"

    # ✅ Date
    elif "date" in command:
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}"

    # ✅ YouTube Search (Flexible)
    elif "play" in command:
        if "youtube" in command:
            search_query = command.replace("play", "").replace("on youtube", "").replace("youtube", "").strip()
            encoded_query = urllib.parse.quote_plus(search_query)
            url = f"https://www.youtube.com/results?search_query={encoded_query}"
            webbrowser.open(url)
            return f"Searching YouTube for {search_query}"
        else:
            return "Do you want me to search YouTube? Please say 'on YouTube' in your command."

    # ✅ Open Websites
    elif "open" in command:
        if "wikipedia" in command:
            webbrowser.open("https://www.wikipedia.org")
            return "Opening Wikipedia"
        elif "google" in command:
            webbrowser.open("https://www.google.com")
            return "Opening Google"
        elif "gmail" in command:
            webbrowser.open("https://mail.google.com")
            return "Opening Gmail"
        elif "github" in command:
            webbrowser.open("https://github.com")
            return "Opening GitHub"
        else:
            return "I don't recognize that website."

    # ✅ Google Search
    elif "search" in command:
        query = command.replace("search", "").strip()
        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://www.google.com/search?q={encoded_query}"
        webbrowser.open(url)
        return f"Searching Google for {query}"

    # ✅ Wikipedia Answer (fallback)
    else:
        try:
            summary = wikipedia.summary(command, sentences=2)
            return summary
        except wikipedia.exceptions.DisambiguationError:
            return "That topic is too broad. Try being more specific."
        except wikipedia.exceptions.PageError:
            return "Sorry, I couldn't find anything on that topic."
        except Exception as e:
            return f"An error occurred: {str(e)}"
