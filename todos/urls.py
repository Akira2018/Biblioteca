from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from todos.views import home, signup  # Importe as funções home e signup do módulo todos.views
from django.contrib.auth.views import LogoutView  # Importe a view de logout padrão do Django
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),  # Corrigido o caminho da página de login
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),    # Outras rotas do seu aplicativo...
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticação padrão do Django
    path('accounts/login/', LoginView.as_view(), name='login'),  # Definição explícita da URL de logi
    path('', home),
    path('logout/', LogoutView.as_view(), name='logout'),  # Configuração da rota de logout

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






