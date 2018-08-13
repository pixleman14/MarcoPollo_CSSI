import webapp2
import jinja2
import os
import logging

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Home(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/index.html')
        self.response.write(mypage.render())

class Food(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/index-5.html')
        self.response.write(mypage.render())

class Outlets(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/index-4.html')
        self.response.write(mypage.render())

class Photo(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/index-3.html')
        self.response.write(mypage.render())

class Recreation(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/index-2.html')
        self.response.write(mypage.render())

app = webapp2.WSGIApplication([
    ('/', Home),#1
    ('/Food', Food),#5
    ('/Outlets', Outlets),#4
    ('/Photo', Photo),#3
    ('/Recreation', Recreation),#2
], debug=True)
