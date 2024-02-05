"""
Script for creating a scrubbed version of a customer database.
Sensitive IDs and values are either randomized or hashed with md5.
"""

from hashlib import md5

salt = md5("secret")

scrub_query_sql = f"""
select setseed(0.31415);
create database scrubbed_data;
create table scrubbed_data.main.relation1 as
select
    md5(customer_id) as id1,
    md5(concat(customer_varchar_field::varchar, '{salt}')) as field1,
    customer_timestamp as timestamp1,
    customer_flag as flag1,
    -- customer_integer_field
    (random()*10)::integer as field2,
    --- customer_float_field
    (random() * 1e2)::FLOAT as field3

from customer_data.main.customer_relation;
"""
