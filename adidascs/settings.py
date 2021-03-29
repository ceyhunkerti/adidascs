from os import environ as env
from dotenv import load_dotenv

load_dotenv()


APP_NAME = env.get("ADIDASCS_APP_NAME", "Adidas Case Study")

PAGE_VIEWS_SCHEMA = env.get(
    "ADIDASCS_PAGE_VIEWS_SCHEMA", "user_id INT, event_date DATE, web_pageid INT"
)
PAGE_VIEWS_FILE = env.get(
    "ADIDASCS_PAGE_VIEWS_FILE",
    "/home/ceyhun/projects/lab/adidas/cases-study/data/page-views.csv",
)

PAGE_SCHEMA = env.get("ADIDASCS_PAGE_SCHEMA", "web_pageid INT, webpage_type STRING")
PAGES_FILE = env.get(
    "ADIDASCS_PAGES_FILE",
    "/home/ceyhun/projects/lab/adidas/cases-study/data/pages.csv",
)

DATE_FORMAT = env.get("ADIDASCS_DATE_FORMAT", "dd/MM/yyyy HH:mm")

OUTPUT_PATH = env.get("ADIDASCS_OUTPUT_PATH", "/home/ceyhun/projects/lab/adidas/output")
