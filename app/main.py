import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('./data.csv')
    country = input('Type country => ')

    result = utils.population_by_country(data, country)
    if len(result) > 0:
        name_country = country
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(name_country, labels, values)
    labels, values = read_csv.get_world_percentages(data)

    #charts.generate_pie_chart(name_country, labels, values)


if __name__ == '__main__':
    run()
