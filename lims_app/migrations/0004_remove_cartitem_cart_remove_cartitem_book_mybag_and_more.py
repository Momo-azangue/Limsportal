# Generated by Django 5.0.1 on 2024-02-01 05:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0003_cart_cartitem_returns_delete_mybag_cart_items'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='book',
        ),
        migrations.CreateModel(
            name='MyBag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyBagItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lims_app.book')),
                ('mybag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lims_app.mybag')),
            ],
        ),
        migrations.AddField(
            model_name='mybag',
            name='items',
            field=models.ManyToManyField(through='lims_app.MyBagItem', to='lims_app.book'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]