# Optimise Redis cluster mutli-key commands with hash tags

## Python dependencies
[redis-py-cluster](https://redis-py-cluster.readthedocs.io/en/master/)

## Redis cluster setup

Setup a twelve node (six master / six slave) Redis cluster

```
./setup-redis-cluster.sh
```

## Running the benchmarks

Measure the number of commands issued and crude execution time when inserting keys with `SET` commands

```
./measure.sh set.py
```

Measure the number of commands issued and crude execution time when inserting keys using hash tags and `MSET` commands

```
./measure.sh mset.py
```

Measure the number of commands issued and crude execution time when calculating Germany's population by fetching its cities' populations using `GET` commands

```
./measure.sh get.py
```

Measure the number of commands issued and crude execution time when calculating Germany's population by fetching its cities' populations using hash tags and one `MGET` command

```
./measure.sh mget.py
```

## Links

`worldcities.csv` data from the [World Cities Database](https://simplemaps.com/data/world-cities)
