from django.db import models
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill,ResizeToFit
import uuid

class Question(models.Model):
	CHOICES = [
        ('hobby', '趣味'),
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
		('other', 'その他'),
    ]
	
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	author=models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
	title=models.CharField(max_length=20,verbose_name='タイトル')
	text=models.TextField(verbose_name='質問',null=True,blank=True)
	category=models.CharField(max_length=15,verbose_name='カテゴリー',default='other',choices=CHOICES)
	ans1 = models.CharField(max_length=30,verbose_name='回答１',default="選択肢１")
	ans1_num = models.IntegerField(verbose_name='回答１投票数',default=0)
	ans2 = models.CharField(max_length=30,verbose_name='回答２',default="選択肢２")
	ans2_num = models.IntegerField(verbose_name='回答２投票数',default=0)
	ans3 = models.CharField(max_length=30,verbose_name='回答３',null=True,blank=True)
	ans3_num = models.IntegerField(verbose_name='回答３投票数',default=0)
	ans4 = models.CharField(max_length=30,verbose_name='回答４',null=True,blank=True)
	ans4_num = models.IntegerField(verbose_name='回答４投票数',default=0)
	photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
	post_photo = ImageSpecField(source='photo',processors=[ResizeToFit(500, 500)],format='JPEG',options={'quality':60})
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	
	def get_good(self):
		goods = Good.objects.filter(post=self)
		return [good.user for good in goods]
		
	def __str__(self):
		return self.get_category_display()

"""
class Answer(models.Model):
	post=models.ForeignKey('Question',on_delete=models.CASCADE)
	ans=models.CharField(max_length=20,verbose_name='回答内容')
	
	def get_good(self):
		goods = Good.objects.filter(ans=self)
		return [good.user for good in goods]
"""
		
class Good(models.Model):
	q=models.ForeignKey('Question',on_delete=models.CASCADE,null=True)
	user=models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
	num=models.IntegerField(verbose_name='問題番号',default=0)
	
		
