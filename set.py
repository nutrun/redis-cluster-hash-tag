from rediscluster import RedisCluster
import csv

def key(country, city):
    return "%s_%s" % (country, city)

def main():
    startup_nodes = [{"host": "0.0.0.0", "port": "30001"}]
    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

    with open('worldcities.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            country = row['country'].replace(' ', '-')
            city = row['city_ascii'].replace(' ', '-')
            population = row['population']

            if population == '':
                population = 0

            rc.set(key(country, city), population)

if __name__ == '__main__':
    main()
