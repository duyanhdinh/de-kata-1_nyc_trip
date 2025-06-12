with date_spine as (
    {{ dbt_utils.date_spine(
        datepart = 'day',
        start_date = "cast('2010-01-01' as date)",
        end_date = "cast('2030-12-31' as date)"
    ) }}
),

dim_date as (
    select
        to_char(date_day, 'DDMMYYYY') as id,
        extract(year from date_day) as year,
        extract(month from date_day) as month,
        extract(day from date_day) as day,
        lpad(cast(extract(month from date_day) as text), 2, '0') as month_text,
        lpad(cast(extract(day from date_day) as text), 2, '0') as day_text,
        to_char(date_day, 'FMDay') as day_name,
        extract(dow from date_day) as day_of_week,
        extract(doy from date_day) as day_of_year,
        to_char(date_day, 'YYYY-MM-DD') as full_date
    from date_spine
)

select * from dim_date
