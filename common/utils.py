from dotenv import load_dotenv
from bilibili_api import Credential
import os

load_dotenv()

def get_Credential():
    credential = Credential(
        sessdata=os.environ.get("SESSDATA"),
        bili_jct=os.environ.get("BILI_JCT"),
        dedeuserid=os.environ.get("DEDEUSERID")
        )
    return credential