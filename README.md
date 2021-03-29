# Case Study for use-case-data-processing
[See here](https://github.com/amitadlakha1/01-uc-bigdata-processing)

# Notes
This is actually not my goto solution to the problem but i wanted to use the function api
rather than building a sql query and executing it. for example
below approach is more debuggable and easier for me to implement
but i did not want to use my sql skills :)

```py
    def expressions()
        for metric in metrics:
            yield """
                max(case <cond> then event_date else null end) <col_name>
                # or
                sum(...)
            """

    column_exp = ", ".join([e for e in expressions])
    ...
    query = f"select {column_exp} ...."
    df = spark.sql(query)
```

# Why not Scala
Simply because I did not set my editor(vscode) for it and already have a pyspark env.


## Install dependencies
`poetry install`

## Build
`poetry build`

## Tests
`pytest`

### Running
```sh
spark-submit --py-files dist/adidascs-0.1.0.tar.gz app.py \
    --page_types news movies \
    --metric_types fre dur \
    --time_windows 360 \
    --ref_date 2019.10.12
```

### SQL
Also added `adidas.sqlite` which has the imported csv files if you want to debug with sql
- `select * from pages`
- `select * from page_views`