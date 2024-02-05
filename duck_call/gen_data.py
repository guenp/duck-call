num_rows = 42

gen_query_sql = f"""
create database customer_data;
create table customer_relation AS (
    select
        uuid()::VARCHAR as customer_id,
        uuid()::VARCHAR as customer_varchar_field,
        '2024-02-01'::timestamp + interval 1 minute * (random() * 20000)::int as customer_timestamp,
        (random() > 0.5)::bool as customer_flag,
        (random()*10)::integer as customer_integer_field,
        CAST(1e12 * random() AS FLOAT) as customer_float_field
    from generate_series(1, {num_rows}) g(x)
"""
