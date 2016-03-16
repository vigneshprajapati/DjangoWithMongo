from __future__ import unicode_literals

from django.db import models
from mongoengine import Document, EmbeddedDocument
from mongoengine import fields
# Create your models here.
import datetime


class Person(Document):
    first_name = fields.StringField()
    last_name =fields.StringField()


