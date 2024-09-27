from django.db import models

# Create your models here.
# admin에 Post 페이지 추가
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    #자동으로 작성 시각과 수정 시각 저장
    updated_at = models.DateTimeField(auto_now=True)
    # author : 추후예정


    def __str__(self):
        return f'[{self.pk}]{self.title}'