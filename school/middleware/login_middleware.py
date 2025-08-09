from django.shortcuts import redirect

Login_Exampt_Urls=[
    
    'accounts/api/v1/login/<str:role>/',
    'accounts/api/v1/register/<str:role>/'
]

class Login:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request,*args,**kwargs):
        if not request.user.is_authenticated and request.path not in Login_Exampt_Urls:
            return redirect("accounts:api-v1:user-login",kwargs.get("role"))
        response = self.get_response(request)
        return response
        
        