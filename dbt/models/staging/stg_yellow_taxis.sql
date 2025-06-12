with source as (
    select *
    from {{ source(env_var('DWH_SCHEMA'), 'yellow_trips') }}
)
select * from source