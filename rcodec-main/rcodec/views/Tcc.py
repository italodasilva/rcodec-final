from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rcodec.models import Tcc
from django import forms
from django.forms import ModelForm

class TccForm(ModelForm):
    class Meta:
        model = Tcc
        fields = '__all__'
        widgets = {
            'descricao' : forms.Textarea()
        }

def listar(request):
    tcc =  Tcc.objects.all()

    return render(request, 'core/pagina3.html', {
        'tcc': tcc
    })


def criar(request):
    frm = TccForm(request.POST or None, request.FILES or None)

    print(request.FILES)

    if frm.is_valid():
        frm.save()
        return redirect('tcc')

    return render(request, 'core/pagina4.html',{
        'titulo' : 'Enviar Arquivo',
        'frm':frm
    })

def editar(request,id):
    tcc = get_object_or_404(Tcc, pk=id)
    frm = TccForm(request.POST or None, instance=tcc)

    if frm.is_valid():
        frm.save()
        return redirect('tcc')

    return render(request, 'core/pagina4.html',{
        'titulo' : 'Editar Arquivo',
        'frm':frm
    })

def excluir(request,id):
    tcc = get_object_or_404(Tcc, pk=id)
    tcc.delete()

    return redirect('tcc')

def mostrar_pdf(request,id):
    t = get_object_or_404(Tcc, pk=id)

    return HttpResponse(t.pdf.read )