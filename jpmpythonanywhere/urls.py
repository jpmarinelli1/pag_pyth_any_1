"""
URL configuration for jpmpythonanywhere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from jpmpythonanywhere.views import inicio, ejemplos, agro, spub, mgba, agro_presupuestolp, agro_erdos, agro_dashb, nube, alta_usuario, exit
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio ),
    path("ejemplos/", ejemplos ),
    path("agro/", agro ),
    path("spub/", spub ),
    path("mgba/", mgba ),
    path("agro_preslp/", agro_presupuestolp),
    path("agro_erdos/", agro_erdos ),
    path("agro_dashb/", agro_dashb ),
    path("nubepal/", nube ),
    path("register/", alta_usuario),
    path("logout/",exit),
    path("accounts/",include('django.contrib.auth.urls')),

]
