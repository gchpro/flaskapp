from app import create_app
import config

app = create_app(config.MDCONFIG)
app.run(debug=True)
