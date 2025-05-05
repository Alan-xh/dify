import logging
import time

from configs import dify_config
from contexts.wrapper import RecyclableContextVar
from dify_app import DifyApp


# ----------------------------
# Application Factory Function
# ----------------------------
def create_flask_app_with_configs() -> DifyApp:
    """
    create a raw flask app
    with configs loaded from .env file
    """
    dify_app = DifyApp(__name__)
    dify_app.config.from_mapping(dify_config.model_dump())

    # add before request hook
    # 应用上下文添加线程记录
    @dify_app.before_request
    def before_request():
        # add an unique identifier to each request
        RecyclableContextVar.increment_thread_recycles()

    return dify_app


def create_app() -> DifyApp:
    start_time = time.perf_counter()
    app = create_flask_app_with_configs()
    initialize_extensions(app)
    end_time = time.perf_counter()
    if dify_config.DEBUG:
        logging.info(
            f"Finished create_app ({round((end_time - start_time) * 1000, 2)} ms)"
        )
    return app


def initialize_extensions(app: DifyApp):
    '''加载应用所有拓展'''
    from extensions import (
        ext_app_metrics,  # response添加时间4
        ext_blueprints,  # (**)routes
        ext_celery,  # 加载配置 celery
        ext_code_based_extension,  # 动态导入可拓展性文件模块
        ext_commands,  # 加载命令行
        ext_compress,  # 配置 response数据压缩
        ext_database,  # 数据库初始化
        ext_hosting_provider,  # 加载云服务提供商
        ext_import_modules,  # 加载模块
        ext_logging,  # 配置日志
        ext_login,  # 加载 flask登入
        ext_mail,  # 初始化邮箱功能
        ext_migrate,  # 数据库迁移
        ext_otel,  # 初始化 OpenTelemetry 可观测性
        ext_proxy_fix,  # 反代理配置，以防反代理解析错误
        ext_redis,  # 初始化redis
        ext_sentry,  # 初始化 sentry_sdk 错误监控
        ext_set_secretkey,  # 设置密匙，防止 cookie签名被恶意串改
        ext_storage,  # 初始化云存储
        ext_timezone,  # 时区配置
        ext_warnings,  # 警告级别配置
    )

    extensions = [
        ext_app_metrics,
        ext_blueprints,
        ext_celery,
        ext_code_based_extension,
        ext_commands,
        ext_compress,
        ext_database,
        ext_hosting_provider,
        ext_import_modules,
        ext_logging,
        ext_login,
        ext_mail,
        ext_migrate,
        ext_otel,
        ext_proxy_fix,
        ext_redis,
        ext_sentry,
        ext_set_secretkey,
        ext_storage,
        ext_timezone,
        ext_warnings,
    ]
    for ext in extensions:
        short_name = ext.__name__.split(".")[-1]
        is_enabled = ext.is_enabled() if hasattr(ext, "is_enabled") else True
        if not is_enabled:
            if dify_config.DEBUG:
                logging.info(f"Skipped {short_name}")
            continue

        start_time = time.perf_counter()
        ext.init_app(app)
        end_time = time.perf_counter()
        if dify_config.DEBUG:
            logging.info(
                f"Loaded {short_name} ({round((end_time - start_time) * 1000, 2)} ms)"
            )


def create_migrations_app():
    app = create_flask_app_with_configs()
    from extensions import ext_database, ext_migrate

    # Initialize only required extensions
    ext_database.init_app(app)
    ext_migrate.init_app(app)

    return app
