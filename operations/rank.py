from fastmcp import FastMCP
from loguru import logger
from constants import *
from bilibili_api import sync, rank
server = FastMCP("bilibili-mcp-server")

def register_tools(server):
    @server.tool()
    def get_rank():
        return sync(rank.get_rank())