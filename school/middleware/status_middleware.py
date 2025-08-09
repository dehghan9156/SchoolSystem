from django.conf import settings
import jwt 
from rest_framework.response import Response
from jwt.exceptions import ExpiredSignatureError,InvalidTokenError
import jwt 
from django.contrib.auth import get_user_model
import logging
from school.models import Logs

logger = logging.getLogger('django')
User = get_user_model()


class StatusApi:
    def __init__(self,get_response):
        self.get_response = get_response 
    
    def __call__(self,request):
        username="Anonymous"
        user = None
        path_user = request.path
        auth_header = request.headers.get("Authorization")
        
        if auth_header and auth_header.startswith("Bearer "):
            token_str = auth_header.split(" ")[1]
            
            try :
                token = jwt.decode(token_str, settings.SECRET_KEY, algorithms=["HS256"])
                user_id = token.get("user_id")
                user = User.objects.get(pk=user_id)
                username = user.username
                
            except ExpiredSignatureError:
                logger.warning("jwt token has expired")
            except InvalidTokenError:
                logger.warning("jwt token is invalid")
            except Exception as e:
                logger.error(f"Error decoding JWT token:{e}")

        response = self.get_response(request)

        if response.status_code >= 500:
            log_type = "critical"
        elif response.status_code >= 400:
            log_type = "error"
        else:
            log_type = "info"

        logger.info(f"{username} called {path_user}")
        Logs.objects.create(user=user,path=path_user,type_log="info")
        return response

        










