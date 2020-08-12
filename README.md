# Example of Prometheus with Airflow


## Build

```bash
docker-compose build
```


## Run

```bash
docker-compose up
```


## Working with services


### Open Airflow UI

```
http://localhost:8080
```


### StatsD exporter

Here you can overview metrics which statsd collects from Airflow.

```
http://localhost:9123/metrics
```

All Airflow metrics description: https://airflow.apache.org/docs/stable/metrics.html



### Prometheus UI

```
http://localhost:9090
```


### Grafana

Enter UI: ```http://localhost:3000```

Loging: `admin`

Password: `password`

![](images/g1.png)


### Connenct to Prometheus

![](images/g2.png)

1. go to `Configuration` -> `Datasources`;
![](images/g3.png)
2. click `Add data source`;
![](images/g4.png)
3. select `Prometheus`;
4. add `URL` = `http://prometheus:9090`;
![](images/g5.png)
5. click `Save and test`.
![](images/g6.png)


### Go to dashboard

Go to `Explore`.

![](images/g7.png)

Select airlfow metric.

![](images/g8.png)

