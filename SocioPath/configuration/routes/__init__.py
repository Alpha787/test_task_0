from SocioPath.configuration.routes.routes import Routes
from SocioPath.internal.routes import users, news

__routes__ = Routes(routers=(users.router, news.router))
