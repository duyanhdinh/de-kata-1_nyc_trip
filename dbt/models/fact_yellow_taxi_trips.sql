with src as (
    select *
    from {{ ref('stg_yellow_taxis') }}
),

fact as (
    select
        src.*,
        pt.type as payment_type_name,
        v.name as vendor_name,
        rc.name as rate_code_name
    from src
    left join {{ ref('dim_payment_type') }} pt
        on src.payment_type = pt.id
    left join {{ ref('dim_vendor') }} v
        on src.vendor_id = v.id
    left join {{ ref('dim_rate_code') }} rc
        on src.rate_code_id = rc.id
)

select * from fact
