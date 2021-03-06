# Generated by Django 3.0.7 on 2020-06-18 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20200618_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='school_teacher', to='school.School'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='school_student', to='school.School'),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='teacher', to='school.Teacher'),
        ),
    ]
