# Generated by Django 3.2.4 on 2021-06-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solo_proj', '0003_alter_song_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]