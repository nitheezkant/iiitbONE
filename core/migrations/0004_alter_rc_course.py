# Generated by Django 4.0.3 on 2022-08-08 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_rc_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rc',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.course'),
        ),
    ]
