from django import forms
from .models import Question

class PostForm(forms.ModelForm):
	category=forms.ChoiceField(choices=[('hobby', '趣味'),
		('life', '生活・暮らし'),
		('beauty', '美容・健康'),
		('fashion', 'ファッション'),
		('human', '恋愛・人間関係'),
		('child', '子育て'),
		('internet', 'インターネット'),
		('kaden', '家電'),
		('computer','コンピュータ'),
		('academic', '学問・サイエンス'),
		('business', 'ビジネス・経済・お金'),
		('news', 'ニュース・政治'),
		('carrer', 'キャリア'),
		('trip', '旅行'),
		('sports', 'スポーツ'),
		('other', 'その他')])
	class Meta: 
		model = Question
		fields = ('title','text','ans1','ans2','ans3','ans4','category','photo')
		error_messages = {
            'title': {
                'required': '必須',
                'max_length': '20字以内です'
            },
            'ans1': {
                'required': '必須',
                'max_length': '30字以内です',
            },
			'ans2': {
                'required': '必須',
                'max_length': '30字以内です',
            },
			'ans3': {
                'max_length': '30字以内です',
            },
			'ans4': {
                'max_length': '30字以内です',
            }
        }