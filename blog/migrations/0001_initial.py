# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 21:21
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=15, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff Status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated asactive. Unselect this instead of deleting accounts', verbose_name='Active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('about_content', models.TextField()),
                ('about_image', models.ImageField(upload_to='uploads/')),
                ('about_image_active', models.BooleanField(default=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_active', models.BooleanField(default=True)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('contact_number_active', models.BooleanField(default=True)),
                ('address', models.CharField(blank=True, max_length=254, null=True)),
                ('address_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.SlugField()),
                ('subtitle', models.CharField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('content', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('meta', models.TextField(blank=True, null=True)),
                ('last_edited', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField()),
                ('category_desc', models.CharField(max_length=254, verbose_name='Category Description')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
    ]