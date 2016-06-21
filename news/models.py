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


class Menu(models.Model):
    menu_classes = (
        ('mt', 'Single main menu'),
        ('sub-menu', 'Menu with sub menu'),
        ('sub','Sub menu'),
    )
    menu_text = models.CharField(max_length=30, blank=True, null=True)
    menu_class = models.CharField(max_length=8, choices=menu_classes)
    menu_href = models.CharField(max_length=30)
    menu_ico = models.CharField(max_length=15);
    menu_have_subs = models.BooleanField();
    menu_parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.menu_text + " " + self.menu_href

