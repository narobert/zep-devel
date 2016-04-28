#! /bin/bash

# kill all daemons
supervisorctl stop all

# stop nginx server
sudo service nginx stop

# Pause script for ten seconds
sleep 1

# start nginx server
sudo service nginx start

# start all daemons
supervisorctl start all