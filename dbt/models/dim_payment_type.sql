with source as (
    select *
    from {{ ref('raw_payment_type') }}
)
select * from source