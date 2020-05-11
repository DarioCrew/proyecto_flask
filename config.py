class Config:
    SECRET_KEY = 'codigofacilito'
# ETAPA DE DESARROLLO 
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:tritubot2018@localhost/project_web'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'darioalex127@gmail.com'
    MAIL_PASSWORD = 'chilechile1'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:tritubot2018@localhost/project_web_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'test': TestConfig
}