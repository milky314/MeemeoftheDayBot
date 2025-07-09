import os
import requests
import tweepy

def post_meme():
    # Auth setup for Twitter API v2 using tweepy.Client
    client = tweepy.Client(
        consumer_key=os.getenv("API_KEY"),
        consumer_secret=os.getenv("API_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

    # Meme details
    image_url = "https://i.redd.it/3vqlgh6mxqb91.jpg"
    caption = "Elon trying to regulate AI after teaching it how to ratio people"
    filename = "meme.jpg"

    # Download meme image
    response = requests.get(image_url)
    with open(filename, "wb") as f:
        f.write(response.content)

    # Upload image to Twitter
    media = client.upload_media(filename=filename)

    # Post tweet with image
    client.create_tweet(text=caption, media_ids=[media.media_id])

    os.remove(filename)

if __name__ == "__main__":
    post_meme()
