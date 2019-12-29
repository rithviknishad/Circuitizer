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


def enable_drag_property(self_pointer):
  lazy_load_js_from_data(self_pointer, """function dragElement(e){var n=0,t=0,o=0,u=0;function l(e){(e=e||window.event).preventDefault(),o=e.clientX,u=e.clientY,document.onmouseup=m,document.onmousemove=d}function d(l){(l=l||window.event).preventDefault(),n=o-l.clientX,t=u-l.clientY,o=l.clientX,u=l.clientY,e.style.top=e.offsetTop-t+"px",e.style.left=e.offsetLeft-n+"px"}function m(){document.onmouseup=null,document.onmousemove=null}document.getElementById(e.id+"header")?document.getElementById(e.id+"header").onmousedown=l:e.onmousedown=l}""")

def enable_drag_property_x(self_pointer):
  lazy_load_js_from_data(self_pointer, """function dragElementX(e){var n=0,t=0;function o(e){(e=e||window.event).preventDefault(),t=e.clientX,document.onmouseup=d,document.onmousemove=u}function u(o){(o=o||window.event).preventDefault(),n=t-o.clientX,t=o.clientX,e.style.left=e.offsetLeft-n+"px"}function d(){document.onmouseup=null,document.onmousemove=null}document.getElementById(e.id+"header")?document.getElementById(e.id+"header").onmousedown=o:e.onmousedown=o}""")

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


def inject_css_scrollbar(self_pointer):
    inject_css(self_pointer, css=""" \
::-webkit-scrollbar { width: 10px; height: 10px; } \
::-webkit-scrollbar-track { background: #969393; } \
::-webkit-scrollbar-thumb { background: white; } \
::-webkit-scrollbar-thumb:hover { background: #555; } \
    """)

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

