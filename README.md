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
  # >>> from articles.models import Article || from music.models import Album
  # >>> Article.objects.all() || Album.objects.all()
  # >>> article = Article() || album = Album()
  # >>> article.title = "A title" || album.album_title = "New Album"
  # >>> article.save()
  # >>> Article.objects.all()

# >>> a = Album(artist="Artist", album_title="Album", genre="Pop", album_logo="#")
# >>> a.save()

### Alternative way to write object data to database
# >>> b = Album()
# >>> b.artist = ""
# >>> b.album_title = ""
# >>> b.genre = ""
# >>> b.album_logo = ""
# >>> b.save()

### Read from database
# >>> a.artist // prints 'Artist' 
# >>> a.album_title // prints 'Album'
# >>> a.id // prints id for that object/item in database

# >>> Album.objects.filter(id=1)
# >>> Album.objects.filter(artist__startswith='Art') // prints any artist with 'Art...'

# configure superuser admin/login
# $ python3 manage.py createsuperuser