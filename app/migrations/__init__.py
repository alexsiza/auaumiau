

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
    ]