import requests

class FetchPosts:
    def print_first_5_posts(url):
        data = requests.get(url)
        # Check if the request was successful (status code 200)
        if data.status_code == 200:
            # Convert JSON response to a Python list of dictionaries
            posts = data.json()
            # Loop to print the first 5 posts
            for post in posts[:5]:
                print("Title:", post['title'])
                print("Body:", post['body'])
                print()
        else:
            print("Error:", data.status_code)