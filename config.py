import os

class Config:
    '''
    General configuration parent class
    '''

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key=61415eb7ca5606cc8564387dc89de335'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):

    pass


class DevConfig(Config):
    
    DEBUG = True

#Dictionary for configurations
config_options = {
'development':DevConfig,
'production':ProdConfig
} 