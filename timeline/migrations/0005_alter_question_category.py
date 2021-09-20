# Generated by Django 3.2.6 on 2021-08-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_alter_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('hobby', '趣味'), ('life', '生活・暮らし'), ('beauty', '美容・健康'), ('fashion', 'ファッション'), ('human', '恋愛・人間関係'), ('child', '子育て'), ('internet', 'インターネット'), ('kaden', '家電'), ('computer', 'コンピュータ'), ('academic', '学問・サイエンス'), ('business', 'ビジネス・経済・お金'), ('news', 'ニュース・政治'), ('carrer', 'キャリア'), ('trip', '旅行'), ('sports', 'スポーツ'), ('other', 'その他')], default='other', max_length=15, verbose_name='カテゴリー'),
        ),
    ]
