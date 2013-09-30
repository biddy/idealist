from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.managers import QueryManager
from model_utils.models import TimeStampedModel


class Title(TimeStampedModel):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='titles')
    slug = models.SlugField(max_length=255, blank=True, default='')
    

class Node(TimeStampedModel):
    STATUS=Choices(u'new',u'improved')

    user = models.ForeignKey(User, related_name='nodes')
    inherit = models.IntegerField()
    content = models.TextField()
    status = StatusField()
    title = models.ForeignKey(Title)
    slug = models.SlugField(max_length=255, blank=True, default='')

    objects = models.Manager()
    new = QueryManager(status=u'new').order_by(u'-modified')
    improved = QueryManager(status=u'improved').order_by(u'-modified')

    def __unicode__(self):
        return '%s' % (self.user)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Node, self).save(*args, **kwargs)

