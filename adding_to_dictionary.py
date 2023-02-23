def city_country(capital, country, populatin):
    full_list[country] = {}
    full_list[country]['city'] = capital
    full_list[country]['population'] = population
    print(full_list)
full_list = {}
while True:
    print('To exit print "q" ')
    capital = input('Enter capital: ')
    if capital == 'q':
        break
    country = input('Enter country: ')
    population = input('Enter population: ')
    city_country(capital, country, population) 
