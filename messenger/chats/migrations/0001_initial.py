# Generated by Django 2.2.5 on 2019-12-04 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='NoName', max_length=128, verbose_name='Title chat')),
                ('is_group_chat', models.BooleanField(default=False, verbose_name='Group chat')),
                ('chat_avatar', models.FileField(default='default.png', upload_to='', verbose_name='Avatar of chat')),
                ('last_message', models.IntegerField(null=True, verbose_name='Id last message')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_read_message', models.IntegerField(null=True, verbose_name='Id last read message')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Chat')),
            ],
        ),
    ]
