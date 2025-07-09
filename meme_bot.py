import os
import requests
import tweepy

def post_meme(api):
    image_url = "https://i.redd.it/3vqlgh6mxqb91.jpg"
    caption = "Elon trying to regulate AI after teaching it how to ratio people"
    filename = "meme.jpg"

    response = requests.get(image_url)
    with open(filename, "wb") as img:
        img.write(response.content)

    api.update_status_with_media(caption, filename)
    os.remove(filename)

def main():
    auth = tweepy.OAuth1UserHandler(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET"),
        os.getenv("ACCESS_TOKEN"),
        os.getenv("ACCESS_TOKEN_SECRET")
    )
    api = tweepy.API(auth)
    post_meme(api)

if __name__ == "__main__":
    main()
