import csv

customers = open('customers.csv','r')
customer_file = csv.reader(customers, delimiter = ',')

next(customer_file)

countries = open('customer_country.csv', 'w', newline = '')
country_file = csv.writer(countries, delimiter = ',')

country_file.writerow(['First Name', 'Last Name', 'Country'])

customer_count = 0

for customer in customer_file:
    first_name = customer[1]
    last_name = customer[2]
    country = customer[4]

    country_list = [first_name, last_name, country]
    country_file.writerow(country_list)

    customer_count += 1

print(customer_count)

customers.close()
countries.close()
