# Generated by Django 3.0.5 on 2020-05-05 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todo_duedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='parentTodo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='todos.Todo'),
        ),
    ]
