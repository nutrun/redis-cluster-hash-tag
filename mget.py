from rediscluster import RedisCluster
import csv

# Use a hash tag to ensure keys of the same country are stored in the same slot
def key(country, city):
    return "{%s}_%s" % (country, city)

def main():
    startup_nodes = [{"host": "0.0.0.0", "port": "30001"}]
    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    germany = []

    # Collect all Germany city keys
    with open('worldcities.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            country = row['country'].replace(' ', '-')
            city = row['city_ascii'].replace(' ', '-')
            population = row['population']

            if country == "Germany":
                germany.append(key(country, city))

    # Fetch all of Germany's cities' populations with one MGET command
    slot = rc.connection_pool.nodes.keyslot(germany[0])
    node = rc.connection_pool.get_master_node_by_slot(slot)
    connection = rc.connection_pool.get_connection_by_node(node)
    connection.send_command('MGET '+' '.join(germany))
    response = rc.parse_response(connection, 'MGET')
    population = sum([int(p) for p in response if p])
    print("Population: %d" % population)

if __name__ == '__main__':
    main()
