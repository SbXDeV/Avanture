from django.shortcuts import render
from django.views.generic import DetailView

from Index.forms import BackForms
from .models import IndexPhone, IndexMenu, IndexHowToWork, IndexCases, IndexFAQ, IndexReview, Police, UserAccept


def Index(request):
    phone = IndexPhone.objects.all()
    menu = IndexMenu.objects.all()
    work = IndexHowToWork.objects.all()
    case = IndexCases.objects.all()
    faq = IndexFAQ.objects.all()
    review = IndexReview.objects.all()
    policy = Police.objects.all()
    user = UserAccept.objects.all()
    context = {
        'phone': phone,
        'menu': menu,
        'work': work,
        'case': case,
        'faq': faq,
        'review': review,
        'policy': policy,
        'user': user,
    }
    if request.method == "POST":
        form = BackForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print('Проблема какая то: ', form.errors)
    return render(request, 'Index/index.html', context)


def DetailCase(request, pk):
    phone = IndexPhone.objects.all()
    menu = IndexMenu.objects.all()
    case = IndexCases.objects.filter(id=pk)
    context = {
        'phone': phone,
        'menu': menu,
        'case': case
    }
    if request.method == "POST":
        form = BackForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print('Проблема какая то: ', form.errors)
    return render(request, 'Index/case.html', context)


def page_not_found_view(request, exception):
    return render(request, 'Index/404.html', status=404)
