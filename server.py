# A simple aiohttp server that does the same thing as cli.py
# but hosts it on an app route

import asyncio
import logging
from aiohttp import web
from people import Crowd


app = web.Application()
async def handle(request):
    print("Got request")

    vibe = request.rel_url.query["vibe"] or ""
    crowd = Crowd(9, vibe=vibe)
    print(crowd)

    responses = await crowd.describe_image(request.rel_url.query["image"])
    # print(responses)
    print("Sending response")
    crowd = None
    return web.Response(text="".join(responses))

app.add_routes([web.post("/", handle)])
logging.info("running")
if  __name__ == "__main__":
    web.run_app(app, port=8080, host="0.0.0.0")