from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')
# from .models import Question
# Create your views here.
# def index(request):
#     myname = "huân"
#     danhsach = {"điện thoại","laptop","phone"}
#     context = {"name": myname, "bring": danhsach}
#     return render(request, "home/index.html", context)

# def viewlist(request):
#     questions = Question.objects.all()
#     context={"list_question": questions}
#     return render(request, "home/question.html", context)

# def detailView(request, question_id):
#     q = Question.objects.get(pk=question_id)
#     return render(request, "home/detail_question.html", {"question": q})
# def vote(request, question_id):
#     q = Question.objects.get(pk=question_id)
#     data = request.POST["choice"]
#     c = q.choice_set.get(pk=data)
#     c.vote=c.vote+1
#     c.save()
#     return render(request, "home/result.html", {"question": q})
