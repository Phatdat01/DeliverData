# 1. Vấn đề đặt ra
Khách hàng muốn một pipeline xử lý MongoDB sang MySQL. Trong đó làm sao phải xử lý nhận biết được sự thay đổi trong DB ban đầu để tiến hành các thay đổi trong target.
Yêu cầu đặt ra là công nghệ có ứng dụng xử lý realtime.
# 2. Các công nghệ sử dụng
* MongoDB
* MySQL
* Kafka
*
# 3. Download Mongodb
```
https://hub.docker.com/_/mongo
https://geshan.com.np/blog/2023/03/mongodb-docker-compose/

docker run -d --name mongodb -p 27017:27017 mongo 
```

# 4. MySQL
```
https://hub.docker.com/_/mysql

docker exec -it my-sql /bin/bash
```