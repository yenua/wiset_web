from django.contrib import admin
from django.urls import path
# index는 대문, board는 게시판
from main.views import *

app_name='main'

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('', index, name='index'),
    # URL:80/board에 접속하면 board 페이지 + URL이름은 board이다
    path('board/', board, name='board'),
    # URL:80/board/숫자로 접속하면 게시글-세부페이지(posting)
    path('board/<int:pk>/', posting, name="posting"),
    path('board/new_post/', new_post),
    path('board/<int:pk>/remove/', remove_post),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)