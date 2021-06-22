from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField
)


class Question(Model):
    subject = CharField(max_length=200)
    content = TextField()
    created_datetime = DateTimeField()
