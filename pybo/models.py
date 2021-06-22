from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    ForeignKey,
    CASCADE
)


class Question(Model):
    subject = CharField(max_length=200)
    content = TextField()
    created_datetime = DateTimeField()

class Answer(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    content = TextField()
    created_datetime = DateTimeField