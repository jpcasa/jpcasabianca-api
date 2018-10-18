from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse

from .. import models


class MenuViewTestCase(TestCase):
    """Test suite for the Menu api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.menu_data = {
            'owner': user.id,
            'name': 'Portfolio'
        }
        self.response_menu = self.client.post(
            reverse('ListCreateMenu'),
            self.menu_data
        )

        self.menu_item_data = {
            'owner': user.id,
            'title': 'Design',
            'url': 'portfolio/design'
        }
        self.response_menu_item = self.client.post(
            reverse('ListCreateMenuItem'),
            self.menu_item_data
        )

        self.sub_menu_item_data = {
            'owner': user.id,
            'title': 'ux',
            'url': 'portfolio/design/ux'
        }
        self.response_sub_menu_item = self.client.post(
            reverse('ListCreateSubMenuItem'),
            self.sub_menu_item_data
        )


    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/menus/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_api_can_create_a_menu(self):
        """Test the api has menu creation capability."""
        self.assertEqual(
            self.response_menu.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_create_a_menu_item(self):
        """Test the api has menu item creation capability."""
        self.assertEqual(
            self.response_menu_item.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_create_a_sub_menu_item(self):
        """Test the api has sub menu item creation capability."""
        self.assertEqual(
            self.response_menu_item.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_get_a_menu(self):
        """Test the api can get a given menu."""
        menu = models.Menu.objects.get()
        response = self.client.get(
            reverse(
                'MenuDetails',
                kwargs={'pk': menu.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, menu)


    def test_api_can_update_menu(self):
        """Test the api can update a given menu."""
        menu = models.Menu.objects.get()
        change_menu = {
            'name': 'Resources'
        }
        response = self.client.put(
            reverse(
                'MenuDetails',
                kwargs={'pk': menu.id}
            ), change_menu, format='json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_api_can_delete_menu(self):
        """Test the api can delete a menu."""
        menu = models.Menu.objects.get()
        response = self.client.delete(
            reverse(
                'MenuDetails',
                kwargs={'pk': menu.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_api_can_get_a_menu_item(self):
        """Test the api can get a given menu item."""
        menu_item = models.MenuItem.objects.get()
        response = self.client.get(
            reverse(
                'MenuItemDetails',
                kwargs={'pk': menu_item.id}
            ), format="json")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, menu_item)


    def test_api_can_delete_menu_item(self):
        """Test the api can delete a menu item."""
        menu_item = models.MenuItem.objects.get()
        response = self.client.delete(
            reverse(
                'MenuItemDetails',
                kwargs={'pk': menu_item.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_api_can_get_a_sub_menu_item(self):
        """Test the api can get a given sub menu item."""
        sub_menu_item = models.SubMenuItem.objects.get()
        response = self.client.get(
            reverse(
                'SubMenuItemDetails',
                kwargs={'pk': sub_menu_item.id}
            ), format="json")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, sub_menu_item)


    def test_api_can_delete_sub_menu_item(self):
        """Test the api can delete a sub menu item."""
        sub_menu_item = models.SubMenuItem.objects.get()
        response = self.client.delete(
            reverse(
                'SubMenuItemDetails',
                kwargs={'pk': sub_menu_item.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


# Skill Views
class SkillViewTestCase(TestCase):
    """Test suite for the Skill api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.skill_chart = {
            "name": "Portfolio",
            "title1": "Something",
            "points1": 7,
            "title2": "Something",
            "points2": 7,
            "title3": "Something",
            "points3": 7,
            "title4": "Something",
            "points4": 7,
            "title5": "Something",
            "points5": 7
        }
        self.response_skill_chart = self.client.post(
            reverse('ListCreateSkillChart'),
            self.skill_chart
        )

        self.skill_category = {
            "owner": user.id,
            "name": "Frontend"
        }
        self.response_skill_category = self.client.post(
            reverse('ListCreateSkillCategory'),
            self.skill_category
        )

        self.skill = {
            "owner": user.id,
            "name": "Something",
            "logo": "Something",
            "skill_level": 7,
            "months_worked": 24,
            "last_project": "Something",
            "website": "https://www.google.com/",
            "documentation": "https://www.google.com/",
            "github": "https://www.google.com/",
            "why": "Something"
        }
        self.response_skill = self.client.post(
            reverse('ListCreateSkill'),
            self.skill
        )


    def test_api_can_create_a_skill_chart(self):
        """Test the api has skill chart creation capability."""
        self.assertEqual(
            self.response_skill_chart.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_create_a_skill_category(self):
        """Test the api has skill category creation capability."""
        self.assertEqual(
            self.response_skill_category.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_get_a_skill_chart(self):
        """Test the api can get a given skill chart."""
        skill_chart = models.SkillChart.objects.get()
        response = self.client.get(
            reverse(
                'SkillChartDetails',
                kwargs={'pk': skill_chart.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, skill_chart)


    def test_api_can_get_a_skill_category(self):
        """Test the api can get a given skill category."""
        skill_category = models.SkillCategory.objects.get()
        response = self.client.get(
            reverse(
                'SkillCategoryDetails',
                kwargs={'pk': skill_category.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, skill_category)


    def test_api_can_update_skill_chart(self):
        """Test the api can update a given skill chart."""
        skill_chart = models.SkillChart.objects.get()
        change_skill_chart = {
            "name": "Portfolio 2",
            "title1": "Something Else",
            "points1": 9,
            "title2": "Something Else",
            "points2": 9,
            "title3": "Something Else",
            "points3": 9,
            "title4": "Something Else",
            "points4": 9,
            "title5": "Something Else",
            "points5": 9
        }
        response = self.client.put(
            reverse(
                'SkillChartDetails',
                kwargs={'pk': skill_chart.id}
            ), change_skill_chart
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_api_can_update_skill_category(self):
        """Test the api can update a given skill category."""
        skill_category = models.SkillCategory.objects.get()
        change_skill_category = {
            "name": "Something",
            "url": "Something"
        }
        response = self.client.put(
            reverse(
                'SkillCategoryDetails',
                kwargs={'pk': skill_category.id}
            ), change_skill_category
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_api_can_delete_skill_chart(self):
        """Test the api can delete a skill chart."""
        skill_chart = models.SkillChart.objects.get()
        response = self.client.delete(
            reverse(
                'SkillChartDetails',
                kwargs={'pk': skill_chart.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_api_can_delete_skill_chart_category(self):
        """Test the api can delete a skill category category."""
        skill_category = models.SkillCategory.objects.get()
        response = self.client.delete(
            reverse(
                'SkillCategoryDetails',
                kwargs={'pk': skill_category.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


# Experience Views
class ExperienceViewTestCase(TestCase):
    """Test suite for the Experience api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.experience = {
            "order": 1,
            "owner": user,
            "job_title": "Something",
            "company": "Something",
            "company_logo": "Logo",
            "company_website": "https://www.google.com/",
            "start_date": "Something",
            "end_date": "Something",
            "place": "Something",
            "responsibilities": "Something",
            "achievements": "Something"
        }
        self.response_experience = self.client.post(
            reverse('ListCreateExperience'),
            self.experience
        )


    def test_api_can_create_an_experience(self):
        """Test the api has experience creation capability."""
        self.assertEqual(
            self.response_experience.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_get_an_experience(self):
        """Test the api can get a given skill chart."""
        experience = models.Experience.objects.get()
        response = self.client.get(
            reverse(
                'ExperienceDetails',
                kwargs={'pk': experience.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, experience.job_title)


    def test_api_can_update_experience(self):
            """Test the api can update a given skill chart."""
            experience = models.Experience.objects.get()
            change_experience = {
                "order": 2,
                "job_title": "Something 2",
                "company": "Something 2",
                "company_logo": "Logo 2",
                "company_website": "https://www.google.com/",
                "start_date": "Something",
                "end_date": "Something",
                "place": "Something",
                "responsibilities": "Something",
                "achievements": "Something"
            }
            response = self.client.put(
                reverse(
                    'ExperienceDetails',
                    kwargs={'pk': experience.id}
                ), change_experience
            )
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )


    def test_api_can_delete_experience(self):
            """Test the api can delete a skill chart."""
            experience = models.Experience.objects.get()
            response = self.client.delete(
                reverse(
                    'ExperienceDetails',
                    kwargs={'pk': experience.id}
                ), format='json', follow=True)
            self.assertEquals(
                response.status_code,
                status.HTTP_204_NO_CONTENT
            )


# Program Views
class ProgramViewTestCase(TestCase):
    """Test suite for the Program api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.program_category = {
            "owner": user.id,
            "name": "Something",
            "url": "Something"
        }
        self.response_program_category = self.client.post(
            reverse('ListCreateProgramCategory'),
            self.program_category
        )

        self.program = {
            "owner": user,
            "name": "Something",
            "logo": "Something",
            "skill_level": "Something",
            "website": "Something"
        }
        self.response_program = self.client.post(
            reverse('ListCreateProgram'),
            self.program
        )


    def test_api_can_create_a_program_category(self):
        """Test the api has program category creation capability."""
        self.assertEqual(
            self.response_program_category.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_create_a_program(self):
        """Test the api has program creation capability."""
        self.assertEqual(
            self.response_program.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_get_a_program_category(self):
        """Test the api can get a given category."""
        program_category = models.ProgramCategory.objects.get()
        response = self.client.get(
            reverse(
                'ProgramCategoryDetails',
                kwargs={'pk': program_category.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, program_category.name)


    def test_api_can_get_a_program(self):
        """Test the api can get a given program."""
        program = models.Program.objects.get()
        response = self.client.get(
            reverse(
                'ProgramDetails',
                kwargs={'pk': program.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, program.name)


    def test_api_can_update_program(self):
        """Test the api can update a given program."""
        program = models.Program.objects.get()
        change_program = {
            "name": "Something Else",
            "logo": "Something Else",
            "skill_level": "Something Else",
            "website": "Something Else"
        }
        response = self.client.put(
            reverse(
                'ProgramDetails',
                kwargs={'pk': program.id}
            ), change_program
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_api_can_delete_program_category(self):
        """Test the api can delete a category."""
        program_category = models.ProgramCategory.objects.get()
        response = self.client.delete(
            reverse(
                'ProgramCategoryDetails',
                kwargs={'pk': program_category.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_api_can_delete_program(self):
        """Test the api can delete a program."""
        program = models.Program.objects.get()
        response = self.client.delete(
            reverse(
                'ProgramDetails',
                kwargs={'pk': program.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


# Education Views
class EducationViewTestCase(TestCase):
    """Test suite for the Education api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.education = {
            "order": 1,
            "owner": user,
            "place": "Something",
            "place_logo": "Something",
            "description": "Logo",
            "website": "https://www.google.com/"
        }
        self.response_education = self.client.post(
            reverse('ListCreateEducation'),
            self.education
        )


    def test_api_can_create_an_education(self):
        """Test the api has experience creation capability."""
        self.assertEqual(
            self.response_education.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_get_an_education(self):
        """Test the api can get a given education."""
        education = models.Education.objects.get()
        response = self.client.get(
            reverse(
                'EducationDetails',
                kwargs={'pk': education.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, education.place)


    def test_api_can_update_education(self):
            """Test the api can update a given education."""
            education = models.Education.objects.get()
            change_education = {
                "order": 2,
                "place": "Something Else",
                "place_logo": "Something Else",
                "description": "Logo 2",
                "website": "https://www.google.com/"
            }
            response = self.client.put(
                reverse(
                    'EducationDetails',
                    kwargs={'pk': education.id}
                ), change_education
            )
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )


    def test_api_can_delete_education(self):
            """Test the api can delete a education."""
            education = models.Education.objects.get()
            response = self.client.delete(
                reverse(
                    'EducationDetails',
                    kwargs={'pk': education.id}
                ), format='json', follow=True)
            self.assertEquals(
                response.status_code,
                status.HTTP_204_NO_CONTENT
            )


# Course Views
class CourseViewTestCase(TestCase):
    """Test suite for the Course api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.course = {
            "order": 1,
            "owner": user,
            "place": "Something",
            "place_logo": "Something",
            "course_title": "Something",
            "description": "Something",
            "main_focus": "Something",
            "achievements": "Something",
            "website": "https://www.google.com/"
        }
        self.response_course = self.client.post(
            reverse('ListCreateCourse'),
            self.course
        )


    def test_api_can_create_an_course(self):
        """Test the api has experience creation capability."""
        self.assertEqual(
            self.response_course.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_get_an_course(self):
        """Test the api can get a given course."""
        course = models.Course.objects.get()
        response = self.client.get(
            reverse(
                'CourseDetails',
                kwargs={'pk': course.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, course.place)


    def test_api_can_update_course(self):
            """Test the api can update a given course."""
            course = models.Course.objects.get()
            change_course = {
                "order": 2,
                "place": "Something Else",
                "place_logo": "Something Else",
                "course_title": "Something Else",
                "description": "Something Else",
                "main_focus": "Something Else",
                "achievements": "Something Else",
                "website": "https://www.google.com/"
            }
            response = self.client.put(
                reverse(
                    'CourseDetails',
                    kwargs={'pk': course.id}
                ), change_course
            )
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )


    def test_api_can_delete_course(self):
            """Test the api can delete a course."""
            course = models.Course.objects.get()
            response = self.client.delete(
                reverse(
                    'CourseDetails',
                    kwargs={'pk': course.id}
                ), format='json', follow=True)
            self.assertEquals(
                response.status_code,
                status.HTTP_204_NO_CONTENT
            )


# Testimony Views
class TestimonyViewTestCase(TestCase):
    """Test suite for the Testimony api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.testimony = {
            "order": 1,
            "owner": user,
            "person": "Something",
            "job": "Something",
            "testimony": "Something",
            "avatar": "Something",
            "linkedin": "https://www.google.com/"
        }
        self.response_testimony = self.client.post(
            reverse('ListCreateTestimony'),
            self.testimony
        )


    def test_api_can_create_a_testimony(self):
        """Test the api has experience creation capability."""
        self.assertEqual(
            self.response_testimony.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_get_an_testimony(self):
        """Test the api can get a given testimony."""
        testimony = models.Testimony.objects.get()
        response = self.client.get(
            reverse(
                'TestimonyDetails',
                kwargs={'pk': testimony.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, testimony.person)


    def test_api_can_update_testimony(self):
            """Test the api can update a given testimony."""
            testimony = models.Testimony.objects.get()
            change_testimony = {
                "order": 2,
                "person": "Something Else",
                "job": "Something Else",
                "testimony": "Something Else",
                "avatar": "Something Else",
                "linkedin": "https://www.google.com/"
            }
            response = self.client.put(
                reverse(
                    'TestimonyDetails',
                    kwargs={'pk': testimony.id}
                ), change_testimony
            )
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )


    def test_api_can_delete_testimony(self):
            """Test the api can delete a testimony."""
            testimony = models.Testimony.objects.get()
            response = self.client.delete(
                reverse(
                    'TestimonyDetails',
                    kwargs={'pk': testimony.id}
                ), format='json', follow=True)
            self.assertEquals(
                response.status_code,
                status.HTTP_204_NO_CONTENT
            )


# Case Study Views
class CaseStudyViewTestCase(TestCase):
    """Test suite for the Case Study api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.case_study = {
            "order": 1,
            "owner": user,
            "title": "Something",
            "subtitle": "Something",
            "summary": "Something",
            "url": "https://www.google.com/",
            "html": "Something"
        }
        self.response_case_study = self.client.post(
            reverse('ListCreateCaseStudy'),
            self.case_study
        )


    def test_api_can_create_a_case_study(self):
        """Test the api has case study creation capability."""
        self.assertEqual(
            self.response_case_study.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_get_an_case_study(self):
        """Test the api can get a given case study."""
        case_study = models.CaseStudy.objects.get()
        response = self.client.get(
            reverse(
                'CaseStudyDetails',
                kwargs={'pk': case_study.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, case_study.title)


    def test_api_can_update_case_study(self):
            """Test the api can update a given case study."""
            case_study = models.CaseStudy.objects.get()
            change_case_study = {
                "order": 2,
                "title": "Something Else",
                "subtitle": "Something Else",
                "summary": "Something Else",
                "url": "https://www.google.com/",
                "html": "Something Else"
            }
            response = self.client.put(
                reverse(
                    'CaseStudyDetails',
                    kwargs={'pk': case_study.id}
                ), change_case_study
            )
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )


    def test_api_can_delete_case_study(self):
            """Test the api can delete a case study."""
            case_study = models.CaseStudy.objects.get()
            response = self.client.delete(
                reverse(
                    'CaseStudyDetails',
                    kwargs={'pk': case_study.id}
                ), format='json', follow=True)
            self.assertEquals(
                response.status_code,
                status.HTTP_204_NO_CONTENT
            )


# Resource Views
class ResourceViewTestCase(TestCase):
    """Test suite for the Resource api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.resource_category = {
            "owner": user.id,
            "name": "Something",
            "url": "Something"
        }
        self.response_resource_category = self.client.post(
            reverse('ListCreateResourceCategory'),
            self.resource_category
        )

        self.resource = {
            "owner": user,
            "reference": "Something",
            "description": "Something",
            "price": 19.99,
            "link": "https://google.com"
        }
        self.response_resource = self.client.post(
            reverse('ListCreateResource'),
            self.resource
        )


    def test_api_can_create_a_resource_category(self):
        """Test the api has resource category creation capability."""
        self.assertEqual(
            self.response_resource_category.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_create_a_resource(self):
        """Test the api has resource creation capability."""
        self.assertEqual(
            self.response_resource.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_get_a_resource_category(self):
        """Test the api can get a given category."""
        resource_category = models.ResourceCategory.objects.get()
        response = self.client.get(
            reverse(
                'ResourceCategoryDetails',
                kwargs={'pk': resource_category.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, resource_category.name)


    def test_api_can_get_a_resource(self):
        """Test the api can get a given resource."""
        resource = models.Resource.objects.get()
        response = self.client.get(
            reverse(
                'ResourceDetails',
                kwargs={'pk': resource.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, resource.reference)


    def test_api_can_update_resource(self):
        """Test the api can update a given resource."""
        resource = models.Resource.objects.get()
        change_resource = {
            "reference": "Something Else",
            "description": "Something Else",
            "price": 29.99,
            "link": "https://google.com"
        }
        response = self.client.put(
            reverse(
                'ResourceDetails',
                kwargs={'pk': resource.id}
            ), change_resource
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_api_can_delete_resource_category(self):
        """Test the api can delete a category."""
        resource_category = models.ResourceCategory.objects.get()
        response = self.client.delete(
            reverse(
                'ResourceCategoryDetails',
                kwargs={'pk': resource_category.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_api_can_delete_resource(self):
        """Test the api can delete a resource."""
        resource = models.Resource.objects.get()
        response = self.client.delete(
            reverse(
                'ResourceDetails',
                kwargs={'pk': resource.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
