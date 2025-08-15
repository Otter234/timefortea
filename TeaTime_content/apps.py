from django.apps import AppConfig

'''
class RenderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'render'
'''

class TeaTimeContentConfig(AppConfig):  # ✅ rename class
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TeaTime_content'            # ✅ match your app folder name exactly
