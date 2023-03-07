from django.db import models

# Create your models here.
from django.db import models
class Board(models.Model) :
    title = models.CharField(max_length=200, verbose_name='글 제목', help_text='*최목은 최대 100자 이내')
    author = models.TextField(max_length=100, verbose_name='글쓴이')
    content = models.TextField(verbose_name='글 내용')
    published_date = models.DateTimeField(auto_now=True, verbose_name='등록(수정)일')
    def __str__(self):
    #__str__()  함수는 객체가 생성되면 문자열로 반활해주는 함수, title(제목)반환환하도록 지정함
        return self.title
