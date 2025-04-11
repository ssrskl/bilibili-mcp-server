from calendar import c

from fastmcp import FastMCP
import requests
import json
from loguru import logger
from constants import *
from bilibili_api import hot, sync, video
from common.utils import get_Credential
server = FastMCP("bilibili-mcp-server")
credential = get_Credential()

def register_tools(server):
    @server.tool()
    def get_hotest_videos(number: int = 10):
        response = requests.get(f"{HOT_URL}?limit={number}")
        if response.status_code == 200:
            data = json.loads(response.text)["list"]
            return data
        else:
            return None

    @server.tool()
    def test(pn: int = 1, ps: int = 20):
        return sync(hot.get_hot_videos(pn, ps))

    @server.tool()
    async def get_video_info(bvid: str):
        v = video.Video(bvid=bvid)
        v_info = await v.get_info()
        return v_info

    @server.tool()
    async def like_video(bvid: str):
        v = video.Video(bvid=bvid, credential=credential)
        return await v.like()
