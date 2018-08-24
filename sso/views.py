import logging

from django.views.generic.base import RedirectView

# Create your views here.

logger = logging.getLogger('awx.sso.views')


class BaseRedirectView(RedirectView):

    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        return '/admin'


class CompleteView(BaseRedirectView):

    def dispatch(self, request, *args, **kwargs):
        response = super(CompleteView, self).dispatch(request, *args, **kwargs)
        if self.request.user and self.request.user.is_authenticated():
            print(u"User %s log ged in" % self.request.user.username)
            print("current request user: {}".format(str(self.request.user)))
            response.set_cookie('userLoggedIn', 'true')
            response.set_cookie('current_user', self.request.user.username)
        return response


sso_complete = CompleteView.as_view()