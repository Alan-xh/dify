#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2025/04/21 23:27:22
@Author  :   Alan_xh
@Version :   1.0
@Desc    :   上下文
'''


from contextvars import ContextVar  # 上下文变量，异步环境中是独立的
from threading import Lock
from typing import TYPE_CHECKING  # 在类型检查器中是 True，默认 False

from contexts.wrapper import RecyclableContextVar

if TYPE_CHECKING:
    from core.model_runtime.entities.model_entities import AIModelEntity
    from core.plugin.entities.plugin_daemon import PluginModelProviderEntity
    from core.tools.plugin_tool.provider import PluginToolProviderController
    from core.workflow.entities.variable_pool import VariablePool


tenant_id: ContextVar[str] = ContextVar("tenant_id")

workflow_variable_pool: ContextVar["VariablePool"] = ContextVar(
    "workflow_variable_pool"
)

"""
为了避免 gunicorn 线程回收导致的​​竞争条件，使用 RecyclableContextVar 来替换
"""
plugin_tool_providers: RecyclableContextVar[
    dict[str, "PluginToolProviderController"]
] = RecyclableContextVar(ContextVar("plugin_tool_providers"))

plugin_tool_providers_lock: RecyclableContextVar[Lock] = RecyclableContextVar(
    ContextVar("plugin_tool_providers_lock")
)

plugin_model_providers: RecyclableContextVar[
    list["PluginModelProviderEntity"] | None
] = RecyclableContextVar(ContextVar("plugin_model_providers"))

plugin_model_providers_lock: RecyclableContextVar[Lock] = RecyclableContextVar(
    ContextVar("plugin_model_providers_lock")
)

plugin_model_schema_lock: RecyclableContextVar[Lock] = RecyclableContextVar(
    ContextVar("plugin_model_schema_lock")
)

plugin_model_schemas: RecyclableContextVar[dict[str, "AIModelEntity"]] = (
    RecyclableContextVar(ContextVar("plugin_model_schemas"))
)
