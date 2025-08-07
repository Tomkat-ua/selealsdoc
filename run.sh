ver=`cat version`
service=UkrSklad_Addons
container=$service
img=tomkat/ukrsklad_addons:$ver

docker container stop $container
docker container rm $container

docker run -dt \
    -e PAGE_ROWS=8 \
    -e DB_HOST=192.168.10.5 \
    -e DB_PATH=sklad_prod \
    -e SERVER_PORT=5000 \
    -e APP_VERSION=$ver \
    -p 8084:5000 \
    --name=$container \
    -e TZ=Europe/Kyiv \
    --restart=always \
    $img