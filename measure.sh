#!/bin/sh

HERE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Clear redis stats
for PORT in 30001 30002 30003 30004 30005 30006
do
    echo CONFIG RESETSTAT | $HERE/redis-stable/src/redis-cli -p $PORT
done

time python $1

# Print Redis total_commands_processed stat
for PORT in 30001 30002 30003 30004 30005 30006
do
    echo INFO stats | $HERE/redis-stable/src/redis-cli -p $PORT | grep total_commands_processed | cut -d : -f 2
done
