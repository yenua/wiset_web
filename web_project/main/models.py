from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname