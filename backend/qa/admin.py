from django.contrib import admin
from .models import Conversation, Question

# Register your admins here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['title', 'user__email']
    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'conversation', 'created_at', 'is_helpful']  # Removed 'user'
    list_filter = ['created_at', 'is_helpful']
    search_fields = ['question_text', 'answer_text']
    
    # Optional: If you want to show the user, add a method
    def get_user(self, obj):
        return obj.conversation.user if obj.conversation else None
    get_user.short_description = 'User'
    
    # Then you can add 'get_user' to list_display if needed:
    # list_display = ['question_text', 'get_user', 'conversation', 'created_at', 'is_helpful']