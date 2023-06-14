# Generated by Django 4.1 on 2023-06-14 13:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('tag', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(default='', unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'unique_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
                ('blob', models.TextField()),
                ('book_image', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField(default='')),
                ('genre', models.ManyToManyField(blank=True, related_name='tags', to='books_app.tag')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]