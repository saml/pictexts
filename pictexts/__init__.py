import webapp2

from pictexts.views import (NewSlideshowPage)

app = webapp2.WSGIApplication([
    ('/', NewSlideshowPage),
    ], debug=True)
