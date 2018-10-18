from rest_framework import serializers

from . import models

# Menu Serializers
class SubMenuItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Menu Item Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.SubMenuItem
        fields = (
            'owner',
            'order',
            'id',
            'title',
            'url',
            'action',
            'subtitle',
            'icon',
            'created_at',
            'modified_at',
        )
        read_only_fields = (
            'created_at',
            'modified_at',
        )


class MenuItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Menu Item Model instance into JSON format."""
    sub_menu_items = SubMenuItemSerializer(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.MenuItem
        fields = (
            'owner',
            'order',
            'id',
            'title',
            'url',
            'action',
            'sub_menu_items',
            'created_at',
            'modified_at',
        )
        read_only_fields = (
            'created_at',
            'modified_at',
        )


class MenuSerializer(serializers.ModelSerializer):
    """Serializer to map the Menu Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')
    menu_items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Menu
        fields = (
            'owner',
            'id',
            'name',
            'menu_items',
            'created_at',
            'modified_at',
        )
        read_only_fields = (
            'created_at',
            'modified_at',
        )


# Skill serializers
class SkillChartSerializer(serializers.ModelSerializer):
    """Serializer to map the Skill Chart Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.SkillChart
        fields = (
            'id',
            'name',
            'title1',
            'points1',
            'title2',
            'points2',
            'title3',
            'points3',
            'title4',
            'points4',
            'title5',
            'points5',
        )


class SkillCategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Skill Category Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.SkillCategory
        fields = (
            'id',
            'name',
            'url',
            'message'
        )


class SkillSerializer(serializers.ModelSerializer):
    """Serializer to map the Menu Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')
    # category = SkillCategorySerializer(many=True, read_only=True)
    skill_chart = SkillChartSerializer(read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Skill
        fields = (
            'owner',
            'id',
            'order',
            'category',
            'name',
            'logo',
            'skill_level',
            'months_worked',
            'last_project',
            'skill_chart',
            'website',
            'documentation',
            'github',
            'why',
            'preferred',
        )


# Experience serializers
class ExperienceSerializer(serializers.ModelSerializer):
    """Serializer to map the Experience Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Experience
        fields = (
            'order',
            'owner',
            'id',
            'job_title',
            'company',
            'start_date',
            'end_date',
            'place',
            'summary'
        )


# Program serializers
class ProgramCategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Skill Chart Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.ProgramCategory
        fields = (
            'id',
            'owner',
            'name',
            'url',
        )


class ProgramSerializer(serializers.ModelSerializer):
    """Serializer to map the Menu Model instance into JSON format."""
    # program_category = ProgramCategorySerializer(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Program
        fields = (
            'id',
            'owner',
            'program_category',
            'name',
            'logo',
            'summary',
            'website',
        )


# Experience serializers
class EducationSerializer(serializers.ModelSerializer):
    """Serializer to map the Education Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Education
        fields = (
            'order',
            'owner',
            'id',
            'place',
            'place_logo',
            'description',
            'website',
        )


# Course serializers
class CourseSerializer(serializers.ModelSerializer):
    """Serializer to map the Course Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Course
        fields = (
            'order',
            'owner',
            'id',
            'place',
            'place_logo',
            'course_title',
            'description',
            'main_focus',
            'website',
        )


# Testimony serializers
class TestimonySerializer(serializers.ModelSerializer):
    """Serializer to map the Testimony Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Testimony
        fields = (
            'order',
            'owner',
            'id',
            'person',
            'job',
            'testimony',
            'avatar',
            'linkedin',
        )


# Case Study serializers
class CaseStudySerializer(serializers.ModelSerializer):
    """Serializer to map the CaseStudy Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.CaseStudy
        fields = (
            'order',
            'owner',
            'id',
            'title',
            'subtitle',
            'summary',
            'cta',
            'url',
            'tags',
            'coming_soon',
        )


# Resource serializers
class ResourceCategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Resource Category Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.ResourceCategory
        fields = (
            'id',
            'owner',
            'name',
            'url',
        )


class ResourceSerializer(serializers.ModelSerializer):
    """Serializer to map the Resource Model instance into JSON format."""
    resource_category = ResourceCategorySerializer(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Resource
        fields = (
            'id',
            'owner',
            'resource_category',
            'reference',
            'description',
            'price',
            'link',
        )
