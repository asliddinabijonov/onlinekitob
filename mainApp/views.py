from django.shortcuts import render, redirect
from .models import *
from django.views import View
from .forms import *


class BolimView(View):
    def get(self, request):
        bolim = Bolim.objects.all()
        context = {
            'bolimlar': bolim
        }
        return render(request, 'bolim.html', context)


class KitobView(View):
    def get(self, request):
        kitoblar = Kitob.objects.all()
        context = {
            'kitoblar': kitoblar,
            'form': KitobForm()
        }
        return render(request, 'kitoblar.html', context)

    def post(self, request):
        if request.method == "POST":
            form = KitobForm(request.POST)
            if form.is_valid():
                form.save()

        return redirect('/kitoblar/', )


class YangiView(View):
    def get(self, request):
        tiriklar = Kitob.objects.filter(muallif__tirik=True)
        context = {
            'tiriklar': tiriklar
        }
        return (request, 'yangi.html', context)


class KitobHaqidaView(View):
    def get(self, request, pk):
        kitob = Kitob.objects.get(pk=pk)
        context = {
            'kitob': kitob
        }
        return render(request, 'kitob.html', context)


class KitobEditView(View):
    def get(self, request, pk):
        kitob = Kitob.objects.get(pk=pk)
        form = KitobForm(instance=kitob)
        context = {
            'kitob': kitob,
            'form': form
        }
        return render(request, 'tahrirlash.html', context)

    def post(self, request, pk):
        kitob = Kitob.objects.get(pk=pk)
        if request.method == "POST":
            kitobform = KitobForm(request.POST, instance=kitob)
            if kitobform.is_valid():
                kitob.save()
            return redirect('/kitoblar/')
