# Generated by Django 4.0.5 on 2022-07-07 11:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0007_alter_books_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='authorEmail',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='books',
            name='authorName',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='books',
            name='bookLocation',
            field=models.CharField(blank=True, choices=[('HOME', 'Home'), ('OFFICE', 'Office'), ('INTO THE MATRIX', 'Into the Matrix')], default='Home', max_length=30),
        ),
        migrations.AlterField(
            model_name='books',
            name='bookType',
            field=models.CharField(blank=True, choices=[('PHYSICAL', 'Physical'), ('PAPERBACK', 'Paperback'), ('DIGITAL', 'Digital')], default='Physical', max_length=12),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(blank=True, default="User hasn't placed a bio yet.", max_length=300),
        ),
        migrations.AlterField(
            model_name='books',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='books_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
