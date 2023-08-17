# Getting started

This repository is a sample application for users following the getting started guide at https://docs.docker.com/get-started/.

The application is based on the application from the getting started tutorial at https://github.com/docker/getting-started


Build 
```bash
docker build -t getting-started .
```

Run without persisted data
```bash
docker run -dp 127.0.0.1:3000:3000 getting-started
```

Run with persisted data
```bash
docker run -dp 127.0.0.1:3000:3000 --mount type=volume,src=todo-db,target=/etc/todos getting-started
```

## Version with mysql.
Create a network and run database
```bash
docker network create todo-app
docker run -d \
     --network todo-app --network-alias mysql \
     -v todo-mysql-data:/var/lib/mysql \
     -e MYSQL_ROOT_PASSWORD=secret \
     -e MYSQL_DATABASE=todos \
     mysql:8.0
```

Run application and connect to mysql
```bash
docker run -dp 127.0.0.1:3000:3000 \
   -w /app -v "$(pwd):/app" \
   --network todo-app \
   -e MYSQL_HOST=mysql \
   -e MYSQL_USER=root \
   -e MYSQL_PASSWORD=secret \
   -e MYSQL_DB=todos \
   node:18-alpine \
   sh -c "yarn install && yarn run dev"
   ```

## End up with compose

Use compose.yaml to get all up and running
Start the application stack
```bash
docker compose up -d
```

Stop the application stack
```bash
docker compose down
```

Check logs
```bash
docker compose logs -f
```