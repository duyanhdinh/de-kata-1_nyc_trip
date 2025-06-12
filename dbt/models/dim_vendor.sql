with source as (
    select *
    from {{ ref('raw_vendor') }}
)
select * from source