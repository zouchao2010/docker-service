# docker-service


## build
```shell
docker build -t zouchao2010/docker-service .

```
  
## run(创建并运行一个容器，退出时删除容器)
```shell
docker run  --name docker-service \
            -h docker-service \
            -v /data/docker-service_data:/var/lib/docker-service \
            -it --rm zouchao2010/docker-service
            
```
  
## run(创建并运行一个容器，以守护进程方式)
```shell
docker run  --name docker-service \
            -h docker-service \
            -v /data/docker-service_data:/var/lib/docker-service \
            -dt zouchao2010/docker-service
            
```

## start|stop|restart(已存在的容器)
```shell
docker start|stop|restart docker-service

```

## exec(使用已运行的容器执行命令)
```shell
docker exec -it docker-service /bin/bash
