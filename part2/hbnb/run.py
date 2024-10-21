from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
    
@app.before_first_request
def list_routes():
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule} -> {rule.methods}")
