from django.contrib.auth.models import User
from django.db import models
from ccg_archive.cyberpunk_ccg_archive.models import Card, Image


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)


class SubmittedCard(Notification):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.card.approved


class SubmittedImage(Notification):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.approved
