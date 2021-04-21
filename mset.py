from rediscluster import RedisCluster
import csv

def key(country, city):
    return "%s_%s" % (country, city)

def main():
    startup_nodes = [{"host": "0.0.0.0", "port": "30001"}]
    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    country_city_populations = {}

    with open('worldcities.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            country = row['country']
            city = row['city_ascii']
            population = row['population']

            if population == '':
                population = 0

            if country not in country_city_populations:
                country_city_populations[country] = {}

            k = key(country, city)
            country_city_populations[country][k] = population

        for populations in country_city_populations.values():
            rc.mset(populations)

if __name__ == '__main__':
    main()
