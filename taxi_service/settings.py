"""
Django settings for taxi_service project.
Generated by 'django-admin startproject' using Django 5.1.3.
For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7u9chh0v05m0msx6axi-rwxx7p!$atm^u(@b-p9^u(srq0o-&$"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
