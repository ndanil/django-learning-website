from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50, default='guest')
    email = models.EmailField(default='example@example.com')

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    time = models.DateField()
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + " " + self.text[:min(len(self.text),20)]