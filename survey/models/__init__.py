# -*- coding: utf-8 -*-

"""
Permit to import everything from survey.models without knowing the details.
"""

import swapper

Category, Answer, Response, Survey, Question = swapper.get_model_names(
    "survey", ["Category", "Answer", "Response", "Survey", "Question"]
)

__all__ = ["Category", "Answer", "Response", "Survey", "Question"]
