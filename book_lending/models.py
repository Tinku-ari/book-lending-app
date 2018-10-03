from django.db import models
from django.utils import timezone

class Language(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(
            default=timezone.now, blank=True)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name

class PeopleStatus(models.Model):
    name = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = 'peoplestatus'

    def __str__(self):
        return self.name

class BookStatus(models.Model):
    name = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = 'bookstatus'

    def __str__(self):
        return self.name

class BookLendingStatus(models.Model):
    name = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = 'booklendingstatus'

    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    standard = models.PositiveIntegerField()
    section = models.CharField(max_length=20, blank=True, null=True, default=None)
    status = models.ForeignKey('PeopleStatus', on_delete=models.CASCADE)

    class Meta:
        db_table = 'people'

    def __str__(self):
        return self.name

class Book(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, default=None, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True, default=None)
    level = models.PositiveIntegerField(blank=True, null=True, default=None)
    isbn = models.CharField(max_length=50, blank=True, null=True, default=None)
    language_code = models.ForeignKey('Language', to_field='code', on_delete=models.CASCADE)
    status = models.ForeignKey('BookStatus', on_delete=models.CASCADE)
    created_at = models.DateTimeField(
            default=timezone.now, null=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title


class BookLending(models.Model):
    people = models.ForeignKey('People', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    date_lent = models.DateTimeField(
            default=timezone.now, null=False)
    date_returned = models.DateTimeField(null=True)
    status = models.ForeignKey('BookLendingStatus', on_delete=models.CASCADE)

    class Meta:
        db_table = 'booklending'


