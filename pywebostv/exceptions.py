# -*- coding: utf-8 -*-

class WebOSException(Exception):
    pass

class WebOSAnswerException(WebOSException):
    def __init__(self, message, response):
        super(WebOSException, self).__init__(message)
        self.response = response

