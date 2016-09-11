-- Question 1
SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

-- Question 2
SELECT COUNT(cities.id)AS count, countries.name
FROM cities
LEFT JOIN countries
ON cities.country_id = countries.id
GROUP BY countries.name
ORDER BY COUNT(cities.id) DESC;

-- Question 3
SELECT cities.name, cities.population
FROM  cities
LEFT JOIN countries
ON cities.country_id = countries.id
WHERE countries.name = 'Mexico'AND cities.population > 500000
ORDER BY  cities.population DESC;

-- Question 4
SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

-- Question 5
SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;

-- Question 6
SELECT countries.name, countries.capital, countries.life_expectancy
FROM countries
LEFT JOIN cities
ON countries.capital = cities.id
WHERE countries.government_form = 'Constitutional Monarchy' AND cities.population > 200 AND countries.life_expectancy > 75; 

-- Question 7
SELECT cities.district, cities.name, cities.population, countries.name
FROM cities
LEFT JOIN countries
ON countries.id = cities.country_id
WHERE cities.population > 500000 AND countries.name = 'Argentina' AND cities.district = 'Buenos Aires';

-- Question 8
SELECT COUNT(countries.id) AS count, countries.region
FROM countries
GROUP BY countries.region
ORDER BY COUNT(countries.id) DESC;