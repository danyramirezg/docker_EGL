from django.urls import path, include
from frontapp.views import root, landing, login, logout, register, snake, topic
from frontapp.views import user_config, select_word, activate


urlpatterns = [
            path('', root.root, name='root'),
            path('landing', landing.landing, name='landing'),
            path('login', login.login, name='login'),
            path('logout', logout.logout, name='logout'),
            path('register', register.register, name='register'),
            path('snake', snake.snake, name='snake'),
            path('topic', topic.topic, name='topic'),
            path('user_config', user_config.user_config, name='user_config'),
            path('select_word', select_word.select_word, name='select_word'),
            path('activate/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',
                activate.activate, name='activate'),
        ]
