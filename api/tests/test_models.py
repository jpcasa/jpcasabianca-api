from django.test import TestCase
from django.contrib.auth.models import User

from .. import models


class MenuModelTestCase(TestCase):
    """This class defines the test suite for the Menu model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.name = "Main Menu"
        self.menu = models.Menu(
            name=self.name,
            owner=user
        )

        self.title = "About Me"
        self.menu_item = models.MenuItem(
            title=self.title,
            owner=user
        )

        self.sub_title = "Short Bio"
        self.sub_menu_item = models.SubMenuItem(
            title=self.sub_title,
            owner=user
        )


    def test_model_can_create_a_menu(self):
        """Test the Menu model can create a menu."""
        old_count = models.Menu.objects.count()
        self.menu.save()
        new_count = models.Menu.objects.count()
        self.assertNotEqual(old_count, new_count)


    def test_model_can_create_a_menu_item(self):
        """Test the MenuItem model can create a menu item."""
        old_count = models.MenuItem.objects.count()
        self.menu_item.save()
        new_count = models.MenuItem.objects.count()
        self.assertNotEqual(old_count, new_count)


    def test_model_can_create_a_sub_menu_item(self):
        """Test the SubMenuItem model can create a submenu item."""
        old_count = models.SubMenuItem.objects.count()
        self.sub_menu_item.save()
        new_count = models.SubMenuItem.objects.count()
        self.assertNotEqual(old_count, new_count)


    def test_menu_can_add_item(self):
        """Test the Menu model can add a menu item."""
        self.menu.save()
        self.menu_item.save()
        old_count = self.menu.menu_items.count()
        self.menu.menu_items.add(self.menu_item)
        new_count = self.menu.menu_items.count()
        self.assertNotEqual(old_count, new_count)


    def test_menu_item_can_add_a_sub_item(self):
        """Test the Menu model can add a sub menu item."""
        self.menu_item.save()
        self.sub_menu_item.save()
        old_count = self.menu_item.sub_menu_items.count()
        self.menu_item.sub_menu_items.add(self.sub_menu_item)
        new_count = self.menu_item.sub_menu_items.count()
        self.assertNotEqual(old_count, new_count)


class SkillModelTestCase(TestCase):
    """This class defines the test suite for the Skill model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.name = "Vue.js"
        self.skill_chart = models.SkillChart(
            name=self.name,
            title1="Title 1",
            points1=8,
            title2="Title 2",
            points2=8,
            title3="Title 3",
            points3=8,
            title4="Title 4",
            points4=8,
            title5="Title 5",
            points5=8,
        )

        self.skill_category = models.SkillCategory(
            owner=user,
            name="Frontend",
            url="frontend"
        )

        self.skill = models.Skill(
            owner=user,
            name="Vue.js",
            logo="img",
            skill_level=8,
            months_worked=24,
            last_project="Website",
            website="https://www.google.com/",
            documentation="https://www.google.com/",
            github="https://www.google.com/",
            why="Title 5",
        )


    def test_model_can_create_a_skill_chart(self):
        """Test the Skill Chart model can create a skill chart."""
        old_count = models.SkillChart.objects.count()
        self.skill_chart.save()
        new_count = models.SkillChart.objects.count()
        self.assertNotEqual(old_count, new_count)


    def test_model_can_create_a_skill_category(self):
        """Test the Skill model can create a skill category."""
        old_count = models.SkillCategory.objects.count()
        self.skill_category.save()
        new_count = models.SkillCategory.objects.count()
        self.assertNotEqual(old_count, new_count)


    def test_model_can_create_a_skill(self):
        """Test the Skill model can create a skill."""
        old_count = models.Skill.objects.count()
        self.skill.save()
        new_count = models.Skill.objects.count()
        self.assertNotEqual(old_count, new_count)


# Experience Models
class ExperienceModelTestCase(TestCase):
    """This class defines the test suite for the Experience model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.experience = models.Experience(
            order=1,
            owner=user,
            job_title="Developer",
            company="Codesign",
            company_logo="img",
            company_website="website",
            start_date="March",
            end_date="December",
            place="Bogotá, Colombia",
            responsibilities="Responsibilities",
            achievements="Achievements"
        )


    def test_model_can_create_an_experience(self):
        """Test the Menu model can create an experience."""
        old_count = models.Experience.objects.count()
        self.experience.save()
        new_count = models.Experience.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(str(self.experience),
            "{} @{}".format(
                self.experience.job_title,
                self.experience.company
        ))


# Program Models
class ProgramModelTestCase(TestCase):
    """This class defines the test suite for the Program model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.program_category = models.ProgramCategory(
            owner=user,
            name="Sales",
            url="sales"
        )

        self.program = models.Program(
            owner=user,
            name="Developer",
            logo="Codesign",
            skill_level="img",
            website="website"
        )


    def test_model_can_create_a_program_category(self):
        """Test the Menu model can create an program category."""
        old_count = models.ProgramCategory.objects.count()
        self.program_category.save()
        new_count = models.ProgramCategory.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(str(self.program_category), self.program_category.name)


    def test_model_can_create_a_program(self):
        """Test the Menu model can create an program."""
        old_count = models.Program.objects.count()
        self.program.save()
        new_count = models.Program.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(str(self.program), self.program.name)


# Education Models
class EducationModelTestCase(TestCase):
    """This class defines the test suite for the Education model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.education = models.Education(
            order=1,
            owner=user,
            place="Sales",
            place_logo="sales",
            description="Description",
            website="https://www.google.com/"
        )

    def test_model_can_create_a_education(self):
        """Test the Menu model can create an education category."""
        old_count = models.Education.objects.count()
        self.education.save()
        new_count = models.Education.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(str(self.education), self.education.place)


# Course Models
class CourseModelTestCase(TestCase):
    """This class defines the test suite for the Course model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.course = models.Course(
            order=1,
            owner=user,
            place="Sales",
            place_logo="sales",
            course_title="Description",
            description="Something",
            main_focus="Something",
            achievements="Something",
            website="https://www.google.com/"
        )

    def test_model_can_create_a_course(self):
        """Test the Menu model can create an course category."""
        old_count = models.Course.objects.count()
        self.course.save()
        new_count = models.Course.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(str(self.course),
            "{} - {}".format(self.course.course_title, self.course.place))


# Testimony Models
class TestimonyModelTestCase(TestCase):
    """This class defines the test suite for the Testimony model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.testimony = models.Testimony(
            order=1,
            owner=user,
            person="Sales",
            job="sales",
            testimony="Description",
            avatar="Something",
            linkedin="https://www.google.com/"
        )


    def test_model_can_create_a_testimony(self):
        """Test the Menu model can create an testimony category."""
        old_count = models.Testimony.objects.count()
        self.testimony.save()
        new_count = models.Testimony.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(str(self.testimony),
            "{} - {}".format(self.testimony.person, self.testimony.job))


# Case Study Models
class CaseStudyModelTestCase(TestCase):
    """This class defines the test suite for the Case Study model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.case_study = models.CaseStudy(
            order=1,
            owner=user,
            title="Something",
            subtitle="Something",
            summary="Something",
            url="https://www.google.com/",
            html="<h1>Hello World</h1>"
        )


    def test_model_can_create_a_testimony(self):
        """Test the Case Study model can create an testimony category."""
        old_count = models.CaseStudy.objects.count()
        self.case_study.save()
        new_count = models.CaseStudy.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(str(self.case_study), self.case_study.title)


# Case Study Models
class ResourceModelTestCase(TestCase):
    """This class defines the test suite for the Resource model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.resource_category = models.ResourceCategory(
            owner=user,
            name="Sales",
            url="sales"
        )

        self.resource = models.Resource(
            owner=user,
            reference="Developer",
            description="Codesign",
            price=19.99,
            link="https://google.com"
        )


    def test_model_can_create_a_resource_category(self):
        """Test the Menu model can create an resource category."""
        old_count = models.ResourceCategory.objects.count()
        self.resource_category.save()
        new_count = models.ResourceCategory.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(str(self.resource_category),
            self.resource_category.name)


    def test_model_can_create_a_resource(self):
        """Test the Menu model can create an resource."""
        old_count = models.Resource.objects.count()
        self.resource.save()
        new_count = models.Resource.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(str(self.resource), self.resource.reference)


class Test(TestCase):
    """Example Test."""

    def test_something(self):
        """Test Something."""
        self.assertEqual(0, 0, 'message')
