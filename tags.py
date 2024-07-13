from TikTokApi import TikTokApi
import json
import asyncio
import pandas as pd

def get_cookies_from_file():
    with open('cookies.json') as f:
        cookies = json.load(f)

    cookies_kv = {}
    for cookie in cookies:
        cookies_kv[cookie['name']] = cookie['value']

    return cookies_kv

cookies = get_cookies_from_file()

def get_cookies(**kwargs):
    return cookies

async def main(tag_name, count):
    nicknames = []
    async with TikTokApi() as api:
        api._get_cookies = get_cookies
        await api.create_sessions()
        tag = api.hashtag(name=tag_name)
        async for vid in tag.videos(count=count):
            vid_dict = await vid.as_dict
            nickname = vid_dict['author']['nickname']
            nicknames.append(nickname)
    
    # Create a DataFrame from the nicknames list
    df = pd.DataFrame(nicknames, columns=['Nickname'])
    print(df)

if __name__ == "__main__":
    asyncio.run(main(tag_name="funny", count=20))
