# Generated by Django 2.1.4 on 2018-12-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_nome', models.CharField(max_length=80)),
                ('sub_url_name', models.CharField(max_length=150)),
                ('sub_icon_class', models.CharField(max_length=150)),
            ],
        ),
    ]
