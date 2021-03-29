# Output metrics naming convention to be followed:
# pageview_<pagetype>_<metrictype>_<timewindow>
#
# input parameters
#
# pagetype – 'news, movies'
# metrictype – 'fre, dur'
# timewindow – '365, 730, 1460, 2920'
# dateofreference - '12/10/2019'
#
# fre - frequency of page views (count)
# dur - recency of page views (no. of days since the last page view from date of reference)
#
# Metric definitions:
# pageview_news_fre_365 - no of page views for news page type in last 365 days
# pageview_news_dur_730 - recency of page views for news category in last 365 da

import pyspark.sql.functions as F
import adidascs.arguments as args
from adidascs.dfloader import get_base_set
from adidascs.settings import OUTPUT_PATH


def get_metrics():
    dur = lambda condition, days: F.min(F.when(condition, days).otherwise(None))
    # that's not cool
    fre = lambda condition, _: F.sum(F.when(condition, 1).otherwise(0))

    # # page_type, metric_type, time_window, *func
    metrics = [(*m, dur if m[1] == "dur" else fre) for m in args.get_metrics()]
    keys = ["page_type", "metric_type", "time_window", "func"]
    return [dict(zip(keys, m)) for m in metrics]


def get_expressions():
    col_name = (
        lambda x: f"pageview_{x['page_type']}_{x['metric_type']}_{x['time_window']}"
    )
    ref_date = args.get_ref_date()
    return [
        m["func"](
            (
                (m["time_window"] > F.datediff(F.lit(ref_date), F.col("event_date")))
                & (F.col("webpage_type") == m["page_type"])
            ),
            F.datediff(F.lit(ref_date), F.col("event_date")),
        ).alias(col_name(m))
        for m in get_metrics()
    ]


def run():
    df = get_base_set()
    return df.groupBy(df.user_id).agg(*get_expressions())


if __name__ == "__main__":
    # can be different formats too
    run().write.mode("overwrite").csv(OUTPUT_PATH)
