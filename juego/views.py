from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .forms import JuegoForm
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.urlresolvers import reverse


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
                juego_nuevo.save()
                template = 'juego/anuncioexitoso.html'
                ctx = {
                    'juego_nuevo': juego_nuevo
                }
                return render(request, template, ctx)
            else:
                messages.error(request, 'Algo falló')
                return HttpResponseRedirect(reverse('juego:anuncio'))
