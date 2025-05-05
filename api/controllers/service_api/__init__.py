from flask import Blueprint

from libs.external_api import ExternalApi

bp = Blueprint("service_api", __name__, url_prefix="/v1")
api = ExternalApi(bp)

# 索引
from . import index

# 租户 app service
from .app import (
    annotation,
    app,
    audio,
    completion,
    conversation,
    file,
    message,
    workflow,
)

# 租户数据集
from .dataset import dataset, document, hit_testing, metadata, segment, upload_file

# 租户可以使用的模型
from .workspace import models
