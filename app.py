from flask import Flask

def create_app():
    app = Flask(__name__)

    # Uygulama yapılandırması
    app.config['DEBUG'] = True

    # Gerekirse mavi baskın ekleyin, modüllerinizi ve diğer bileşenleri kaydedin

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
