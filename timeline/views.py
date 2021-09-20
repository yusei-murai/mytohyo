from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from .models import Question,Good
from accounts.models import CustomUser
from django.contrib import messages
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        posts = Question.objects.order_by('-created_at')
        return posts
        
class UserView(LoginRequiredMixin, generic.ListView):
    template_name = 'user.html'
    model = CustomUser

    def get_queryset(self):
        posts = Question.objects.order_by('-created_at')
        return posts
        
class CategoryView(generic.ListView):
	template_name = 'category.html'
	paginate_by = 10
	
	def get_context_data(self, **kwargs):
		ur=self.request.path.strip("/")
		ur=ur.replace('category/', '')
		CHOICES = {
		'hobby':'趣味',
		'life':'生活・暮らし',
		'beauty': '美容・健康',
		'fashion': 'ファッション',
		'human': '恋愛・人間関係',
		'child': '子育て',
		'internet': 'インターネット',
		'kaden':'家電',
		'computer':'コンピュータ',
		'academic': '学問・サイエンス',
		'business': 'ビジネス・経済・お金',
		'news': 'ニュース・政治',
		'carrer': 'キャリア',
		'trip': '旅行',
		'sports': 'スポーツ',
		'other': 'その他'
		}
		context = super().get_context_data(**kwargs)
		context['cat'] = CHOICES[ur]
		return context
		
	def get_queryset(self):
		ur=self.request.path.strip("/")
		ur=ur.replace('category/', '')
		posts = Question.objects.filter(category=ur).order_by('-created_at')
		return posts

class CreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PostForm
    success_url = reverse_lazy('timeline:index')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        messages.success(self.request, '投稿が完了しました')
        return super(CreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, '投稿が失敗しました')
        return redirect('timeline:index')
        
class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Question
    success_url = reverse_lazy('timeline:index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == request.user:
            messages.success(self.request, '削除しました')
            return super().delete(request, *args, **kwargs)
			
class PostView(LoginRequiredMixin,generic.TemplateView):
	template_name = "posting.html"
            
class QView(generic.DetailView):
    model = Question
    template_name="q.html"
	
def privacy(request):
	return render(request,'privacy.html')

@login_required
def good1(request, pk):
	post = get_object_or_404(Question, pk=pk)
	good = Good.objects.filter(q=post,user=request.user, num=1)
	
	if request.method == 'POST':
		if good.exists() == False:
			post.ans1_num += 1
			Good.objects.create(q=post,user=request.user,num=1)
			post.save()
		else:
			post.ans1_num -= 1
			good.delete()
			post.save()
	return redirect('timeline:q',pk)

@login_required
def good2(request, pk):
    post = get_object_or_404(Question, pk=pk)
    good = Good.objects.filter(q=post,user=request.user,num=2)

    if request.method == 'POST':
        if good.exists() == False:
            post.ans2_num += 1
            Good.objects.create(q=post,user=request.user, num=2)
            post.save()
        else:
            post.ans2_num -= 1
            good.delete()
            post.save()

    return redirect('timeline:q',pk)
        
@login_required
def good3(request, pk):
    post = get_object_or_404(Question, pk=pk)
    good = Good.objects.filter(q=post,user=request.user,num=3)

    if request.method == 'POST':
        if good.exists() == False:
            post.ans3_num += 1
            Good.objects.create(q=post,user=request.user,num=3)
            post.save()
        else:
            post.ans3_num -= 1
            good.delete()
            post.save()

    return redirect('timeline:q',pk)
	
@login_required
def good4(request, pk):
    post = get_object_or_404(Question, pk=pk)
    good = Good.objects.filter(q=post,user=request.user,num=4)

    if request.method == 'POST':
        if good.exists() == False:
            post.ans4_num += 1
            Good.objects.create(q=post,user=request.user,num=4)
            post.save()
        else:
            post.ans4_num -= 1
            good.delete()
            post.save()

    return redirect('timeline:q',pk)

            
#class GoodView(LoginRequiredMixin, generic.View):
 #   model = Good
    
   # def post(self,request):

index = IndexView.as_view() 
create = CreateView.as_view()
delete = DeleteView.as_view()
q=QView.as_view()
u=UserView.as_view()
cate=CategoryView.as_view()
p=PostView.as_view()