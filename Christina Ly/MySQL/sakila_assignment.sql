-- QUESTION 1
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
LEFT JOIN address
ON customer.address_id = address.address_id
LEFT JOIN city
ON city.city_id = address.city_id
WHERE city.city_id = 312;

-- QUESTION 2
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
LEFT JOIN film_category
ON film_category.film_id = film.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

-- QUESTION 3
SELECT film.title, film.description, film.release_year
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

-- QUESTION 4
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
LEFT JOIN store
ON store.store_id = customer.store_id
LEFT JOIN address
ON address.address_id = customer.address_id
LEFT JOIN city
ON city.city_id = address.city_id
WHERE (city.city_id = 1 OR city.city_id = 42 OR city.city_id = 312 OR city.city_id = 459) AND store.store_id = 1;

-- QUESTION 5
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE film.rating = 'G' AND actor.actor_id = 15 AND film.special_features LIKE "%behind%";

-- QUESTION 6
SELECT film.film_id AS film_id, film.title AS title, actor.actor_id AS actor_id, CONCAT(actor.first_name,' ', actor.last_name) AS actor_name
FROM actor
LEFT JOIN film_actor
ON actor.actor_id = film_actor.actor_id
LEFT JOIN film
ON film.film_id = film_actor.film_id
WHERE film.film_id = 369;

-- QUESTION 7
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, rental_rate
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99 AND category.name = 'drama';

-- QUESTION 8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
RIGHT JOIN film_actor
ON film_actor.film_id = film.film_id
RIGHT JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER' AND category.name = 'action';