from datetime import datetime
import argparse
from itertools import product

parser = argparse.ArgumentParser()

parser.add_argument(
    "--page_types",
    default=["news", "movies"],
    nargs="+",
    help="List of page types. eg. news movies",
)
parser.add_argument(
    "--metric_types",
    nargs="+",
    help="List of metric types. eg. fe dur",
)
parser.add_argument(
    "--time_windows",
    nargs="+",
    type=int,
    help="List of time windows. eg. 365 730 1460 2920",
)
parser.add_argument(
    "--ref_date",
    default=datetime.strptime("2019.10.12", "%Y.%m.%d"),
    type=lambda x: datetime.strptime(x, "%Y.%m.%d"),
    help="Reference data yyyy.mm.dd eg. 2019.10.12",
)

_args = parser.parse_args()


def get_arguments():
    # for tests
    return _args


def get_metrics():
    return list(product(_args.page_types, _args.metric_types, _args.time_windows))


def get_ref_date():
    return _args.ref_date
