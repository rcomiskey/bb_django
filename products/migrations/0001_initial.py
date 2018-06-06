# Generated by Django 2.0.1 on 2018-05-17 20:38

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regex', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.Category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colourOptions', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aw_deep_link', models.CharField(default='', max_length=500)),
                ('product_name', models.CharField(default='', max_length=500)),
                ('aw_image_url', models.CharField(default='', max_length=500)),
                ('search_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('merchant_name', models.CharField(default='', max_length=500)),
                ('display_price', models.CharField(default='', max_length=500)),
                ('colour', models.CharField(default='', max_length=500)),
                ('rrp_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('description', models.CharField(default='', max_length=500)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Brand')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
                ('colourOptions', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Colour')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Size'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('parent', 'slug')},
        ),
    ]
