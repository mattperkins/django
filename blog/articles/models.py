from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thumbnail
    # add author

    # show string version in database
    # using >>> Article.objects.all()
    # (self) = instance of the article
    def __str__(self):
        return self.title