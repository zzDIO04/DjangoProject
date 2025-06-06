# Generated by Django 5.2.2 on 2025-06-07 00:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_quiz_pergunta_resposta'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TentativaQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acertos', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tentativas', to=settings.AUTH_USER_MODEL)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tentativas', to='principal.quiz')),
            ],
        ),
    ]
