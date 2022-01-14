# Generated by Django 4.0 on 2022-01-11 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_calendar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendar',
            options={'ordering': ('-publish',), 'verbose_name': 'Ближайшие события', 'verbose_name_plural': 'Ближайшие события'},
        ),
        migrations.RemoveField(
            model_name='calendar',
            name='cover',
        ),
        migrations.AddField(
            model_name='calendar',
            name='date_go',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Когда будет мероприятие'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='body',
            field=models.TextField(verbose_name='Текст для статьи'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='short',
            field=models.TextField(max_length=90, verbose_name='Кратко написать(отображается на главной)'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, verbose_name='Выбрать паблиш если нужно опубликовать или драфт если необходимо скрыть'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
    ]
