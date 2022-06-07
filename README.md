#### Usage

Documentation for API calls can be found [here](https://app.swaggerhub.com/apis/RobJun/amcef/1.0.0#/).

Required python version is 3.10

###### Installation

First create ```config.json``` file which contains:

```json
{
    "secret" : "<secret key>"
}
```
###### Manual install

Start virtual environment:

```shell
python -m venv <env-name>
```

Activate environment

Windows:

```powershell
./<env-name>/Scripts/Activate
```

Linux:

```shell
source <env-name>/bin/activate
```

next install dependencies:

```shell
pip install -r requirements.txt
```

and you are good to go. Just startup django server with command:

```shell
python manage.py runserver 0.0.0.0:8000
```

###### Using Docker

If you are using docker all you need to do while in project directory run command:

```shell
#must be inside directory of the project
docker-compose up
```
