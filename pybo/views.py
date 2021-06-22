from django.views import View
from django.shortcuts import render

from pybo.models import Question


class Index(View):
    def get(self, request):

        question_list = Question.objects.order_by('-created_datetime')
        context = {
            'question_list': question_list
        }

        return render(request, 'pybo/question_list.html', context)
