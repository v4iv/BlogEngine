from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _

from BlogEngine.settings import AUTH_USER_MODEL


# Create your models here.
class BlogUserManager(BaseUserManager):
    def _create_user(self, username, first_name, last_name, email, password, is_staff, is_superuser,
                     **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        now = timezone.now()

        if not email:
            raise ValueError('Email is Required!')
        if not username:
            raise ValueError('Username is Required!')

        email = self.normalize_email(email)
        user = self.model(username=username, first_name=first_name, last_name=last_name, email=email,
                          is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, first_name, last_name, email, password=None, **extra_fields):
        return self._create_user(username, first_name, last_name, email, password, False, False, **extra_fields)

    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        return self._create_user(username, first_name, last_name, email, password, True, True, **extra_fields)


class BlogUser(AbstractBaseUser, PermissionsMixin):
    """
    A Custom User model with admin-compliant Permissions.

    First Name, Last Name and Email are required.
    """
    username = models.CharField(_('Username'), max_length=15, unique=True,
                                help_text="Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only.")
    email = models.EmailField(_('Email Address'), max_length=254, unique=True)
    first_name = models.CharField(_('First Name'), max_length=30)
    last_name = models.CharField(_('Last Name'), max_length=30)
    is_staff = models.BooleanField(_('Staff Status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('Active'), default=True,
                                    help_text='Designates whether this user should be treated as'
                                              'active. Unselect this instead of deleting accounts')
    date_joined = models.DateTimeField(_('Date Joined'), default=timezone.now)
    objects = BlogUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
        """
        Full Name.
        :return: Returns the first_name plus the last_name, with space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Short Name.
        :return: Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        :param subject: Subject of the mail.
        :param message:  Message content of the mail.
        :param from_email: the senders email.
        """
        send_mail(subject, message, from_email, [self.email])


class Category(models.Model):
    """
        Model describing article category.
    """

    creator = models.ForeignKey(AUTH_USER_MODEL)
    category_name = models.CharField(
        _('Category Name'), max_length=100, unique=True)
    slug = models.SlugField()
    category_desc = models.CharField(_('Category Description'), max_length=254)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def get_absolute_url(self):
        return "/%s/" % urlquote(self.slug)

    def create(self):
        """
        Saves the created category with timestamp.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.category_name


class Article(models.Model):
    """
    Model describing article.
    """
    author = models.ForeignKey(AUTH_USER_MODEL)
    title = models.CharField(max_length=140)
    slug = models.SlugField()
    subtitle = models.CharField(max_length=254, blank=True, null=True)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='uploads/')
    content = models.TextField()
    featured = models.BooleanField(default=False)
    meta = models.TextField(blank=True, null=True)
    last_edited = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    def get_absolute_url(self):
        return "/%s/" % urlquote(self.slug)

    def publish(self):
        """
        Publishes the article with timestamp.
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class About(models.Model):
    """
    Model describing about page.
    """
    title = models.CharField(max_length=254)
    about_content = models.TextField()
    about_image = models.ImageField(upload_to="uploads/")
    about_image_active = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    email_active = models.BooleanField(default=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    contact_number_active = models.BooleanField(default=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    address_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Social(models.Model):
    icon = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    url = models.URLField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Model describing contact form.
    """
    fullname = models.CharField(max_length=254)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fullname
