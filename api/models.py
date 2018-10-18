from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models

# MENU MODELS
class SubMenuItem(models.Model):
    """This class represents the Submenu Item model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='submenuitems',
        on_delete=models.CASCADE
    )
    order = models.IntegerField(
        blank=False,
        default=0
    )
    title = models.CharField(
        blank=False,
        max_length=100
    )
    url = models.CharField(
        blank=False,
        max_length=100,
        unique=True
    )
    action = models.CharField(
        blank=False,
        max_length=100,
        default="push"
    )
    subtitle = models.CharField(
        blank=True,
        max_length=100
    )
    icon = models.CharField(
        blank=True,
        max_length=100
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.title)


class MenuItem(models.Model):
    """This class represents the Menu Item model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='menuitems',
        on_delete=models.CASCADE
    )
    order = models.IntegerField(
        blank=False,
        default=0
    )
    title = models.CharField(
        blank=False,
        max_length=100
    )
    url = models.CharField(
        blank=True,
        max_length=100
    )
    action = models.CharField(
        max_length=100,
        default="push"
    )
    sub_menu_items = models.ManyToManyField(
        SubMenuItem,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.title)


class Menu(models.Model):
    """This class represents the Menu model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='menus',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        blank=False,
        max_length=100,
        unique=True
    )
    menu_items = models.ManyToManyField(
        MenuItem,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.name)


# SKILLS MODELS
class SkillChart(models.Model):
    """This class represents the Skill Chart model."""
    name = models.CharField(
        blank=False,
        max_length=535
    )
    title1 = models.CharField(
        blank=False,
        max_length=535
    )
    points1 = models.IntegerField(
        blank=False,
        default=0
    )
    title2 = models.CharField(
        blank=False,
        max_length=535
    )
    points2 = models.IntegerField(
        blank=False,
        default=0
    )
    title3 = models.CharField(
        blank=False,
        max_length=535
    )
    points3 = models.IntegerField(
        blank=False,
        default=0
    )
    title4 = models.CharField(
        blank=False,
        max_length=535
    )
    points4 = models.IntegerField(
        blank=False,
        default=0
    )
    title5 = models.CharField(
        blank=False,
        max_length=535
    )
    points5 = models.IntegerField(
        blank=False,
        default=0
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.name)


class SkillCategory(models.Model):
    """This class represents the Skill Category model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='skill_categories',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        blank=False,
        max_length=100,
        unique=True
    )
    url = models.CharField(
        blank=True,
        max_length=100
    )
    message = models.TextField(
        blank=True
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.name)


class Skill(models.Model):
    """This class represents the Skill model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='skills',
        on_delete=models.CASCADE
    )
    order = models.IntegerField(
        blank=False,
        default=0
    )
    category = models.ManyToManyField(
        SkillCategory,
        blank=True
    )
    name = models.CharField(
        blank=False,
        max_length=100,
        unique=True
    )
    logo = models.CharField(
        blank=False,
        max_length=535
    )
    skill_level = models.IntegerField(
        blank=False,
        default=0
    )
    months_worked = models.IntegerField(
        blank=False,
        default=0
    )
    last_project = models.CharField(
        blank=False,
        max_length=535
    )
    skill_chart = models.ForeignKey(
        SkillChart,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    website = models.URLField(
        blank=False
    )
    documentation = models.URLField(
        blank=False
    )
    github = models.URLField(
        blank=False
    )
    why = models.CharField(
        blank=False,
        max_length=535
    )
    preferred = models.BooleanField(
        default=False
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.name)


# EXPERIENCE MODELS
class Experience(models.Model):
    """This class represents the Experience model."""
    order = models.IntegerField(
        blank=False
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='experiences',
        on_delete=models.CASCADE
    )
    job_title = models.CharField(
        blank=False,
        max_length=255
    )
    company = models.CharField(
        blank=False,
        max_length=255
    )
    start_date = models.CharField(
        blank=False,
        max_length=255
    )
    end_date = models.CharField(
        blank=False,
        max_length=255
    )
    place = models.CharField(
        blank=False,
        max_length=255
    )
    summary = models.CharField(
        blank=False,
        max_length=255
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{} @{}".format(self.job_title, self.company)


# Program Models
class ProgramCategory(models.Model):
    """This class represents the Program Category model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='prgram_categories',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        blank=False,
        max_length=255
    )
    url = models.CharField(
        blank=False,
        max_length=255
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.name)


class Program(models.Model):
    """This class represents the Program model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='programs',
        on_delete=models.CASCADE
    )
    program_category = models.ForeignKey(
        ProgramCategory,
        null=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        blank=False,
        max_length=255
    )
    logo = models.CharField(
        blank=False,
        max_length=255
    )
    summary = models.CharField(
        blank=False,
        max_length=255,
        default=""
    )
    website = models.CharField(
        blank=False,
        max_length=255
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.name)


# Education Models
class Education(models.Model):
    """This class represents the Education model."""
    order = models.IntegerField(
        blank=False
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='educations',
        on_delete=models.CASCADE
    )
    place = models.CharField(
        blank=False,
        max_length=255
    )
    place_logo = models.CharField(
        blank=False,
        max_length=255
    )
    description = models.CharField(
        blank=False,
        max_length=255
    )
    website = models.URLField(
        blank=False
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.place)


class Course(models.Model):
    """This class represents the Course model."""
    order = models.IntegerField(
        blank=False
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='courses',
        on_delete=models.CASCADE
    )
    place = models.CharField(
        blank=False,
        max_length=255
    )
    place_logo = models.CharField(
        blank=False,
        max_length=255
    )
    course_title = models.CharField(
        blank=False,
        max_length=255
    )
    description = models.CharField(
        blank=False,
        max_length=255
    )
    main_focus = models.TextField(
        blank=False
    )
    website = models.URLField(
        blank=False
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{} - {}".format(self.course_title, self.place)


class Testimony(models.Model):
    """This class represents the Testimony model."""
    order = models.IntegerField(
        blank=False
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='testimonies',
        on_delete=models.CASCADE
    )
    person = models.CharField(
        blank=False,
        max_length=255
    )
    job = models.CharField(
        blank=False,
        max_length=255
    )
    testimony = models.CharField(
        blank=False,
        max_length=255
    )
    avatar = models.CharField(
        blank=False,
        max_length=255
    )
    linkedin = models.URLField(
        blank=False
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{} - {}".format(self.person, self.job)


class CaseStudy(models.Model):
    """This class represents the CaseStudy model."""
    order = models.IntegerField(
        blank=False
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='case_studies',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        blank=False,
        max_length=255
    )
    subtitle = models.CharField(
        blank=False,
        max_length=255
    )
    summary = models.CharField(
        blank=False,
        max_length=535
    )
    cta = models.CharField(
        blank=False,
        max_length=255,
        default="View More"
    )
    url = models.CharField(
        blank=False,
        max_length=255
    )
    tags = models.CharField(
        blank=True,
        max_length=255
    )
    coming_soon = models.BooleanField(
        default=False
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.title)


# Resource Models
class ResourceCategory(models.Model):
    """This class represents the Resource Category model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='resource_categories',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        blank=False,
        max_length=255
    )
    url = models.CharField(
        blank=False,
        max_length=255
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.name)


class Resource(models.Model):
    """This class represents the Resource model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='resources',
        on_delete=models.CASCADE
    )
    resource_category = models.ForeignKey(
        ResourceCategory,
        null=True,
        on_delete=models.CASCADE
    )
    reference = models.CharField(
        blank=False,
        max_length=255
    )
    description = models.CharField(
        blank=False,
        max_length=255
    )
    price = models.FloatField(
        blank=False
    )
    link = models.URLField(
        blank=False
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.reference)


# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
