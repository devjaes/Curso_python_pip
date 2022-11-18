import csv


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


def get_country_data(data_of_csv, country):
    country_data = {}

    for countries in data_of_csv:
        # print(countries["Country"])
        # print(type(countries['Country']))
        #country_data = data_of_csv[0]
        if countries["Country"] == country:
            country_data = countries

    return country_data


def read_population_by_years(country_data):
    population_dict = {}
    for data, value in country_data.items():

        if 'Population' in data:
            if 'Worl' in data:
                continue

            population_dict[data[:4]] = value

    return population_dict


def get_world_percentages(data):
    percentages_dict = {
        item['Country']: item['World Population Percentage'] for item in data}
    labels = percentages_dict.keys()
    values = percentages_dict.values()

    return labels, values


if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    country_data = get_country_data(data, 'Brazil')
#    print(country_data)
    print(read_population_by_years(country_data))
