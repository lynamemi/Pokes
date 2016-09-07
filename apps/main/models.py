from __future__ import unicode_literals
from ..loginreg.models import User
from django.db import models

# Create your models here.
class Pokes(models.Model):
	sender = models.ForeignKey('loginreg.User', models.DO_NOTHING, related_name="senderspoke")
	receiver = models.ForeignKey('loginreg.User', models.DO_NOTHING, related_name ="receiverspoke")
	pokes = models.IntegerField(null=True)
	created_at = models.DateTimeField(blank=True, null=True)
	updated_at = models.DateTimeField(blank=True, null=True)
	#function python calls when it tries to display object
	# def __repr__(self):
	# 	return "{} poked {}".format(self.sender.name, self.receiver.name)