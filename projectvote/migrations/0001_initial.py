# Generated by Django 4.0.5 on 2022-06-14 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=300)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=30000, null=True)),
                ('designrate', models.PositiveSmallIntegerField(choices=[(1, '1- Worst'), (2, '2- Awful'), (3, '3- Bad'), (4, '4- Poor'), (5, '5- Average'), (6, '6- Satisfactory'), (7, '7- Good'), (8, '8- Great'), (9, '9- Almost Perfect'), (10, '10- Excellent')])),
                ('contentrate', models.PositiveSmallIntegerField(choices=[(1, '1- Worst'), (2, '2- Awful'), (3, '3- Bad'), (4, '4- Poor'), (5, '5- Average'), (6, '6- Satisfactory'), (7, '7- Good'), (8, '8- Great'), (9, '9- Almost Perfect'), (10, '10- Excellent')])),
                ('usabilityrate', models.PositiveSmallIntegerField(choices=[(1, '1- Worst'), (2, '2- Awful'), (3, '3- Bad'), (4, '4- Poor'), (5, '5- Average'), (6, '6- Satisfactory'), (7, '7- Good'), (8, '8- Great'), (9, '9- Almost Perfect'), (10, '10- Excellent')])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='projectvote.project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('profile_pic', models.ImageField(default='sunrise.png', upload_to='media/')),
                ('bio', models.TextField(blank=True, max_length=400)),
                ('location', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projectvote.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
