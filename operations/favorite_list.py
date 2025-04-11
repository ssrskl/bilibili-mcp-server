from fastmcp import FastMCP
from loguru import logger
from constants import *
from bilibili_api import sync, favorite_list
from bilibili_api.favorite_list import (
    FavoriteListContentOrder,
    SearchFavoriteListMode
)
from common.utils import get_Credential

server = FastMCP("bilibili-mcp-server")
credential = get_Credential()

def register_tools(server):
    @server.tool()
    def get_favorite_list_content(
        media_id: int, 
        page: int = 1,
        keyword: str = None,
        order: FavoriteListContentOrder = FavoriteListContentOrder.MTIME,
        tid : int = 0,
        mode : SearchFavoriteListMode = SearchFavoriteListMode.ONLY
        ):
        return sync(favorite_list.get_video_favorite_list_content(
            media_id=media_id,
            page=page,
            keyword=keyword,
            order=order,
            tid=tid,
            mode=mode,
            credential=credential
        ))