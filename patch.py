from gevent import monkey as gmonkey

gmonkey.patch_all(thread=False, select=False)
