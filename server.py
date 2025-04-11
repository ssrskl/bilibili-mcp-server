from fastmcp import FastMCP
from operations.videos import register_tools as register_videos_tools
from operations.rank import register_tools as register_rank_tools
from operations.user import register_tools as register_user_tools
from operations.favorite_list import register_tools as register_favorite_list_tools

server = FastMCP("bilibili-mcp-server")

register_videos_tools(server)
register_rank_tools(server)
register_user_tools(server)
register_favorite_list_tools(server)

if __name__ == "__main__":
    server.run()

