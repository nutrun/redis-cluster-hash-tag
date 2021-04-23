# Optimise Redis cluster mutli key commands with hash tags

Setup a twelve (six master / six slave) node Redis cluster

```
./setup-redis-cluster.sh
```

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

Measure the number of commands issued and crude execution time when calculating Germany's population by fetching its cities' using hash tags and one `MGET` command

```
./measure.sh mget.py
```

`worldcities.csv` data from the [World Cities Database](https://simplemaps.com/data/world-cities)
