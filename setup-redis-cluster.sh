#!/bin/sh

rm -rf redis-6.2.2/
wget http://download.redis.io/releases/redis-6.2.2.tar.gz
tar xzf redis-6.2.2.tar.gz
rm redis-6.2.2.tar.gz
cd redis-6.2.2/
make
cd utils/create-cluster/
awk '{sub(/NODES=6/,"NODES=12"); print}' create-cluster > create-cluster.tmp
mv create-cluster.tmp create-cluster
chmod 700 create-cluster
./create-cluster start
./create-cluster create
# ./create-cluster stop
# ./create-cluster clean
