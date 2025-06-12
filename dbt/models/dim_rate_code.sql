with source as (
    select *
    from {{ ref('raw_rate_code') }}
)
select * from source