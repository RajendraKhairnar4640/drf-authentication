This mini project includes BasicAuthentication, SessionAuthentication, TokenAuthentication,customAuthentication, and RemoteUserAuthentication

1. Basic Authentication:-

This authentication scheme uses HTTP Basic Authentication, signed against a user's username and password. Basic authentication is generally only appropriate for testing.

If successfully authenticated, BasicAuthentication provides the following credentials.

request.user will be a Django User instance.
request.auth will be None.
Unauthenticated responses that are denied permission will result in an HTTP 401 Unauthorized response with an appropriate WWW-Authenticate header. For example:WWW-Authenticate: Basic realm="api"
Note- check the settings.py file for DEFAULT_AUTHENTICATION_CLASSES and add the authentication classes and permission classes in the class of API.
EX- class EmployeeView(APIView):
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated,IsAdminUser]
    permission_classes=[AllowAny]
    permission_classes=[IsAdminUser]
    permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
