from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from blog.forms import BlogUserChangeForm, BlogUserCreationForm
from blog.models import BlogUser, Category, Article, About, Contact, Social


# Register your models here.
class BlogUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field

    form = BlogUserChangeForm
    add_form = BlogUserCreationForm

    fieldsets = ((_('User'), {'fields': ('username', 'email', 'password')}),
                 (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
                 (_('Permissions'),
                  {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                 (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
                 )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category_name",)}


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(BlogUser, BlogUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Social)
admin.site.register(About)
admin.site.register(Contact)