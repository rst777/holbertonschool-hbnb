from app import create_app
from app.api.v1 import blueprint as api_v1_blueprint

app = create_app()

app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

def list_routes():
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule} -> {rule.methods}")

list_routes()

if __name__ == '__main__':
    app.run(debug=True)
