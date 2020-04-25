# Generated by Django 3.0.5 on 2020-04-25 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cyberpunk_ccg_archive', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedImage',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notifications.Notification')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyberpunk_ccg_archive.Image')),
            ],
            bases=('notifications.notification',),
        ),
        migrations.CreateModel(
            name='SubmittedCard',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notifications.Notification')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyberpunk_ccg_archive.Card')),
            ],
            bases=('notifications.notification',),
        ),
    ]
