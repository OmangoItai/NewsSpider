from typing import Callable, List
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()
WXGZH_API = os.getenv("WXGZH_API")
JZL_KEY = os.getenv("JZL_KEY")

ScanningLogicType = Callable[[], List[str]]

# firefox_options = Options()
# firefox_options.headless = True

# driver = webdriver.Firefox(options=firefox_options)

def WXGZH(url: str):
    params = {
        "key" : JZL_KEY,
        "url" : url
    }
    res = requests.get(url = WXGZH_API, params=params).json()
    urls = [item["url"] for item in res["data"]]
    urls = urls[:2]
    return urls
