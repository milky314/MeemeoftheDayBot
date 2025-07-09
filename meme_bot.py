import os
import requests
import tweepy

def post_meme():
    # Step 1: Auth for v1.1 (media upload)
    auth = tweepy.OAuth1UserHandler(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET"),
        os.getenv("ACCESS_TOKEN"),
        os.getenv("ACCESS_TOKEN_SECRET")
    )
    api_v1 = tweepy.API(auth)

    # Step 2: Auth for v2 (tweet posting)
    client = tweepy.Client(
        consumer_key=os.getenv("API_KEY"),
        consumer_secret=os.getenv("API_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

    # Meme info
    image_url = "https://i.redd.it/3vqlgh6mxqb91.jpg"
    caption = "Elon trying to regulate AI after teaching it how to ratio people"
    filename = "meme.jpg"

    # Download image
    response = requests.get(image_url)
    with open(filename, "wb") as f:
        f.write(response.content)

    # Upload image (v1.1)
    media = api_v1.media_upload(filename)

    # Post tweet (v2)
    client.create_tweet(text=caption, media_ids=[media.media_id])

    os.remove(filename)

if __name__ == "__main__":
    post_meme()
