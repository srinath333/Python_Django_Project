# Generated by Django 2.2.4 on 2019-08-05 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raters_app', '0002_items_workflows'),
    ]

    operations = [
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rater_id', models.CharField(max_length=30)),
                ('item_id', models.CharField(max_length=30)),
                ('workflow_id', models.CharField(max_length=30)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('Judmenent_answer', models.CharField(blank=True, max_length=100)),
                ('Prediction_A', models.CharField(blank=True, max_length=100)),
                ('Prediction_B', models.CharField(blank=True, max_length=100)),
                ('Prediction_C', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='workflows',
            name='Instruction',
            field=models.CharField(default='Default Instruction', max_length=100),
        ),
        migrations.AddField(
            model_name='workflows',
            name='Judgement_question',
            field=models.CharField(default='Model Judgement question', max_length=100),
        ),
        migrations.AddField(
            model_name='workflows',
            name='Prediction_question',
            field=models.CharField(default='Model Prediction question', max_length=100),
        ),
    ]
