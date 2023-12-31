# Generated by Django 4.2.3 on 2023-07-15 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcast_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='episode',
            name='podcast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode', to='podcast_app.podcast'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='podcast', to='podcast_app.author'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcast', to='podcast_app.language'),
        ),
    ]
