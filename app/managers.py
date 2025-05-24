from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _ 

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        # extra_fields.setdefault("is_staff", True)
        # extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
        