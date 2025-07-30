
  create view "destination_db"."public"."my_model__dbt_tmp"
    
    
  as (
    -- models/example/thriller_films.sql

WITH thriller_films AS (
    SELECT f.film_id, f.title, f.release_date, f.user_rating
    FROM "destination_db"."public"."films" f
    JOIN "destination_db"."public"."film_category" fc ON f.film_id = fc.film_id
    WHERE fc.category_name = 'Thriller'
),
thriller_with_actors AS (
    SELECT tf.film_id, tf.title, a.actor_name, tf.user_rating
    FROM thriller_films tf
    JOIN "destination_db"."public"."film_actors" fa ON tf.film_id = fa.film_id
    JOIN actors a ON fa.actor_id = a.actor_id
)

SELECT * FROM thriller_with_actors
  );