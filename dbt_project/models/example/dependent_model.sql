SELECT * 
FROM {{ ref('my_model') }}
WHERE user_rating > 4.5
ORDER BY user_rating DESC