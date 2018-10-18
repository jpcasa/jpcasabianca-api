from django.shortcuts import render
from rest_framework import generics, permissions

from . import serializers
from . import models
from .permissions import IsOwner, IsOwnerMenuItem


# Menu Views
class ListCreateMenuView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner,
    )

    def perform_create(self, serializer):
        """Save the post data when creating a new menu."""
        serializer.save(owner=self.request.user)


class MenuDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner,
    )


class ListCreateMenuItemView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerMenuItem)

    def perform_create(self, serializer):
        """Save the post data when creating a new menu item."""
        serializer.save(owner=self.request.user)


class MenuItemDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ListCreateSubMenuItemView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.SubMenuItem.objects.all()
    serializer_class = serializers.SubMenuItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new menu item."""
        serializer.save(owner=self.request.user)


class SubMenuItemDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.SubMenuItem.objects.all()
    serializer_class = serializers.SubMenuItemSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Skill Views
class ListCreateSkillChartView(generics.ListCreateAPIView):
    """This class defines the create behavior for the Skill Chart Model."""
    queryset = models.SkillChart.objects.all()
    serializer_class = serializers.SkillChartSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new skill chart."""
        serializer.save()


class SkillChartDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.SkillChart.objects.all()
    serializer_class = serializers.SkillChartSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ListCreateSkillCategoryView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.SkillCategory.objects.all()
    serializer_class = serializers.SkillCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new menu item."""
        serializer.save(owner=self.request.user)


class SkillCategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.SkillCategory.objects.all()
    serializer_class = serializers.SkillCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class ListCreateSkillView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return models.Skill.objects.all().order_by('name')

    def perform_create(self, serializer):
        """Save the post data when creating a new menu item."""
        serializer.save(owner=self.request.user)


class SkillDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SearchSkills(generics.ListAPIView):
    serializer_class = serializers.SkillSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        url = self.kwargs['url']
        return models.Skill.objects.filter(category__url=url).order_by('order')


# Experience views
class ListCreateExperienceView(generics.ListCreateAPIView):
    """This class defines the create behavior for the Skill Chart Model."""
    queryset = models.Experience.objects.all()
    serializer_class = serializers.ExperienceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return models.Experience.objects.all().order_by('order')

    def perform_create(self, serializer):
        """Save the post data when creating a new skill chart."""
        serializer.save(owner=self.request.user)


class ExperienceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.Experience.objects.all()
    serializer_class = serializers.ExperienceSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Program Views
class ListCreateProgramCategoryView(generics.ListCreateAPIView):
    """This class defines the create behavior for the Skill Chart Model."""
    queryset = models.ProgramCategory.objects.all()
    serializer_class = serializers.ProgramCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new program category chart."""
        serializer.save(owner=self.request.user)


class ProgramCategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.ProgramCategory.objects.all()
    serializer_class = serializers.ProgramCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class ListCreateProgramView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.Program.objects.all()
    serializer_class = serializers.ProgramSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a program."""
        serializer.save(owner=self.request.user)


class ProgramDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.Program.objects.all()
    serializer_class = serializers.ProgramSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SearchPrograms(generics.ListAPIView):
    serializer_class = serializers.ProgramSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        url = self.kwargs['url']
        return models.Program.objects.filter(program_category__url=url)


# Education views
class ListCreateEducationView(generics.ListCreateAPIView):
    """This class defines the create behavior for the Skill Chart Model."""
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new skill chart."""
        serializer.save(owner=self.request.user)


class EducationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Course views
class ListCreateCourseView(generics.ListCreateAPIView):
    """This class defines the create behavior for the Skill Chart Model."""
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new skill chart."""
        serializer.save(owner=self.request.user)


class CourseDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)


# Testimony views
class ListCreateTestimonyView(generics.ListCreateAPIView):
    """This class defines the create behavior for the Skill Chart Model."""
    queryset = models.Testimony.objects.all()
    serializer_class = serializers.TestimonySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new skill chart."""
        serializer.save(owner=self.request.user)


class TestimonyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.Testimony.objects.all()
    serializer_class = serializers.TestimonySerializer
    permission_classes = (permissions.IsAuthenticated,)


# Case Study views
class ListCreateCaseStudyView(generics.ListCreateAPIView):
    """This class defines the create behavior for the Skill Chart Model."""
    queryset = models.CaseStudy.objects.all()
    serializer_class = serializers.CaseStudySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new skill chart."""
        serializer.save(owner=self.request.user)


class CaseStudyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.CaseStudy.objects.all()
    serializer_class = serializers.CaseStudySerializer
    permission_classes = (permissions.IsAuthenticated,)


# Resource Views
class ListCreateResourceCategoryView(generics.ListCreateAPIView):
    """This class defines the create behavior for the Skill Chart Model."""
    queryset = models.ResourceCategory.objects.all()
    serializer_class = serializers.ResourceCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new program category chart."""
        serializer.save(owner=self.request.user)


class ResourceCategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.ResourceCategory.objects.all()
    serializer_class = serializers.ResourceCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class ListCreateResourceView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a program."""
        serializer.save(owner=self.request.user)


class ResourceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer
    permission_classes = (permissions.IsAuthenticated,)
