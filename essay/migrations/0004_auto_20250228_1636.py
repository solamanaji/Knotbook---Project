# Generated by Django 3.2.7 on 2025-02-28 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knotebook', '00011_initial'),
        ('essay', '0003_auto_20250228_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_title', models.CharField(max_length=255)),
                ('question', models.TextField()),
                ('correct_answer', models.TextField()),
                ('correct_answer_score', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='StudentResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_title', models.CharField(max_length=255)),
                ('user_response', models.TextField(blank=True, null=True)),
                ('user_response_score', models.FloatField(default=0.0)),
                ('tgpa', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essay.questionbank')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knotebook.student_table')),
            ],
            options={
                'unique_together': {('student', 'exam_title')},
            },
        ),
        migrations.DeleteModel(
            name='QuestionAnswer',
        ),
    ]
