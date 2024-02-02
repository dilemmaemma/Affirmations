from flask import Blueprint

private_routes_bp = Blueprint('private_routes', __name__)
public_routes_bp = Blueprint('public_routes', __name__)
dev_tools_bp = Blueprint('dev_tools', __name__)

from .private_affirmation_routes import *
from .public_affirmation_routes import *
from .dev_tools_bp import *