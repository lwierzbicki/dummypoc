Example app from https://stackify.com/docker-build-a-beginners-guide-to-building-docker-images/

Build and run
```bash
docker build . -t v13rsba/example-node-app
docker images
docker run -d -p80:3000 v13rsba/example-node-app
```

Diagnose 
```bash
docker ps
docker inspect [container_id]
docker logs [container_id]
docker stop [container_id]
```