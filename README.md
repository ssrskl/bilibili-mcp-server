# Bilibili-Mcp-Server
Bilibili-Mcp-Server 是一个针对Bilibili的MCP服务器，提供了以下功能：
- 视频：
  - 获取视频信息：获取视频的基本信息，如标题、描述、上传时间等。
  - 对视频点赞：用户可以对视频进行点赞操作。
- 用户：
  - 获取用户信息：获取用户的基本信息，如用户名、头像等。
  - 关注用户：用户可以关注其他用户。
  - 获得用户的硬币数量



## 使用方法
使用uv安装依赖
```bash
uv install
```
配置环境信息，在`.env`文件中填写`SESSDATA`，`BILI_JCT`，`DEDEUSERID`等信息
```txt
SESSDATA=your sessdata
BILI_JCT=your bili_jct
DEDEUSERID=your deuserid
```

可以使用fastmcp 的MCP Inspector 进行测试
```bash
fastmcp dev server.py
```

## MCP Server Configure
在配置文件中填写sessdata，bili_jct，deuserid等信息，获取方法见->[获取 Credential 类所需信息](https://nemo2011.github.io/bilibili-api/#/get-credential)
```json
"bilibili-mcp-server": {
"disabled": false,
"timeout": 60,
"command": "uv",
"args": [
    "--directory",
    "/Users/maoyan/Codes/Python/mcps/bilibili-mcp-server",
    "run",
    "server.py"
],
"env": {
    "SESSDATA":"your sessdata",
    "BILI_JCT":"your bili_jct",
    "DEDEUSERID":"your deuserid"
},
"transportType": "stdio"
}
```