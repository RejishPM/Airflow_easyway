
  create view "destination_db"."public"."dependent_model__dbt_tmp"
    
    
  as (
    SELECT * 
FROM "destination_db"."public"."my_model"
WHERE user_rating > 4.5
ORDER BY user_rating DESC
  );