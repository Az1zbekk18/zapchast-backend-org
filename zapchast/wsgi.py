import os
import dotenv
dotenv.load_dotenv()
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zapchast.settings')

application = get_wsgi_application()