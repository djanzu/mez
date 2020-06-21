```
<(╹ヮ╹)>anzu@anzuAir ~/develop/mez $ mkvirtualenv mez --python=python3
Running virtualenv with interpreter /usr/local/bin/python3

(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez $ pip install mezzanine
Collecting mezzanine
  Downloading Mezzanine-4.3.1-py2.py3-none-any.whl (5.9 MB)
     |████████████████████████████████| 5.9 MB 7.7 MB/s 
     
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez $ pip freeze | sort > requirements.txt
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez $ mezzanine-project sample
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez $ cd sample/
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez/sample $ python manage.py startapp theme
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez/sample $ python manage.py createdb
Operations to perform:
  Apply all migrations: admin, auth, blog, conf, contenttypes, core, django_comments, forms, galleries, generic, pages, redirects, sessions, sites, twitter
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sites.0001_initial... OK
  Applying blog.0001_initial... OK
  Applying blog.0002_auto_20150527_1555... OK
  Applying blog.0003_auto_20170411_0504... OK
  Applying conf.0001_initial... OK
  Applying core.0001_initial... OK
  Applying core.0002_auto_20150414_2140... OK
  Applying django_comments.0001_initial... OK
  Applying django_comments.0002_update_user_email_field_length... OK
  Applying django_comments.0003_add_submit_date_index... OK
  Applying pages.0001_initial... OK
  Applying forms.0001_initial... OK
  Applying forms.0002_auto_20141227_0224... OK
  Applying forms.0003_emailfield... OK
  Applying forms.0004_auto_20150517_0510... OK
  Applying forms.0005_auto_20151026_1600... OK
  Applying forms.0006_auto_20170425_2225... OK
  Applying galleries.0001_initial... OK
  Applying galleries.0002_auto_20141227_0224... OK
  Applying generic.0001_initial... OK
  Applying generic.0002_auto_20141227_0224... OK
  Applying generic.0003_auto_20170411_0504... OK
  Applying pages.0002_auto_20141227_0224... OK
  Applying pages.0003_auto_20150527_1555... OK
  Applying pages.0004_auto_20170411_0504... OK
  Applying redirects.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying sites.0002_alter_domain_unique... OK
  Applying twitter.0001_initial... OK

A site record is required.
Please enter the domain and optional port in the format 'domain:port'.
For example 'localhost:8000' or 'www.example.com'. 
Hit enter to use the default (127.0.0.1:8000): 

Creating default site record: 127.0.0.1:8000 ...


Creating default account ...

Username (leave blank to use 'anzu'): 
Email address: anzu@*************
Password: 
Password (again): 
Superuser created successfully.
Traceback (most recent call last):
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/db/backends/utils.py", line 62, in execute
    return self.cursor.execute(sql)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/db/backends/sqlite3/base.py", line 326, in execute
    return Database.Cursor.execute(self, query)
sqlite3.OperationalError: no such table: django_site__old

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 14, in <module>
    execute_from_command_line(sys.argv)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/core/management/__init__.py", line 364, in execute_from_command_line
    utility.execute()
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/core/management/__init__.py", line 356, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/core/management/base.py", line 283, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/core/management/base.py", line 330, in execute
    output = self.handle(*args, **options)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/mezzanine/core/management/commands/createdb.py", line 61, in handle
    func()
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/mezzanine/core/management/commands/createdb.py", line 109, in create_pages
    call_command("loaddata", "mezzanine_required.json")
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/core/management/__init__.py", line 131, in call_command
    return command.execute(*args, **defaults)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/core/management/base.py", line 330, in execute
    output = self.handle(*args, **options)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/core/management/commands/loaddata.py", line 69, in handle
    self.loaddata(fixture_labels)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/core/management/commands/loaddata.py", line 115, in loaddata
    connection.check_constraints(table_names=table_names)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/db/backends/sqlite3/base.py", line 286, in check_constraints
    column_name, referenced_column_name,
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/db/backends/utils.py", line 79, in execute
    return super(CursorDebugWrapper, self).execute(sql, params)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/db/utils.py", line 94, in __exit__
    six.reraise(dj_exc_type, dj_exc_value, traceback)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/utils/six.py", line 685, in reraise
    raise value.with_traceback(tb)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/db/backends/utils.py", line 62, in execute
    return self.cursor.execute(sql)
  File "/Users/anzu/.virtualenvs/mez/lib/python3.7/site-packages/django/db/backends/sqlite3/base.py", line 326, in execute
    return Database.Cursor.execute(self, query)
django.db.utils.OperationalError: Problem installing fixtures: no such table: django_site__old
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez/sample $ ls
deploy			dev.db			fabfile.py		manage.py		requirements.txt	sample			theme
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez/sample $ ls sample/
__init__.py		__pycache__		local_settings.py	settings.py		urls.py			wsgi.py
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez/sample $ cd sample/
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez/sample/sample $ emacs -nw local_settings.py settings.py 
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez/sample/sample $ cd ..
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez/sample $ python manage.py createdb
CommandError: Database already created, you probably want the migrate command
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez/sample $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, conf, contenttypes, core, django_comments, forms, galleries, generic, pages, redirects, sessions, sites, twitter
Running migrations:
  No migrations to apply.
(mez) <(╹ヮ╹)>anzu@anzuAir ~/develop/mez/sample $ python manage.py runserver
              .....
          _d^^^^^^^^^b_
       .d''           ``b.
     .p'                `q.
    .d'                   `b.
   .d'                     `b.   * Mezzanine 4.3.1
   ::                       ::   * Django 1.11.29
  ::    M E Z Z A N I N E    ::  * Python 3.7.7
   ::                       ::   * SQLite 3.32.1
   `p.                     .q'   * Darwin 17.7.0
    `p.                   .q'
     `b.                 .d'
       `q..          ..p'
          ^q........p^
              ''''

Performing system checks...

System check identified no issues (0 silenced).
June 21, 2020 - 08:58:58
Django version 1.11.29, using settings 'sample.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

https://qiita.com/kotayanagi/items/79194e6e7ee4743f1ed4

の写経。
createdbの途中でエラーが出たけど、普通に起動してしまった。  
なんだろう。
