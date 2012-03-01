import webapp2
import jinja2
from pictexts.settings import (TEMPLATE_DIR, ASSETS_BASEPATH)

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

def get_template_vars():
    return {
        'ASSETS_BASEPATH': ASSETS_BASEPATH
    }

class NewSlideshowPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('slideshow_form.html')
        var = get_template_vars()
        var['title'] = 'New Slideshow'
        self.response.out.write(template.render(var))


