import abc

from django.conf import settings
from django.db import models
from django.utils import timezone




class Assignment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="assignments")
    created = models.DateTimeField(default=timezone.now)
    started = models.DateTimeField(null=True, blank=True)
    pre_reqs_completed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    recipe = models.ForeignKey("homework.Recipe")
    deliverable = models.URLField(null=True, blank=True)





    # TODO! Assignments should could some kind of deliverable...!?
    # TODO! Assignments should have some markdown instructions







    # def __unicode__(self):
    #     return "%s - %s" % (self.user, self.__class__.__name__)
    #
    # @classmethod
    # def check_user_has_completed(cls, user):
    #     try:
    #         return cls.objects.get(user=user, completed=True)
    #     except cls.DoesNotExist:
    #         return False
    #
    # def get_missing_pre_reqs(self):
    #     """Returns a list of missing pre reqs OR a message describing the problem"""
    #     if hasattr(self, "pre_reqs"):
    #         # pre_reqs are classes, like MakeGHPage
    #         missing_pre_reqs = list(filter(lambda x: not x.check_user_has_completed(self.user), self.pre_reqs))
    #     else:
    #         missing_pre_reqs = None
    #     self.pre_reqs_completed = not missing_pre_reqs
    #     self.save()
    #     return missing_pre_reqs
    #
    # @abc.abstractclassmethod
    # def do_completed_check(self):
    #     raise NotImplementedError()
