with source as (
    select *
    from {{ ref('raw_taxi_zone') }}
)
select * from source