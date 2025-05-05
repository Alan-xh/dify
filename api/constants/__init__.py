#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2025/04/21 23:26:58
@Author  :   Alan_xh
@Version :   1.0
@Desc    :   常量配置
'''


from configs import dify_config

HIDDEN_VALUE = "[__HIDDEN__]"
UUID_NIL = "00000000-0000-0000-0000-000000000000"

DEFAULT_FILE_NUMBER_LIMITS = 3

IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "webp", "gif", "svg"]
IMAGE_EXTENSIONS.extend([ext.upper() for ext in IMAGE_EXTENSIONS])

VIDEO_EXTENSIONS = ["mp4", "mov", "mpeg", "mpga"]
VIDEO_EXTENSIONS.extend([ext.upper() for ext in VIDEO_EXTENSIONS])

AUDIO_EXTENSIONS = ["mp3", "m4a", "wav", "webm", "amr"]
AUDIO_EXTENSIONS.extend([ext.upper() for ext in AUDIO_EXTENSIONS])


if dify_config.ETL_TYPE == "Unstructured":
    DOCUMENT_EXTENSIONS = [
        "txt",
        "markdown",
        "md",
        "mdx",
        "pdf",
        "html",
        "htm",
        "xlsx",
        "xls",
    ]
    DOCUMENT_EXTENSIONS.extend(
        ("doc", "docx", "csv", "eml", "msg", "pptx", "xml", "epub")
    )
    if dify_config.UNSTRUCTURED_API_URL:
        DOCUMENT_EXTENSIONS.append("ppt")
    DOCUMENT_EXTENSIONS.extend([ext.upper() for ext in DOCUMENT_EXTENSIONS])
else:
    DOCUMENT_EXTENSIONS = [
        "txt",
        "markdown",
        "md",
        "mdx",
        "pdf",
        "html",
        "htm",
        "xlsx",
        "xls",
        "docx",
        "csv",
    ]
    DOCUMENT_EXTENSIONS.extend([ext.upper() for ext in DOCUMENT_EXTENSIONS])
