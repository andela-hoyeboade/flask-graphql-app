from app.models import db
from app.views import app

db.init_app(app)
app.run(debug=True)
