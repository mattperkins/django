# $ django-admin startproject newProj
# $ cd newProj
# $ python3 manage.py runserver

# settings.py add: 'DIRS': ['templates'],

# python3 manage.py startapp newApps

# settings.py INSTALLED_APPS add : ['appName']

# initialise default setup
# python3 manage.py migrate

# make models.py for app then: 
# python3 manage.py makemigrations
# python3 manage.py migrate


# Django ORM
# test against the database
# from within project directory:
# $ python3 manage.py shell
# >>> from articles.models import Article
# >>> Article.objects.all()
# >>> article = Article()
# >>> article.title = "A title"
# >>> article.save()
# >>> Article.objects.all()

# configure superuser admin/login
# $ python3 manage.py createsuperuser