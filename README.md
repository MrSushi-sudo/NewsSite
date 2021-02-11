Build the project:
Start the Docker container using the up command, adding the -d flag so it runs in detached mode, and the --build flag to build our initial image. If we did not add this flag, we'd need to open a separate command line tab to execute commands.

1)docker-compose up -d --build

Restoring the data into Docker container

2)docker exec -i newssite_db pg_restore --verbose --clean --no-acl --no-owner -h localhost -U postgres -d NewsSite < ./NewsSite.sql

http://127.0.0.1:8000/admin/ - admin page (login-pass: "admin")
http://127.0.0.1:8000/news/ - home page
http://127.0.0.1:8000/news/id/ - specific news page

Create News:
1) Click "Нажми здесь" in sidebar
2) Date Published format: dd.mm.yyyy hh:mm:ss
2) Fill in the fields and Click "Создать" button

Paging with adjustable
the number of news per page: 10, 20 and 50, located at the bottom of the page.

If you need to return to the home page, click the "Новости" button in the navbar

You can run the tests with the command: python manage.py test