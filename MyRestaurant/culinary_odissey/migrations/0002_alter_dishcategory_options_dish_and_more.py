# Generated by Django 5.0 on 2023-12-26 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culinary_odissey', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ('order',), 'verbose_name_plural': 'Disch categories'},
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('ingredients', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo', models.ImageField(blank=True, upload_to='dishes/')),
                ('is_visible', models.BooleanField(default=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dishes', to='culinary_odissey.dishcategory')),
            ],
            options={
                'verbose_name_plural': 'Dishes',
                'ordering': ('order',),
            },
        ),
        migrations.AddConstraint(
            model_name='dish',
            constraint=models.UniqueConstraint(fields=('order', 'category'), name='unique_order_per_each_category'),
        ),
        migrations.AlterUniqueTogether(
            name='dish',
            unique_together={('id', 'slug')},
        ),
    ]
