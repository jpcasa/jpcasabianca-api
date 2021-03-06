from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

from . import views


urlpatterns = {
    path('auth/',
        include('rest_framework.urls',
        namespace='rest_framework')
    ),
    path(
        'menus/',
        views.ListCreateMenuView.as_view(),
        name="ListCreateMenu"
    ),
    path(
        'menus/<int:pk>/',
        views.MenuDetailsView.as_view(),
        name="MenuDetails"
    ),
    path(
        'menu-items/',
        views.ListCreateMenuItemView.as_view(),
        name="ListCreateMenuItem"
    ),
    path(
        'menu-items/<int:pk>/',
        views.MenuItemDetailsView.as_view(),
        name="MenuItemDetails"
    ),
    path(
        'sub-menu-items/',
        views.ListCreateSubMenuItemView.as_view(),
        name="ListCreateSubMenuItem"
    ),
    path(
        'sub-menu-items/<int:pk>/',
        views.SubMenuItemDetailsView.as_view(),
        name="SubMenuItemDetails"
    ),
    path(
        'skill-charts/',
        views.ListCreateSkillChartView.as_view(),
        name="ListCreateSkillChart"
    ),
    path(
        'skill-charts/<int:pk>/',
        views.SkillChartDetailsView.as_view(),
        name="SkillChartDetails"
    ),
    path(
        'skill-categories/',
        views.ListCreateSkillCategoryView.as_view(),
        name="ListCreateSkillCategory"
    ),
    path(
        'skill-categories/<int:pk>/',
        views.SkillCategoryDetailsView.as_view(),
        name="SkillCategoryDetails"
    ),
    path(
        'skills/',
        views.ListCreateSkillView.as_view(),
        name="ListCreateSkill"
    ),
    path(
        'skills/<int:pk>/',
        views.SkillDetailsView.as_view(),
        name="SkillDetails"
    ),
    path(
        'skills/search/<url>/',
        views.SearchSkills.as_view(),
        name="SearchSkills"
    ),
    path(
        'experiences/',
        views.ListCreateExperienceView.as_view(),
        name="ListCreateExperience"
    ),
    path(
        'experiences/<int:pk>/',
        views.ExperienceDetailsView.as_view(),
        name="ExperienceDetails"
    ),
    path(
        'program-categories/',
        views.ListCreateProgramCategoryView.as_view(),
        name="ListCreateProgramCategory"
    ),
    path(
        'program-categories/<int:pk>/',
        views.ProgramCategoryDetailsView.as_view(),
        name="ProgramCategoryDetails"
    ),
    path(
        'programs/',
        views.ListCreateProgramView.as_view(),
        name="ListCreateProgram"
    ),
    path(
        'programs/<int:pk>/',
        views.ProgramDetailsView.as_view(),
        name="ProgramDetails"
    ),
    path(
        'programs/search/<url>/',
        views.SearchPrograms.as_view(),
        name="SearchPrograms"
    ),
    path(
        'education/',
        views.ListCreateEducationView.as_view(),
        name="ListCreateEducation"
    ),
    path(
        'education/<int:pk>/',
        views.EducationDetailsView.as_view(),
        name="EducationDetails"
    ),
    path(
        'courses/',
        views.ListCreateCourseView.as_view(),
        name="ListCreateCourse"
    ),
    path(
        'courses/<int:pk>/',
        views.CourseDetailsView.as_view(),
        name="CourseDetails"
    ),
    path(
        'testimonies/',
        views.ListCreateTestimonyView.as_view(),
        name="ListCreateTestimony"
    ),
    path(
        'testimonies/<int:pk>/',
        views.TestimonyDetailsView.as_view(),
        name="TestimonyDetails"
    ),
    path(
        'case-studies/',
        views.ListCreateCaseStudyView.as_view(),
        name="ListCreateCaseStudy"
    ),
    path(
        'case-studies/<int:pk>/',
        views.CaseStudyDetailsView.as_view(),
        name="CaseStudyDetails"
    ),
    path(
        'resource-categories/',
        views.ListCreateResourceCategoryView.as_view(),
        name="ListCreateResourceCategory"
    ),
    path(
        'resource-categories/<int:pk>/',
        views.ResourceCategoryDetailsView.as_view(),
        name="ResourceCategoryDetails"
    ),
    path(
        'resources/',
        views.ListCreateResourceView.as_view(),
        name="ListCreateResource"
    ),
    path(
        'resources/<int:pk>/',
        views.ResourceDetailsView.as_view(),
        name="ResourceDetails"
    ),
    path(
        'get-token/',
        obtain_auth_token
    ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
