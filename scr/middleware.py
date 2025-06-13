import geocoder
import logging
from django.utils import translation
from django.shortcuts import redirect
from django.urls import reverse

logger = logging.getLogger(__name__)

class GeoLanguageMiddleware:
    """
    This area needs to be fixed later because the user can select their language in the settings, not automatically.

    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get client IP address from headers or remote address
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0] or request.META.get('REMOTE_ADDR')
        
        # Example IP for testing (do not manually assign IP in production)
        test_ip = "104.252.221.255" 
        logger.debug(f"User Ip for testing: {test_ip}") 

        g = geocoder.ip(test_ip) # If you need to use the user's IP address, replace test_ip with user_ip.
        logger.debug(f"Detected country from IP: {g.country}")  

        country_code = g.country.upper() if g.country else ''

        spanish_speaking_countries = [
            'AR', 'BO', 'CL', 'CO', 'CR', 'CU', 'EC', 'SV', 'GT', 'HN', 'MX', 'NI', 'PA', 
            'PY', 'PE', 'PR', 'DO', 'UY', 'VE', 'ES'
        ]
        
        english_speaking_countries = [
            'US', 'GB', 'CA', 'AU', 'IN', 'IE', 'ZA', 'NZ', 'PH', 'JM', 'TT', 'SG'
        ]

        if country_code in spanish_speaking_countries:
            language_code = 'es'  
        elif country_code in english_speaking_countries:
            language_code = 'en'  
        else:
            language_code = 'en' 

        logger.debug(f"Language selected: {language_code}")  

        translation.activate(language_code)
        request.LANGUAGE_CODE = language_code  

        response = self.get_response(request)
        return response


class AdminLoginRequiredMiddleware:

    """ 
    Middleware that restricts access to the django admin interface to authenticated users only, 
    
    If an unauthenticated user tries to access the admin panel, they will be redirected to the login page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            if not request.user.is_authenticated:
                return redirect('login')  
        response = self.get_response(request)
        return response
