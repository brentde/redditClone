# Generated by Django 2.2.5 on 2019-10-06 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorldApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='suggestion2',
            field=models.CharField(default='', max_length=240),
            preserve_default=False,
        ),
    ]
