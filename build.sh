bash ./bump_version.sh
sleep 1

ver=`cat version`
docker build -t tomkat/serialsDocs:$ver .