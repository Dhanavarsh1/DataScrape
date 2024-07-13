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
    data = []
    async with TikTokApi() as api:
        api._get_cookies = get_cookies
        await api.create_sessions()
        tag = api.hashtag(name=tag_name)
        async for vid in tag.videos(count=count):
            vid_dict = vid.as_dict
            author = vid_dict['author']
            author_stats = vid_dict['authorStats']
            data.append({
                "Nickname": author['nickname'],
                "Verified": author['verified'],
                "Follower Count": author_stats['followerCount'],
                "Following Count": author_stats['followingCount'],
                "Heart Count": author_stats['heartCount'],
                "Video Count": author_stats['videoCount']
            })
    
    # Create a DataFrame from the data list
    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    asyncio.run(main(tag_name="funny", count=20))
