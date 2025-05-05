from configs import dify_config
from dify_app import DifyApp


def init_app(app: DifyApp):
    # register blueprint routers

    from flask_cors import CORS  # type: ignore

    from controllers.console import bp as console_app_bp
    from controllers.files import bp as files_bp
    from controllers.inner_api import bp as inner_api_bp
    from controllers.service_api import bp as service_api_bp
    from controllers.web import bp as web_bp

    ''' 服务租户路由组 '''
    CORS(
        service_api_bp,
        allow_headers=["Content-Type", "Authorization", "X-App-Code"],
        methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    )
    app.register_blueprint(service_api_bp)

    CORS(
        web_bp,
        resources={
            r"/*": {"origins": dify_config.WEB_API_CORS_ALLOW_ORIGINS}
        },  # 指定哪些源（origin）可以访问该资源
        supports_credentials=True,  # 可以在跨域请求中携带 cookies 或其他认证信息
        allow_headers=["Content-Type", "Authorization", "X-App-Code"],
        methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
        expose_headers=["X-Version", "X-Env"],  # 指定可以读取的额外响应头
    )

    app.register_blueprint(web_bp)

    ''' admin 控制台路由组 '''
    CORS(
        console_app_bp,
        resources={r"/*": {"origins": dify_config.CONSOLE_CORS_ALLOW_ORIGINS}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
        expose_headers=["X-Version", "X-Env"],
    )

    app.register_blueprint(console_app_bp)

    CORS(
        files_bp,
        allow_headers=["Content-Type"],
        methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    )
    app.register_blueprint(files_bp)

    app.register_blueprint(inner_api_bp)
