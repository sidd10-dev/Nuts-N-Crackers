# Generated by Django 3.2 on 2021-07-29 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nnc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('brand', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('product_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nnc.category')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nnc.product')),
            ],
        ),
    ]