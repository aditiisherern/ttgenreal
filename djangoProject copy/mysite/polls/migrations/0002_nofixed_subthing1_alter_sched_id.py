# Generated by Django 5.0.7 on 2024-09-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nofixed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nofix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='subthing1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diction', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='sched',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]