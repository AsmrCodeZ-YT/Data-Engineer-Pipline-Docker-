# create network dataline
    docker create network dataline
# run producer
generate data and insert into redis


# Run redis
    docker run -d --rm  --name redis -p 6379:6379 --hostname redis --network dataline redis

# run consumer
feed from redis 

# run postgres
    docker run -d --rm --name postgres --hostname postgres --network dataline -p 54321:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=ecommerce_docker postgres -c wal_level=logical
