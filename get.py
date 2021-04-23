from rediscluster import RedisCluster
import csv

def key(country, city):
    return "%s_%s" % (country, city)

def main():
    startup_nodes = [{"host": "0.0.0.0", "port": "30001"}]
    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    germany_population = 0

    with open('worldcities.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            country = row['country'].replace(' ', '-')
            if country == 'Germany':
                city = row['city_ascii'].replace(' ', '-')
                population = rc.get(key(country, city))
                if population:
                    germany_population += int(population)

    print("Population: %d" % germany_population)

if __name__ == '__main__':
    main()
