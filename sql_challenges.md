List all actors.
    select first_name, last_name from actor;
Find the surname of the actor with the forename 'John'.
    select last_name from actor where first_name='John';
Find all actors with surname 'Neeson'.
    select first_name, last_name from actor where last_name = 'Neeson';
Find all actors with ID numbers divisible by 10.
    select actor_id, first_name, last_name from actor where actor_id%10=0;
What is the description of the movie with an ID of 100?
Find every R-rated movie.
Find every non-R-rated movie.
Find the ten shortest movies.
Find the movies with the longest runtime, without using LIMIT.
Find all movies that have deleted scenes.
Using HAVING, reverse-alphabetically list the last names that are not repeated.
Using HAVING, list the last names that appear more than once, from highest to lowest frequency.
Which actor has appeared in the most films?
When is 'Academy Dinosaur' due?
What is the average runtime of all films?
List the average runtime for every film category.
List all movies featuring a robot.
How many movies were released in 2010?
Find the titles of all the horror movies.
List the full name of the staff member with the ID of 2.
List all the movies that Fred Costner has appeared in.
How many distinct countries are there?
List the name of every language in reverse-alphabetical order.
List the full names of every actor whose surname ends with '-son' in alphabetical order by their forename.
Which category contains the most films?



Using COUNT, get the number of cities in the USA.
    SELECT COUNT(Name) FROM city where CountryCode = 'USA';
Find out the population and life expectancy for people in Argentina.
    select Population, LifeExpectancy from country WHERE Name='Argentina'
Using IS NOT NULL, ORDER BY, and LIMIT, which country has the highest life expectancy?
    SELECT Name, LifeExpectancy FROM country WHERE LifeExpectancy IS NOT NULL ORDER BY LifeExpectancy DESC LIMIT 1;
Using JOIN ... ON, find the capital city of Spain.
    SELECT country.Name, country.Capital, city.Name, city.ID FROM city JOIN Country ON city.ID=country.Capital WHERE Country.Name='Spain';
Using JOIN ... ON, list all the languages spoken in the Southeast Asia region.
    SELECT cl.language FROM countrylanguage cl LEFT JOIN country c ON cl.CountryCode=c.Code WHERE c.Region='Southeast Asia';
Using a single query, list 25 cities around the world that start with the letter F.
    SELECT Name FROM city WHERE Name LIKE 'F%' LIMIT 25;
Using COUNT and JOIN ... ON, get the number of cities in China.
    
Using IS NOT NULL, ORDER BY, and LIMIT, which country has the lowest population? Discard non-zero populations.
Using aggregate functions, return the number of countries the database contains.
What are the top ten largest countries by area?
List the five largest cities by population in Japan.
List the names and country codes of every country with Elizabeth II as its Head of State. You will need to fix the mistake first!
List the top ten countries with the smallest population-to-area ratio. Discard any countries with a ratio of 0.
List every unique world language.
List the names and GNP of the world's top 10 richest countries.
List the names of, and number of languages spoken by, the top ten most multilingual countries.
List every country where over 50% of its population can speak German.
Which country has the worst life expectancy? Discard zero or null values.
List the top three most common government forms.
How many countries have gained independence since records began?