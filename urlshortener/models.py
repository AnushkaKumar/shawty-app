from django.db import models
import string
from datetime import datetime,timedelta
from django.utils import timezone
\
_char_map = string.ascii_letters+string.digits

def index_to_char(sequence):
    return "".join([_char_map[x] for x in sequence])


class Link(models.Model):
    link = models.URLField()
    hits = models.IntegerField(default=0)
    short = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    expiry = models.IntegerField(default = 30)

    def __repr__(self):
        return "<Link (Hits %s): %s>"%(self.hits, self.link)

    def get_short_id(self):
        _id = self.id
        digits = []
        while _id > 0:
            rem = _id % 62
            digits.append(rem)
            _id //= 62
        digits.reverse()
        return index_to_char(digits)

    @staticmethod
    def decode_id(string):
        i = 0
        for c in string:
            i = i * 64 + _char_map.index(c)
        return i

    def is_expired(self):
    	print (self.created+timedelta(seconds = self.expiry))
    	print (timezone.now())
    	if self.created+timedelta(seconds = self.expiry) < timezone.now(): 
    		return True
    	return False