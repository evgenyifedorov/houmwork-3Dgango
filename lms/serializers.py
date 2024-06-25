from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True, source='lesson_set')
    lesson_count = SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self,object):
        if object.lesson_set.count():
            return object.lesson_set.count()
        return 0


