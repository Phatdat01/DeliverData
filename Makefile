include .env

build:
	docker-compose build

up:
	docker-compose --env-file .env up -d

down:
	docker-compose --env-file .env down

to_mysql:
	docker exec -it mysql mysql --local-infile=1 -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" brazillian_ecommerce

to_mysql_root:
	docker exec -it mysql mysql -u"root" -p"${MYSQL_ROOT_PASSWORD}"

to_mongo_root:
	docker exec -it mongodb mongosh -u "${MONGO_INITDB_ROOT_USERNAME}" -p "${MONGO_INITDB_ROOT_PASSWORD}"