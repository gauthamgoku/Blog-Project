# Generated by Django 2.1 on 2019-05-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_delete_article_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('article_comment', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'article_comment',
            },
        ),
    ]