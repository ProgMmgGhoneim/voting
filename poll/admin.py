from django.contrib import admin

from .models import Poll, Choice, Comment, Vote

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    readonly_fields = ('count',)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields =('content', 'voter', 'poll')
    
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('titile', 'description', 'expire_date', 'is_expire')
    inlines = [ChoiceInline, CommentInline]
    
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('content', 'count', 'poll')
    readonly_fields = ('count',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = readonly_fields =('content', 'voter', 'poll')
    
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'voter')
    