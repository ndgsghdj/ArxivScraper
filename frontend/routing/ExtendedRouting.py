from flet_route import Routing, Params, Basket
from flet import Page, View
from typing import Callable
from repath import match

def ExtendedPath(url: str, clear: bool, view: Callable[[Page, Params, Basket], View], protected: bool, middleware: Callable[[Page, Params, Basket], None] = None):
    """
    ```
    path(
        url = "/", # Here you have to give that url which will call your view on mach
        clear = True, # If you want to clear all the routes you have passed so far, then pass True otherwise False.
        view = IndexView # Here you have to pass a function or method which will take page and params and return ft.View
        protected = True # Here you have to pass a boolean value to indicate whether the route is protected by authentication
    )
    ```
    """
    return [url, clear, view, protected, middleware]

def route_str(route):
    if type(route) == str:
        return route
    else:
        return str(route.route)

class ExtendedRouting(Routing):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__middleware = kwargs.get("middleware", None)
        self.__params = Params({})
        self.__basket = Basket()
    
    def change_route(self, route):
        not_found = True
        for url in self.app_routes:
            path_match = match(url[0], self.page.route)
            if path_match:
                self.__params = Params(path_match.groupdict())
                if self.__middleware != None:
                    self.__middleware(  # call main middleware
                        page=self.page,
                        params=self.__params,
                        basket=self.__basket
                    )
                # if change route using main middleware recall change route
                if self.page.route != route_str(route=route):
                    self.page.go(self.page.route)
                    return
                
                # check if route is protected
                if url[3]:
                    if not self.page.session.get("authenticated"):
                        self.page.go("/login")
                        return

                if url[4] != None:
                    url[4](  # call url middleware
                        page=self.page,
                        params=self.__params,
                        basket=self.__basket
                    )

                # if change route using url middleware recall change route
                if self.page.route != route_str(route=route):
                    self.page.go(self.page.route)
                    return

                if url[1]:
                    self.page.views.clear()
                view = url[2](
                    page=self.page,
                    params=self.__params,
                    basket=self.__basket
                )
                view.appbar = self.appbar
                view.navigation_bar = self.navigation_bar
                self.page.views.append(
                    view
                )
                not_found = False
                break
        if not_found:
            self.__params = Params({"url": self.page.route})
            self.page.views.append(
                self.not_found_view(
                    page=self.page,
                    params=self.__params,
                    basket=self.__basket
                )
            )
        self.page.update()