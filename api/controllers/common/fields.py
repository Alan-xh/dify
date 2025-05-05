#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   fields.py
@Time    :   2025/04/21 23:45:55
@Author  :   Alan_xh
@Version :   1.0
@Desc    :   注册各种 restful 字段类型
'''


from flask_restful import fields  # type: ignore

parameters__system_parameters = {
    "image_file_size_limit": fields.Integer,
    "video_file_size_limit": fields.Integer,
    "audio_file_size_limit": fields.Integer,
    "file_size_limit": fields.Integer,
    "workflow_file_upload_limit": fields.Integer,
}

parameters_fields = {
    "opening_statement": fields.String,
    "suggested_questions": fields.Raw,
    "suggested_questions_after_answer": fields.Raw,
    "speech_to_text": fields.Raw,
    "text_to_speech": fields.Raw,
    "retriever_resource": fields.Raw,
    "annotation_reply": fields.Raw,
    "more_like_this": fields.Raw,
    "user_input_form": fields.Raw,
    "sensitive_word_avoidance": fields.Raw,
    "file_upload": fields.Raw,
    "system_parameters": fields.Nested(parameters__system_parameters),
}
