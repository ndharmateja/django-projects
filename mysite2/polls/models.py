from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    Model,
)


# Create your models here.
class Question(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField("date published")


    def __str__(self):
        return self.question_text


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text
