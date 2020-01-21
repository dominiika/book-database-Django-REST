from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # added by this user
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return '{0.first_name} {0.last_name}'.format(self)

    class Meta:
        ordering = ['last_name']

    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.title())
        super(Author, self).save(*args, **kwargs)


class Publisher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # added by this user
    name = models.CharField(max_length=150)
    established = models.IntegerField(default=2019,
                                      validators=[MaxValueValidator(datetime.now().year), MinValueValidator(1800)]
                                      )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    #  Capitalize the first letter
    def save(self, *args, **kwargs):
        val = getattr(self, 'name', False)
        if val.upper() != val:
            if val:
                setattr(self, 'name', val.title())
        super(Publisher, self).save(*args, **kwargs)


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # added by this user
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=17)
    published = models.IntegerField(default=2019,
                                    validators=[MaxValueValidator(datetime.now().year), MinValueValidator(1800)]
                                    )

    def __str__(self):
        return '{0.title} - {0.author}'.format(self)

    class Meta:
        ordering = ['title']

    #  Capitalize the first letter
    def save(self, *args, **kwargs):
        val = getattr(self, 'title', False)
        if val:
            setattr(self, 'title', val.title())
        super(Book, self).save(*args, **kwargs)
