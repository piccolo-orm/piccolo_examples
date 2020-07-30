# headless blog

An example headless blog, built with FastAPI and Piccolo.

![Admin](_images/admin.png?raw=true "Admin")
![FastAPI](_images/fastapi.png?raw=true "FastAPI")

## Trying it out

Install requirements:

```
pip install -r requirements.txt
```

Make sure a Postgres database exists with the name `piccolo_headless_blog` (see piccolo_conf.py for the connection details).

Run the migrations:

```
piccolo migrations forwards all
```

Create an admin user:

```
piccolo user create
```

Start the web server:

```
python main.py
```

Now you have a headless blog!

 * To create some posts: [localhost:8000/admin/](http://localhost:8000/admin/)
 * To see the API docs: [localhost:8000/docs/](http://localhost:8000/docs/)
