# Testing, CI/CD

[Configuring Admin interface](airline0/flights/admin.py)

[Loading static files](airline0/flights/templates/flights/base.html)

[Basic test](tests0.py)

[Assertion](assert1.py)

[Unit test](tests1.py)

Django has its own testing framework.

[Flights tests](airline1/flights/tests.py)

Django creates a separate database test for running tests. To run the tests, we use `python manage.py test`

[Testing web client](airline2/flights/tests.py)

[Testing Javascript on Browser](selenium/tests.py)

When a new push has been made to github. Github notifies Travis, Travis pulls the code and runs tests and informs the results to Github. We need to configure Travis and for that YAML file is used.

```yaml
language: python
python:
  - 3.6
install:
  - pip install -r requirements.txt
script:
  - python manage.py test
```

[Travis Yaml File](airline3/.travis.yml)

To use Travis, link your github account to [Travis](https://travis-ci.org)

To manage environment for web application, we can have containers running a web server. We can compose two containers to run database server and web server. An example, [docker compose file](airline4/docker-compose.yml) shows this. We can manage dependencies using [requirements file](airline4/requirements.txt). The docker container will be created based on [Dockerfile](airline4/Dockerfile). This project includes database as postgres which can be seen in [settings file](airline4/airline/settings.py)


To start up, application, we use `docker-compose up`.

```shell
docker ps # to see running containers
docker exec -it <container_id> bash -l # to enter bash of a particular container
```