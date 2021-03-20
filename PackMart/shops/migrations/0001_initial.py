# Generated by Django 3.1.7 on 2021-03-20 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('business_type', models.CharField(choices=[('S', 'Service'), ('P', 'Product')], max_length=10)),
                ('product_type', models.CharField(choices=[('Antiques and Collectibles', 'Antiques and Collectibles'), ('Arts and Crafts', 'Arts and Crafts'), ('Food', 'Food'), ('Fashion', 'Fashion'), ('Health and Beauty', 'Health and Beauty'), ('Technology', 'Technology'), ('Tools and Equipment', 'Tools and Equipment'), ('Home', 'Home'), ('General', 'General')], default='General', max_length=30)),
                ('service_type', models.CharField(choices=[('Automotive', 'Automotive'), ('Health_and_Beauty', 'Health and Beauty'), ('Technology', 'Technology'), ('Creative', 'Creative'), ('Skilled Trade', 'Skilled Trade'), ('Lessons_and_Tutoring', 'Lessons and Tutoring'), ('Pet', 'Pet'), ('Legal', 'Legal'), ('Labor', 'Labor'), ('General', 'General')], default='General', max_length=30)),
                ('description', models.CharField(max_length=512)),
                ('owner_bio', models.CharField(max_length=512)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=512)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop'),
        ),
    ]
