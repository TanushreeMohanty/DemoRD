import os  # ADD THIS AT THE TOP
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- PRODUCTION READY SETTINGS ---
# 1. Get SECRET_KEY from environment or use a fallback for local dev
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-key')

# 2. Set DEBUG to False in production
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# 3. Allow Render URL and Localhost
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOSTS', '127.0.0.1'),
    'localhost',
    '.onrender.com' # This allows any Render subdomain
]

# --- APP CONFIG ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # ADD THIS for static files on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Keep this above CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

# ... (Templates, Auth, and Internationalization stay the same as your snippet) ...

# --- STATIC FILES ---
# Add this for Render to serve CSS/Images correctly
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- CORS ---
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
"https://demo-rd.vercel.app",]