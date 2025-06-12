with time_spine as (
   select
      (generate_series(
        '2000-01-01 00:00:00'::timestamp,
        '2000-01-01 23:59:00'::timestamp,
        interval '1 minute'
      ))::time as time_value
),

dim_time as (
    select
        to_char(time_value, 'HH24:MI:SS') as id,
        extract(hour from time_value) as hour,
        extract(minute from time_value) as minute,
        case
            when extract(hour from time_value) between 0 and 5 then 'Late Night'
            when extract(hour from time_value) between 6 and 11 then 'Morning'
            when extract(hour from time_value) between 12 and 17 then 'Afternoon'
            else 'Evening'
        end as time_of_day
    from time_spine
)

select * from dim_time
