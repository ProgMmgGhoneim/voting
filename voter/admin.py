from django.contrib import admin

from .models import VoterUser


@admin.register(VoterUser)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_username', 'user_email',
                    'created_at', 'updated_at', 'is_verified', 'otp_sent')
    readonly_fields = ('is_verified', 'otp_sent', 'otp_sent_date',
                       'failed_attempts', 'last_otp')
    
    def user_username(self, obj):
        return obj.user.username or 'NA'
    
    def user_email(self, obj):
        return obj.user.email or 'NA'
    
    user_username.short_description = 'username'
    user_email.short_description = 'email'