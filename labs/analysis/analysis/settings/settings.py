class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SEED = 49
    BASE_PATH = '../data/'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True