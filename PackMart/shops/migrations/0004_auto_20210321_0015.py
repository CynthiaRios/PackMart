# Generated by Django 3.1.7 on 2021-03-21 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20210321_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='owner_bio',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='product_type',
            field=models.CharField(choices=[('Antiques and Collectibles', 'Antiques and Collectibles'), ('Arts and Crafts', 'Arts and Crafts'), ('Food', 'Food'), ('Fashion', 'Fashion'), ('Health and Beauty', 'Health and Beauty'), ('Technology', 'Technology'), ('Tools and Equipment', 'Tools and Equipment'), ('Home', 'Home'), ('General', 'General')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='service_type',
            field=models.CharField(choices=[('Automotive', 'Automotive'), ('Health_and_Beauty', 'Health and Beauty'), ('Technology', 'Technology'), ('Creative', 'Creative'), ('Skilled Trade', 'Skilled Trade'), ('Lessons_and_Tutoring', 'Lessons and Tutoring'), ('Pet', 'Pet'), ('Legal', 'Legal'), ('Labor', 'Labor'), ('General', 'General')], max_length=30, null=True),
        ),
    ]