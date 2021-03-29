import pyspark.sql.functions as F
from adidascs.base import spark
from adidascs.settings import (
    PAGE_VIEWS_SCHEMA,
    PAGE_SCHEMA,
    PAGE_VIEWS_FILE,
    PAGES_FILE,
    DATE_FORMAT,
)
from adidascs.arguments import get_ref_date


def get_page_views():
    """
    has some dups. so added distinct
    """
    return (
        (
            spark.read.format("csv")
            .option("treatEmptyValuesAsNulls", "true")
            .option("header", "true")  # can be env to
            .option("dateFormat", DATE_FORMAT)
            .schema(PAGE_VIEWS_SCHEMA)
            .load(PAGE_VIEWS_FILE)
        )
        .distinct()
        .repartition("event_date")
    )


def get_pages():
    return (
        spark.read.format("csv")
        .option("header", "true")  # can be env to
        .schema(PAGE_SCHEMA)
        .load(PAGES_FILE)
    )


def get_base_set():
    pv, p, ref_date = get_page_views(), get_pages(), get_ref_date()
    return (
        pv.join(p.hint("broadcast"), p.web_pageid == pv.web_pageid)
        .filter(pv.event_date < ref_date)
        .select([pv.user_id, pv.event_date, p.webpage_type])
    )
