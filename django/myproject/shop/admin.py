from django.contrib import admin
from .models import Post, Article

# 방식 1
# admin.site.register(Post)

'''
# 방식 2
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'content', 'content_size10', 'content_len', 'created_at', 'updated_at']

    def content_size10(self, Post):
        return '{}'.format(Post.content[:10])

    content_size10.short_description = '일부내용'

    def content_len(self, Post):
        return '{}글자'.format(len(Post.content))
    content_len.short_description = '글자 수'

admin.site.register(Post, PostAdmin)
'''

# 방식 3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 테이블 구조로 보여준다.
    # 표시할 컬럼을 지정할 수 있다.
    list_display = ['user', 'title', 'content', 'content_size10',
                    'content_len', 'created_at', 'updated_at']
    # 상세 페이지로 이동하는 링크를 설정할 수 있다.
    list_display_links = ['user', 'title']
    # 화면에 보여줄 필드를 제한할 수 있다.
    # fields = ['title', 'content']

    # 특정 필드를 기준으로 필터 기능을 추가할 수 있다.
    list_filter = ['title']

    # 특정 필드를 기준으로 검색 기능을 추가한다.
    search_fields = ['title']

    def content_size10(self, Post):
        return '{}'.format(Post.content[:10])

    content_size10.short_description = '일부내용'

    def content_len(self, Post):
        return '{}글자'.format(len(Post.content))
    content_len.short_description = '글자 수'

def action1(self, request, queryset):
    queryset.update(status='p')

action1.short_description = '모두 p로 변경하기'

def action2(self, request, queryset):
    queryset.update(status='d')

action2.short_description = '모두 d로 변경하기'

def action3(self, request, queryset):
    queryset.update(title='Title Change..')

action3.short_description = 'Title 변경하기'

def action4(self, request, queryset):
    queryset.update(body='미세먼지 최악..')

action4.short_description = 'Body 변경하기'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', 'status']
    ordering = ['title']
    actions = [action1, action2, action3, action4]

    list_display_links = ['title', 'status']

    list_filter = ['status']

    search_fields = ['title', 'status']