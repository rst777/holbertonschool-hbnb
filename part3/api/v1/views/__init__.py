#!/usr/bin/python3
"""Initialize views package"""

from flask import Blueprint

# Define the Blueprint instance for all views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import specific routes after defining the Blueprint to avoid circular imports
from api.v1.views.users import *
from api.v1.views.places_reviews import *
from api.v1.views.places import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
