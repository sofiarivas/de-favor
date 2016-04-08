from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .forms import JuegoForm
from django.utils.decorators import method_decorator


class JuegoView(View):
    @method_decorator(login_required(login_url='cuentas:login'))
    def get(self, request):
        form = JuegoForm()
        template = 'juego/anuncio.html'
        ctx = {'form': form}
        return render(request, template, ctx)

    def post(self, request):
            juego_nuevo = JuegoForm(request.POST, request.FILES)
            if juego_nuevo.is_valid():
                juego_nuevo.save(commit=False)
                juego_nuevo.usuario = request.User
                juego_nuevo.save()
            return redirect('main:detalle')
