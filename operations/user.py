from fastmcp import FastMCP
from loguru import logger
from constants import *
from bilibili_api import sync, user
from common.utils import get_Credential

server = FastMCP("bilibili-mcp-server")
credential = get_Credential()

def register_tools(server):
    @server.tool()
    def get_self_coins():
        # return credential
        return sync(user.get_self_coins(credential))