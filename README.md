This is an example of a python client application using the MigratoryData Client API for Python.

The latest build of the API can be downloaded from [here](https://migratorydata.com/downloads/migratorydata-6/).

The API documentation can be found [here](https://migratorydata.com/docs/client-api/python/).

### REQUIREMENTS

1. Python version 3.0.1 or more recent

2. MigratoryData Server version 6.0 or more recent 

### How To Run

The client application connects to the MigratoryData server deployed at `localhost:8800` and publishes a message every second on the subject `/server/status`.

If you don't have a MigratoryData server installed on your machine but there is docker installed you can run the following command to start MigratoryData server, otherwise you can download and install the latest version for your os from [here](https://migratorydata.com/downloads/migratorydata-6/).

```sh
docker pull migratorydata/server:latest
docker run -d --name my_migratorydata -p 8800:8800 migratorydata/server:latest
```

Next, run the application using command:

```sh
python sample
```
