"""
Factories for Program Enrollment tests.
"""


from uuid import uuid4

import factory
from factory.django import DjangoModelFactory
from opaque_keys.edx.keys import CourseKey

from lms.djangoapps.program_enrollments import models
from student.tests.factories import CourseEnrollmentFactory, UserFactory


class ProgramEnrollmentFactory(DjangoModelFactory):
    """ A Factory for the ProgramEnrollment model. """
    class Meta(object):
        model = models.ProgramEnrollment

    user = factory.SubFactory(UserFactory)
    external_user_key = None
    program_uuid = factory.LazyFunction(uuid4)
    curriculum_uuid = factory.LazyFunction(uuid4)
    status = 'enrolled'


PROGRAM_COURSE_ENROLLMENT_DEFAULT_COURSE_KEY = (
    CourseKey.from_string("course-v1:edX+DemoX+Demo_Course")
)


class ProgramCourseEnrollmentFactory(DjangoModelFactory):
    """ A factory for the ProgramCourseEnrollment model. """
    class Meta(object):
        model = models.ProgramCourseEnrollment

    program_enrollment = factory.SubFactory(ProgramEnrollmentFactory)
    course_enrollment = factory.SubFactory(CourseEnrollmentFactory)
    course_key = factory.LazyAttribute(
        lambda pce: (
            pce.course_enrollment.course_id
            if pce.course_enrollment
            else PROGRAM_COURSE_ENROLLMENT_DEFAULT_COURSE_KEY
        )
    )
    status = 'active'
