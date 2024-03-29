from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class EmployeeManager(BaseUserManager):
    def create_user(self, email, fullname, emp_code, mobile, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        emp = self.model(
            email=self.normalize_email(email),
            fullname=fullname,
            emp_code=emp_code,
            mobile=mobile
        )

        emp.set_password(password)
        emp.save(using=self._db)
        return emp

    def create_superuser(self, email, fullname, emp_code, mobile, password=None):
        
        emp = self.create_user(
            email,
            password=password,
            fullname=fullname,
            emp_code=emp_code,
            mobile=mobile
        )
        emp.is_admin = True
        emp.save(using=self._db)
        return emp


class Employee(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.IntegerField(max_length=11)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname","emp_code","mobile"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin