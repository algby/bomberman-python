import json
import httplib, urllib
from bomberman.error import BadRequest
from bomberman.error import Unauthorized
from bomberman.error import InternalServerError
from bomberman.connection import Connection

class Client(object):
  def __init__(self):
    self.conn = Connection()

  def is_profane(self, corpus):
    params = urllib.urlencode({'corpus': corpus})
    self.conn.request("GET", "/v1/profanity/check?%s" % params, headers=self.conn.headers)
    resp = self.conn.getresponse()
    if resp.status == 200:
      profane = resp.read()
      self.conn.close()
      return (profane == "1")
    else:
      self.conn.close()
      self.__raise_exception(resp.status)

  def censor(self, corpus, replacement_text="***"):
    params = urllib.urlencode({'corpus': corpus, 'replacement_text': replacement_text})
    self.conn.request("GET", "/v1/profanity/censor?%s" % params, headers=self.conn.headers)
    resp = self.conn.getresponse()
    if resp.status == 200:
      data = json.loads(resp.read())
      self.conn.close()
      return data['censored_text']
    else:
      self.conn.close()
      self.__raise_exception(resp.status)

  def highlight(self, corpus, start_tag="<strong>", end_tag="</strong>"):
    params = urllib.urlencode({'corpus': corpus, 'start_tag': start_tag, 'end_tag': end_tag})
    self.conn.request("GET", "/v1/profanity/highlight?%s" % params, headers=self.conn.headers)
    resp = self.conn.getresponse()
    if resp.status == 200:
      data = json.loads(resp.read())
      self.conn.close()
      return data['highlighted_text']
    else:
      self.conn.close()
      self.__raise_exception(resp.status)

  def __raise_exception(self, code):
    if code == 400:
      raise BadRequest
    elif code == 401:
      raise Unauthorized
    elif code == 500:
      raise InternalServerError
    else:
      raise Exception("Bomberman returned error code %s" % code)
