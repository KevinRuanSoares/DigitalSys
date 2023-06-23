import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from user.choices import PROFILE_CHOICES

class UserManager(BaseUserManager):
    def create_user(self, nickname, password=None):
        if not nickname:
            raise ValueError('Users must have an nickname address')
        user = self.model(
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, password):
        user = self.create_user(
            nickname,
            password=password,
        )
        user.admin = 'ADMIN'
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    objects = UserManager()
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    nickname = models.CharField(max_length=50, null=False, blank=False, unique=True)
    active = models.BooleanField(default=True)
    profile = models.CharField(max_length=10, choices=PROFILE_CHOICES, default='USER')

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'users'

    def is_staff(self, perm, obj=None):
        return self.profile == 'ADMIN'
        
    def has_perm(self, perm, obj=None):
        return self.profile == 'ADMIN'

    def has_module_perms(self, app_label):
        return self.profile == 'ADMIN'