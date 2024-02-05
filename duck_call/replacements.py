"""
Script for replacing table and field names in query after scrubbing data
"""
from hashlib import md5

salt = md5("secret")

query_to_scrub = """
select
    customer_id,
    customer_varchar_field,
    customer_timestamp,
    customer_flag,
    customer_integer_field,
    customer_float_field
from customer_data.main.customer_relation
where customer_varchar_field = "SomeValue";
"""

replacements = {
    "customer_data.main.customer_relation": "scrubbed_data.main.relation1",
    "customer_id": "id1",
    "customer_varchar_field": "field1",
    "customer_timestamp": "timestamp1",
    "customer_flag": "flag1",
    "customer_integer_field": "field2",
    "customer_float_field": "field3",
    "SomeValue": md5(b"SomeValue" + salt).hexdigest(),
}

for a, b in replacements.items():
    query_to_scrub = query_to_scrub.replace(a, b)

print(query_to_scrub)
