# Generated by Django 4.2 on 2023-04-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_rentissue_drop_off_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('email', models.CharField(max_length=128, verbose_name='Email')),
                ('theme', models.CharField(max_length=128, verbose_name='Theme')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'User Message',
                'verbose_name_plural': 'UserMessages',
            },
        ),
        migrations.AlterField(
            model_name='rentissue',
            name='rent_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Per Hour Rate'), (2, 'Per Day Rate'), (3, 'Leasing')], default=1, verbose_name='Rent Type'),
        ),
    ]
