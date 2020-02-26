var meta = document.createElement('meta');
meta.http-equiv = 'Cache-Control';
meta.content = 'no-cache, no-store, must-revalidate';
document.getElementsByTagName('HEAD')[0].appendChild(meta);

var meta2 = document.createElement('meta');
meta2.http-equiv = 'Pragma';
meta2.content = 'no-cache';
document.getElementsByTagName('HEAD')[0].appendChild(meta2);

var meta3 = document.createElement('meta');
meta3.http-equiv = 'Expires';
meta3.content = '0';
document.getElementsByTagName('HEAD')[0].appendChild(meta3);
