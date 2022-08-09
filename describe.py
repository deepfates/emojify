import aiohttp
import asyncio
from pathlib import Path
# from emojify import Emojifier

async def call_api(session, img, personality):
    resp = await session.post(
                    f"http://cliptalk.tenant-mobilecoin-imogen.knative.chi.coreweave.com/?={personality}",
                    data={"img": img},
                ) 
    return (personality, (await resp.json())[:5])

async def get_img_from_url(url):
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        return(await resp.read())

async def describe(img, personalities=["Creative"]):
    
    async with aiohttp.ClientSession() as session:
        if Path(img).is_file():
            img = open(Path(img), "rb").read()
        else:
            img_resp = await session.get(img)
            img = await img_resp.read()
        tasks = [] 
        for p in personalities:
            tasks.append(asyncio.create_task(call_api(session, img, p)))

        original_result = await asyncio.gather(*tasks)
        return(original_result)

if __name__ == "__main__":
    print(asyncio.run(describe("test.jpeg")))