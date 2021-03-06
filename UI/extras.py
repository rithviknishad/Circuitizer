#!/usr/bin/python3
# Steroids for REMI
# Not python friendly !

# https://www.w3schools.com/w3css/4/w3.css
# https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css
# https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css

def lazy_load_css(self_pointer, url):
    self_pointer.execute_javascript("""
        var link = document.createElement('link')
        link.rel = 'stylesheet'
        link.href = \"""" + url + """\"
        document.getElementsByTagName('HEAD')[0].appendChild(link)
    """)


# <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
# <meta http-equiv="Pragma" content="no-cache" />
# <meta http-equiv="Expires" content="0" />

def lazy_load_http_equiv(self_pointer):
    self_pointer.execute_javascript("""
        var meta = document.createElement('meta')
        meta.http-equiv = 'Cache-Control'
        meta.content = 'no-cache, no-store, must-revalidate'
        document.getElementsByTagName('HEAD')[0].appendChild(meta)

        var meta2 = document.createElement('meta')
        meta2.http-equiv = 'Pragma'
        meta2.content = 'no-cache'
        document.getElementsByTagName('HEAD')[0].appendChild(meta2)

        var meta3 = document.createElement('meta')
        meta3.http-equiv = 'Expires'
        meta3.content = '0'
        document.getElementsByTagName('HEAD')[0].appendChild(meta3)
    """)


# https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js

def lazy_load_js(self_pointer, url):
    self_pointer.execute_javascript("""
        var js = document.createElement('script')
        js.type = 'text/javascript'
        js.src = \"""" + url + """\"
        document.getElementsByTagName('HEAD')[0].appendChild(js)
    """)

def lazy_load_js_from_data(self_pointer, data):
    self_pointer.execute_javascript("""
        var js = document.createElement('script')
        js.innerHTML = '""" + data + """'
        document.getElementsByTagName('HEAD')[0].appendChild(js)
    """)


def inject_drag_property_to_widget(self_pointer, ID):
  self_pointer.execute_javascript("dragElement(document.getElementById(\"" + ID + "\"));")
  
def inject_drag_property_to_widget_x_only(self_pointer, ID):
  self_pointer.execute_javascript("dragElementX(document.getElementById(\"" + ID + "\"));")

def inject_css(self_pointer, css):    
    self_pointer.execute_javascript("""
        var css = document.createElement('style')
        css.innerHTML = '""" + css + """'
        document.getElementsByTagName('HEAD')[0].appendChild(css)
    """)


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

