```
git clone https://github.com/koopichi/TamashakhoonehBot.git && cd Tamashakhooneh
```

```
docker build -t tamashakhooneh .
```

```
docker network create my_network
```

```
docker run -d --name mongodb \
  --network my_network \
  -e MONGO_INITDB_ROOT_USERNAME=USERNAME \
  -e MONGO_INITDB_ROOT_PASSWORD=PASSWORD \
  -p 27017:27017 \
  -v /root/mongo:/data/db \
  mongo
```

enter your .env

```
docker run -d --restart unless-stopped --name tamasha \
  --network my_network \
  -v /root/env/.env:/app/.env \
  -p 8080:8080 \
  tamashakhooneh
```
