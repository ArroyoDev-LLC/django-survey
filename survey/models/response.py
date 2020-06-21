# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

import swapper

Survey = swapper.get_model_name("survey", "Survey")

try:
    from django.conf import settings

    if settings.AUTH_USER_MODEL:
        user_model = settings.AUTH_USER_MODEL
    else:
        user_model = User
except (ImportError, AttributeError):
    user_model = User


class BaseResponse(models.Model):
    """
        A Response object is a collection of questions and answers with a
        unique interview uuid.
    """

    created = models.DateTimeField(_("Creation date"), auto_now_add=True)
    updated = models.DateTimeField(_("Update date"), auto_now=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name=_("Survey"), related_name="responses")
    user = models.ForeignKey(user_model, on_delete=models.SET_NULL, verbose_name=_("User"), null=True, blank=True)
    interview_uuid = models.CharField(_("Interview unique identifier"), max_length=36)

    class Meta:
        verbose_name = _("Set of answers to surveys")
        verbose_name_plural = _("Sets of answers to surveys")
        abstract = True

    def __str__(self):
        _, concrete_name = swapper.split(swapper.get_model_name("survey", "Response"))
        msg = "{} to {} by {}".format(concrete_name, self.survey, self.user)
        msg += " on {}".format(self.created)
        return msg


class Response(BaseResponse):
    class Meta(BaseResponse.Meta):
        swappable = swapper.swappable_setting("survey", "Response")
