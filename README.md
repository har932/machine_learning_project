# machine_learning_project
First Project

Creating conda environment
```
conda create -p venv python==3.7 -y
```

```
conda activate venv/
```

```
pip install -r requirements.txt
```

To add files to git
```
git add .
```

```
fit add <file_name>
```

Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```

To check all the version maintain by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
``` 

To send changes/version to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we nee 3 information

1. HEROKU_EMAIL = seenivasanharish786@gmil.com
2. HEROKU_API_KEY = 26adcc83-6f84-4c98-a644-83cbd2893780 
3. HERKO_APP_NAME = ml-regressio

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

To run docker image
```
docker run -p 5000:5000 -e PORT=5000 5be2fda018d1
```

To check running container in docker
```
docker ps
``` 

To stop docker container
```
docker stop <container_id>
```

```
python setup.py install
```