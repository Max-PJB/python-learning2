from sanic import Sanic, Blueprint
from sanic.response import text

app = Sanic(__name__)
blueprint_1 = Blueprint("blueprint_1", url_prefix="/bp1")
blueprint_2 = Blueprint("blueprint_2", url_prefix="/bp2", version=4,
                        version_prefix="/h", )
group = Blueprint.group(
    blueprint_1,
    blueprint_2,
    version=1,
    version_prefix="/api/v",
    url_prefix="/grouped",
    strict_slashes=True,
)
primary = Blueprint.group(group, url_prefix="/primary")


@blueprint_1.route("/")
def blueprint_1_default_route(request):
    return text("BP1_OK")


@blueprint_2.route("/")
def blueprint_2_default_route(request):
    return text("BP2_OK")


app.blueprint(group)
app.blueprint(primary)
app.blueprint(blueprint_1)

# The mounted paths:
# /api/v1/grouped/bp1/
# /api/v1/grouped/bp2/
# /api/v1/primary/grouped/bp1
# /api/v1/primary/grouped/bp2
# /bp1

app.run()
