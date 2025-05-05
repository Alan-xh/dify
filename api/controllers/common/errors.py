#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   errors.py
@Time    :   2025/04/21 23:43:48
@Author  :   Alan_xh
@Version :   1.0
@Desc    :   定义公共错误
'''

from werkzeug.exceptions import HTTPException


class FilenameNotExistsError(HTTPException):
    code = 400
    description = "The specified filename does not exist."


class RemoteFileUploadError(HTTPException):
    code = 400
    description = "Error uploading remote file."
