#!/bin/sh

rm -rf redis-stable/
wget http://download.redis.io/releases/redis-stable.tar.gz
tar xzf redis-stable.tar.gz
rm redis-stable.tar.gz
cd redis-stable/
make
cd utils/create-cluster/
awk '{sub(/NODES=6/,"NODES=12"); print}' create-cluster > create-cluster.tmp
mv create-cluster.tmp create-cluster
chmod 700 create-cluster
./create-cluster start
./create-cluster create
# ./create-cluster stop
# ./create-cluster clean
