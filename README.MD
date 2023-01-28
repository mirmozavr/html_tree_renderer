# Tree Renderer

Django app to render tree menues

### HOWTO

- Fastest method: execute `runserver.sh` script to create db, populate it with admin user (password: **`admin`**) and
  a couple example tree menus and launch a server at default `127.0.0.1:8000`. Tested on linux OS,
  `python3` command is used
- Manual method:  execute followed commands. Use `python` or `python3` depending on your OS.

> 1. `python3 manage.py makemigrations`
> 1. `python3 manage.py migrate`
> 1. `python3 manage.py loaddata admin.json`
> 1. `python3 manage.py loaddata tree.json`
> 1. `python3 manage.py runserver`  


### Description
All available menus are listed on home page
![image](https://user-images.githubusercontent.com/68658828/215261413-57b50adc-5b18-40b6-bf10-50bbe73fbde8.png)

Example 1  
![image](https://user-images.githubusercontent.com/68658828/215261523-7f50ea87-6f39-4858-9f7b-72083698b4bd.png)

Example 2  
![image](https://user-images.githubusercontent.com/68658828/215261599-36788fb3-c234-4c76-98d2-b6f14227782b.png)
