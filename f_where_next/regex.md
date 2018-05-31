# example 1
select
a$phone
a$car
a$postal_code
a$phone_number
b$cover_life
b$cover_disability
b$cover_health
from
client_info as a inner join policy_info as b on a.guid=b.guid
where a.city='panama' and b.premium>1e3

# example 2
some vba code to refactor to python
	from web or eoe

# methods
	- simple substitution
	- batch substitution
	- code formating
