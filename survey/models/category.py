# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

import swapper

Survey = swapper.get_model_name("survey", "Survey")


class BaseCategory(models.Model):
    name = models.CharField(_("Name"), max_length=400)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name=_("Survey"), related_name="categories")
    order = models.IntegerField(_("Display order"), blank=True, null=True)
    description = models.CharField(_("Description"), max_length=2000, blank=True, null=True)

    class Meta:
        # pylint: disable=too-few-public-methods
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        abstract = True

    def __str__(self):
        return self.name

    def slugify(self):
        return slugify(str(self))


class Category(BaseCategory):
    class Meta(BaseCategory.Meta):
        swappable = swapper.swappable_setting("survey", "Category")
