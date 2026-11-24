from flask import Flask
from flask_caching import Cache

cache = Cache()

def create_app():
    # esta wea me va a dar problemas
    app = Flask(__name__)
        #configuración se sockest y CORS
    app.config['CACHE_TYPE'] = "SimpleCache"
        #app.config['CACHE_DEFAULT_TIMEOUT'] = 300
    
    cache.init_app(app)

    #importación de librerias
    from .controllers.ElementController import element

    #registro de los controles en el blueprint
    app.register_blueprint(element, url_prefix='/elements')

    #apartado de debug 
    #_space_debug(app, cache)
    
    return app

def _space_debug(app: Flask, cache:Cache):
    #ejecución para el caché
    @app.route('/')
    @cache.cached(timeout=60)
    def test_caching():
        return{
            "data": "algo",
            "other_data": 20
        }
