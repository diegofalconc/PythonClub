from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.meeting=Meeting(meetingtitle='Test Review')

    def test_string(self):
        self.assertEqual(str(self.meeting), 'Test Review')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.minute=MeetingMinutes(minutes='243')

    def test_string(self):
        self.assertEqual(str(self.minute), '243')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.resource=Resource(resourcename='check')

    def test_string(self):
        self.assertEqual(str(self.resource), 'check')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.event=Event(eventtitle='Party')

    def test_string(self):
        self.assertEqual(str(self.event), 'Party')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')