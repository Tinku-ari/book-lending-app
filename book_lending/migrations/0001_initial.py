# Generated by Django 2.0.8 on 2018-09-28 09:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=50)),
                ('level', models.PositiveIntegerField()),
                ('isbn', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('standard', models.PositiveIntegerField()),
                ('section', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PeopleStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_lending.PeopleStatus'),
        ),
        migrations.AddField(
            model_name='book',
            name='language_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_lending.Language', to_field='code'),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_lending.BookStatus'),
        ),
    ]
