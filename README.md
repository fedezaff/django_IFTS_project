## Documetation

### Project Description: WebApp for Training and Decent Work

**Objective:**
>Our project aligns with the 2030 Agenda, specifically with Goal 8, which promotes decent work and training. The main objective is to create an innovative web app that combines features of Wikipedia and LinkedIn, facilitating the connection between companies and job candidates.

**Project Description:**
>The web app will allow companies to post job descriptions and the necessary qualifications for open positions. Each requirement will be linked to online training resources, enabling users to easily access courses and materials needed to develop the required skills.

**Self Hosting procedure:**

1. Make sure to have these already set up For the SysAdmin part:
    - Get docker Installed
2. Create an Ubuntu Container:
    - Create an ubuntu container and then enter inside with

```
     | docker exec -it “id_container” /bin/bash | make a folder and clone the git repo of NextStep_App |
      git clone https://github.com/fedezaff/django_IFTS_project.git |
```

3. Dependencies and virtual enviroment
    - Install the following dependencies :

**Step 1: apt-get update**

**Step 2: apt-get install -y python3 python3-pip python3-venv libmysqlclient-dev build-essential**

#### Virtual Environment

**Step 1: Create a virtual environment inside your project directory**

```
python3 -m venv venv
```

**Step 2: Activate the virtual environment**

```
source venv/bin/activate
```

**Step 3: Upgrade pip to the latest version**

```
pip install --upgrade pip
```

**Step 4: Install Django and MySQL client library**

```
pip install django mysqlclient
```

##### Step 5: Create a new Django project (if you haven't already created one)**

```
django-admin startproject myproject.
```

**Step 6: Edit the settings\.py file to configure the database and allowed hosts**

**(You can use a text editor like nano or vim)**

```
nano myproject/settings.py
```

**Add your Docker MySQL database configuration to the settings\.py:**

```
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'yourdbname',

        'USER': 'yourdbuser',

        'PASSWORD': 'yourdbpassword',

        'HOST': 'db',  # This is the name of the MySQL service in your docker-compose.yml

        'PORT': '3306',

    }

}
```

#

**Also, add the hostname to ALLOWED_HOSTS:**

```
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your_hostname']
```

**Step 7: Run Django migrations**

```
python manage.py migrate
```

**Step 8: Create a superuser for accessing the Django admin**

```
python manage.py createsuperuser
```

**Step 9: Run the Django development server**

```
python manage.py runserver 0.0.0.0:8000
```

**Summary of Commands:**
**Before Creating the Virtual Environment:**

```
docker-compose up -d
docker exec -it interactive_ubuntu /bin/bash
apt-get update
apt-get install -y python3 python3-pip python3-venv libmysqlclient-dev build-essential
cd /data/my_django_project
```

**Inside the Virtual Environment:**

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django mysqlclient
django-admin startproject myproject .
nano myproject/settings.py (Edit settings for database and allowed hosts)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
 ```

Once the server is running, you can access the Django application at \<<http://localhost:8000>> in your browser.
