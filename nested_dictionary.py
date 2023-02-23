countries = {
    'Ukraine' : {'capital' : 'Kyiv', 'population' : '111'},
    'USA' : {'capital' : 'Washington', 'population' : '222'},
    'Great Britain' : {'capital' : 'London', 'population' : '333'}
}

countries['France'] = {}

countries['France']['capital'] = 'Paris'
countries['France']['population'] = '444'

for country, data in countries.items():

    print(f"country: {country} capital: {data['capital']} population: {data['population']}")