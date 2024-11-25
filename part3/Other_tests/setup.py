from setuptools import setup, find_packages

setup(
    name='hbnb',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask==2.0.1',
        'Flask-Cors==3.0.10',
        'flask-sqlalchemy==2.5.1',
        'SQLAlchemy==1.4.23',
        'mysqlclient==2.0.3',
        'python-dotenv==0.19.0',
        'gunicorn==20.1.0'
    ],
    python_requires='>=3.6',
)