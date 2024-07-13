from TikTokApi import TikTokApi
import json
import asyncio

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
    async with TikTokApi() as api:
        api._get_cookies = get_cookies
        await api.create_sessions()
        tag = api.hashtag(name=tag_name)
        async for vid in tag.videos(count=count):
            print(vid)
            print(vid.as_dict)
            print(vid.nickname)
            print('--------------')
        print()

if __name__ == "__main__":
    asyncio.run(main(tag_name="funny", count=20))
