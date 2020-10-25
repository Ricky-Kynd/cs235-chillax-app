from flask import Blueprint, render_template

import chillax.utilities.utilities as utilities
import chillax.news.services as news_utilities


home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',
        selected_articles=utilities.get_selected_articles(),
        tag_urls=utilities.get_tags_and_urls()
    )
