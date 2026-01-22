/*
SELECT 'green_tripdata_202511' tableName, count(*) total
	FROM public.green_tripdata_202511
union all 
	select 'taxi_zone_lookup' tableName, count(*) total
	from public.taxi_zone_lookup;
*/

--Q3
/*
select count(*) from green_tripdata_202511
--order by lpep_pickup_datetime desc
where lpep_pickup_datetime >= '2025-11-01'  
and  lpep_pickup_datetime < '2025-12-01'
and trip_distance<=1
--order by trip_distance desc
*/


--Q4

/*
select  * from green_tripdata_202511
where 
 trip_distance<100
order by trip_distance desc


select DATE_TRUNC('day', lpep_pickup_datetime), max (trip_distance) from green_tripdata_202511
where 
 trip_distance<100
group by 1
order by 2 desc
*/

--Q5
/*
select  b."Zone", count(*), sum(total_amount)
from green_tripdata_202511 as a
join public.taxi_zone_lookup as b on a."PULocationID"=b."LocationID"
where a.lpep_pickup_datetime >= '2025-11-18'  
and  a.lpep_pickup_datetime < '2025-11-19'
group by b."Zone"
order by 3 desc
*/
--order by lpep_pickup_datetime desc
--select * from public.taxi_zone_lookup order by "Zone" 

--Q6
/*
select b."Zone" as pu_zone, c."Zone" as do_zone, *
from green_tripdata_202511 as a
join public.taxi_zone_lookup as b on a."PULocationID"=b."LocationID"
join public.taxi_zone_lookup as c on a."DOLocationID"=c."LocationID"
where a.lpep_pickup_datetime >= '2025-11-01'  
and  a.lpep_pickup_datetime < '2025-12-01'
and a."PULocationID"=74
order by a.tip_amount desc
*/



