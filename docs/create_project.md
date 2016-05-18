## Create project ##

Before create your project please install cookiecutter
```sh
pip install cookiecutter
```

With cookiecutter installed make your project
```sh
$ cookiecutter https://github.com/luizalabs/tornado-cookiecutter.git
Cloning into 'tornado-cookiecutter'...
remote: Counting objects: 467, done.
remote: Compressing objects: 100% (214/214), done.
remote: Total 467 (delta 192), reused 467 (delta 192), pack-reused 0
Receiving objects: 100% (467/467), 53.39 KiB | 0 bytes/s, done.
Resolving deltas: 100% (192/192), done.
Checking connectivity... done.
project_name []:
project_slug []: # this field is not required, because it is generate based at a project_name
short_description []:
description []: # short description to your project
version [0.1.0]:
author []:
repo []:
travis_url [luizalabs/]:
```
