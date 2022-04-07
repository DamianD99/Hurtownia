from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404

from django.conf import settings

from cart.forms import CartAddProductForm
from .forms import ProduktyForm, ZamowieniaFrom, ZwrotForm, EmailForm

from django.core.mail import send_mail

from .models import Zamówienia, Produkty, Zwrot


@login_required(login_url='user-login')
def index(request):
    zamówienia = Zamówienia.objects.all()
    produkty = Produkty.objects.all()
    if request.method == 'POST':
        form = ZamowieniaFrom(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('hurtownia-index')
    else:
        form = ZamowieniaFrom()
    context = {
        'zamówienia': zamówienia,
        'form': form,
        'produkty': produkty,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
def developer(request):
    return render(request, 'dashboard/developer.html')


@login_required(login_url='user-login')
def zamówienia(request):
    zamówienia = Zamówienia.objects.all()
    produkty = Produkty.objects.all()

    context = {
        'zamówienia': zamówienia,
        'produkty': produkty,

    }

    return render(request, 'dashboard/zamówienia.html', context)


@login_required(login_url='user-login')
def produkty(request):
    produkty = Produkty.objects.all()

    if request.method == 'POST':
        form = ProduktyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produkty')
    else:
        form = ProduktyForm()
    context = {
        'produkty': produkty,
        'form': form,
    }
    return render(request, 'dashboard/produkty.html', context)


@login_required(login_url='user-login')
def update_produkt(request, pk):
    produkty = Produkty.objects.get(id=pk)
    form = ProduktyForm(instance=produkty)

    if request.method == 'POST':
        messages.success(request, "Udało ci sie pomyslnie zmienic parametry")
        form = ProduktyForm(request.POST, instance=produkty)
        if form.is_valid():
            form.save()
            return redirect('hurtownia-developer')

    context = {'form': form}

    return render(request, 'dashboard/produkt_update.html', context)


@login_required(login_url='user-login')
def delete_produkt(request, pk):
    produkty = Produkty.objects.get(id=pk)
    if request.method == 'POST':
        produkty.delete()
        return redirect('hurtownia-developer')
    context = {'item': produkty}

    return render(request, 'dashboard/produkty_delete.html', context)


@login_required(login_url='user-login')
def klijent(request):
    klijent = User.objects.all()
    context = {
        'klijent': klijent
    }
    return render(request, 'dashboard/klijenci.html', context)


@login_required(login_url='user-login')
def klijent_pokaz(request, pk):
    klijent = User.objects.get(id=pk)
    context = {
        'klijent': klijent
    }
    return render(request, 'dashboard/klijent_pokaz.html', context)


def start(request):
    return render(request, 'partnerzy/start_wszystko.html')


def pokaz_produkt(request, id, slug):
    produkty = get_object_or_404(Produkty,
                                 id=id,
                                 slug=slug, available=True)
    cart_product_form =CartAddProductForm()

    return render(request,
                  'dashboard/pokaz_produkt.html', {'produkty': produkty,
                                                   'cart_product_form':cart_product_form})


def sendMail(request):
    messageSent = False
    if request.method == 'POST':

        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an email with Django"
            message = cd['Wiadomość do admintratora']

            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['Emial']])
            messageSent = True
    else:
        form = EmailForm()

    return render(request, 'dashboard/contact.html', {

        'form': form,
        'messageSent': messageSent,

    })


def serwis(request):
    return render(request, "dashboard/serwis.html", {})


def zwrot(request):
    zwrot = Zwrot.objects.all()

    if request.method == 'POST':
        form = ZwrotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produkty')
    else:
        form = ZwrotForm()
    context = {
        'zwrot': zwrot,
        'form': form,
    }
    return render(request, "dashboard/zwrot.html", context)


def reklamacja(request):
    return render(request, "dashboard/reklamacja.html", {})


def zwroty_admin(request):
    zwrot = Zwrot.objects.all()
    produkty = Produkty.objects.all()
    context = {
        'zwrot': zwrot,
        'produkty': produkty,
    }
    return render(request, "dashboard/zwroty_admin.html", context)


