/*
    Enable the drag property in Circuitizer Widget
*/

// Drag widget in both X, Y axis
function dragElement(e) {
    var n = 0,
        t = 0,
        o = 0,
        u = 0;

    function l(e) {
        (e = e || window.event).preventDefault(), o = e.clientX, u = e.clientY, document.onmouseup = m, document.onmousemove = d
    }

    function d(l) {
        (l = l || window.event).preventDefault(), n = o - l.clientX, t = u - l.clientY, o = l.clientX, u = l.clientY, e.style.top = e.offsetTop - t + "px", e.style.left = e.offsetLeft - n + "px"
    }

    function m() {
        document.onmouseup = null, document.onmousemove = null
    }
    document.getElementById(e.id + "header") ? document.getElementById(e.id + "header").onmousedown = l : e.onmousedown = l
}

// Drag widget in X axis only
function dragElementX(e) {
    var n = 0,
        t = 0;

    function o(e) {
        (e = e || window.event).preventDefault(), t = e.clientX, document.onmouseup = d, document.onmousemove = u
    }

    function u(o) {
        (o = o || window.event).preventDefault(), n = t - o.clientX, t = o.clientX, e.style.left = e.offsetLeft - n + "px"
    }

    function d() {
        document.onmouseup = null, document.onmousemove = null
    }
    document.getElementById(e.id + "header") ? document.getElementById(e.id + "header").onmousedown = o : e.onmousedown = o
}
