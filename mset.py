from rediscluster import RedisCluster
import csv

# Use a hash tag to ensure keys of the same country are stored in the same slot
def key(country, city):
    return "{%s}_%s" % (country, city)

def main():
    startup_nodes = [{"host": "0.0.0.0", "port": "30001"}]
    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    slots = {}

    with open('worldcities.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        # Group keys by slot
        for row in reader:
            country = row['country'].replace(' ', '-')
            city = row['city_ascii'].replace(' ', '-')
            population = row['population']

            k = key(country, city)
            slot = rc.connection_pool.nodes.keyslot(k)

            if slot not in slots:
                slots[slot] = []

            slots[slot].append("%s %s" % (k, population))

    # Issue one MSET command for all of a country's populations
    for slot, populations in slots.items():
        node = rc.connection_pool.get_master_node_by_slot(slot)
        connection = rc.connection_pool.get_connection_by_node(node)
        connection.send_command('MSET '+' '.join(populations))

if __name__ == '__main__':
    main()
