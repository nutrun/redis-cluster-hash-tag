#!/bin/sh

wget http://download.redis.io/releases/redis-6.2.2.tar.gz
tar xzf redis-6.2.2.tar.gz
rm redis-6.2.2.tar.gz
cd redis-6.2.2/
make
gsed -i 's/NODES=6/NODES=12/g' utils/create-cluster/create-cluster
cd utils/create-cluster/
./create-cluster start
./create-cluster stop
cd ../..
