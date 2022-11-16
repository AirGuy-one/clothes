# Generated by Django 4.1.1 on 2022-10-10 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_clothsdata_time_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='clothsdata',
            options={'verbose_name': 'Вещь', 'verbose_name_plural': 'Вещи'},
        ),
        migrations.AddField(
            model_name='clothsdata',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.categorydata'),
        ),
    ]
