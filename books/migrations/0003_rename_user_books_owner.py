# Generated by Django 4.0.5 on 2022-07-04 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_booklocation_books_coverimage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='user',
            new_name='owner',
        ),
    ]