import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dq#gpof#)4en6hbxj)k!syq3pihtw(fi(ijm57s9g%_@9xco&&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quiz',
]

# In your settings.py

JAZZMIN_SETTINGS = {
    # General settings
    "site_title": "QuizMaster Admin",
    "site_header": "QuizMaster Administration",
    "site_brand": "QuizMaster",
    "site_logo": None,
    "welcome_sign": "Welcome to QuizMaster Admin Panel",
    "copyright": "QuizMaster Inc.",
    "search_model": ["auth.User", "quiz.Quiz"],
    
    # UI Configuration
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": ['auth.group'],
    "order_with_respect_to": [
        'quiz',
        'quiz.QuizCategory',
        'quiz.Quiz', 
        'quiz.Question',
        'quiz.Answer',
        'quiz.QuizAttempt',
        'quiz.UserAnswer',
        'auth.user'
    ],
    
    # Custom icons
    "icons": {
        # Quiz models
        "quiz.quizcategory": "fas fa-tags",
        "quiz.quiz": "fas fa-question-circle",
        "quiz.question": "fas fa-question",
        "quiz.answer": "fas fa-check-circle",
        "quiz.quizattempt": "fas fa-clipboard-list",
        "quiz.useranswer": "fas fa-user-check",
        
        # Auth models
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    
    # UI tweaks
    "related_modal_active": True,
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible", 
        "auth.group": "vertical_tabs"
    },
}

JAZZMIN_UI_TWEAKS = {
    # Color themes
    "theme": "darkly",
    "dark_mode_theme": "cyborg",
    
    # Navbar
    "navbar": "navbar-dark",
    "navbar_fixed": True,
    "navbar_small_text": False,
    "brand_colour": "navbar-primary",
    "no_navbar_border": False,
    
    # Sidebar
    "sidebar": "sidebar-dark-primary",
    "sidebar_fixed": True,
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    
    # Footer
    "footer_fixed": False,
    "footer_small_text": False,
    
    # Body
    "body_small_text": False,
    "brand_small_text": False,
    
    # Buttons
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    
    # Misc
    "actions_sticky_top": True,
    "accent": "accent-primary",
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'quizapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'quizapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Add this if you want to use sessions for tracking quiz attempts
SESSION_COOKIE_AGE = 3600  # 1 hour
