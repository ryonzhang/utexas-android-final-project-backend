# Generated by Django 3.0.6 on 2020-11-29 23:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=255, unique=True, verbose_name='Name')),
                ('introduction', models.TextField(help_text='Introduction', verbose_name='Introduction')),
                ('rating', models.IntegerField(help_text='Rating', verbose_name='Rating')),
                ('num_of_comments', models.IntegerField(help_text='Number of Comments', verbose_name='Number of Comments')),
                ('price', models.DecimalField(decimal_places=2, help_text='Price', max_digits=6, verbose_name='Price')),
                ('amount_left', models.IntegerField(help_text='Amount Left', verbose_name='Amount Left')),
                ('amount_sold', models.IntegerField(help_text='Amount Sold', verbose_name='Amount Sold')),
                ('features', models.TextField(help_text='Features', verbose_name='Features')),
                ('category', models.TextField(help_text='Category', verbose_name='Category')),
                ('thumbnail_url', models.TextField(help_text='Thumbnail URL', verbose_name='Thumbnail URL')),
                ('image_url', models.TextField(help_text='Image URL', verbose_name='Image URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('owner', models.ForeignKey(help_text='Owner', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('shop', models.ForeignKey(help_text='Shop', on_delete=django.db.models.deletion.CASCADE, to='shops.Shop', verbose_name='Shop')),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
                'ordering': ('rating',),
            },
        ),
    ]
