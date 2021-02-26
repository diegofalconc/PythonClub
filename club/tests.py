from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import ResourceForm, MeetingForm
from django.urls import reverse_lazy, reverse

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

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
         self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
         self.type=Resource.objects.create(resourcename='resource', resourcetype='check', url='http://www.lenovo.com', dateentered=datetime.date(2021,1,10), userid=self.test_user, description="bam")

    def test_redirect_if_not_logged_in(self):
         response = self.client.get(reverse('newresource'))
         self.assertRedirects(response, '/accounts/login/?next=/club/newresource/')

class New_Meeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=Meeting.objects.create(meetingtitle='newtitle', meetingdate=datetime.date(2021,1,10), meetingtime=12, location="scooby", agenda="fasf")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newmeeting/')

    #    resourcename = models.CharField(max_length = 255)
    # resourcetype = models.CharField(max_length = 255)
    # url = models.URLField()
    # dateentered = models.DateField()
    # userid = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    # description = models.TextField()