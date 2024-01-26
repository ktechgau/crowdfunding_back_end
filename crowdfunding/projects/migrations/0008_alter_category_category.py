# Generated by Django 4.2.3 on 2024-01-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_remove_category_name_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('BUSINESS', 'Business Management & Entrepreneurship'), ('ENGINEERING', 'Engineering, Automation & Technology'), ('AGRI', 'Agriculture'), ('IT', 'IT and Computing'), ('EDUCATION', 'Teaching, Education & Training'), ('ARCHITECTURE', 'Architecture, Construction & Planning'), ('OTHER', 'Other'), ('TRAVEL', 'Travel, Tourism & Hospitality'), ('LAW', 'Law, Paralegal'), ('SOCIETY', 'Society, Culture & Humanities'), ('SCIENCES', 'Sciences and Mathematics'), ('CREATIVE', 'Creative arts & Design'), ('HEALTH', 'Health, Medicine, Psychology'), ('ENVIRONMENTAL', 'Environmental Science & Sustainability'), ('PERSONAL', 'Personal Care, Beauty & Hair, Fitness'), ('MEDIA', 'Media & Communications'), ('VET', 'Veterinary Medicine')], default='AGRI', max_length=200),
        ),
    ]
