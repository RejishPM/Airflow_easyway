-- models/example/thriller_films.sql

WITH thriller_films AS (
    SELECT f.film_id, f.title, f.release_date, f.user_rating
    FROM {{ source('public', 'films') }} f
    JOIN {{ source('public', 'film_category') }} fc ON f.film_id = fc.film_id
    WHERE fc.category_name = 'Thriller'
),
thriller_with_actors AS (
    SELECT tf.film_id, tf.title, a.actor_name, tf.user_rating
    FROM thriller_films tf
    JOIN {{ source('public', 'film_actors') }} fa ON tf.film_id = fa.film_id
    JOIN actors a ON fa.actor_id = a.actor_id
)

SELECT * FROM thriller_with_actors
