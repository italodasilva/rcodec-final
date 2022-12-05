"""rcodec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rcodec.views import paginas, Repositorio, Tcc
from rcodec import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paginas.index, name='index'),
    path('index/', paginas.index, name='index'),
    path('home/', paginas.home, name='home'),
    path('pagina1/', paginas.pagina1, name='pagina1'),
    path('pagina2/', paginas.pagina2, name='pagina2'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('repositorio', Repositorio.listar, name='repositorio'),
    path('repositorio/criar', Repositorio.criar, name='repositorio.criar'),
    path('repositorio/editar/<id>', Repositorio.editar, name='repositorio.editar'),
    path('repositorio/excluir/<id>', Repositorio.excluir, name='repositorio.excluir'),
    path('repositorio/mostrar_pdf/<id>', Repositorio.mostrar_pdf, name='mostrar_pdf'),

    path('tcc', Tcc.listar, name='tcc'),
    path('tcc/criar', Tcc.criar, name='tcc.criar'),
    path('tcc/editar/<id>', Tcc.editar, name='tcc.editar'),
    path('tcc/excluir/<id>', Tcc.excluir, name='tcc.excluir'),
    path('tcc/mostrar_pdf/<id>', Tcc.mostrar_pdf, name='mostrar_pdf'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    