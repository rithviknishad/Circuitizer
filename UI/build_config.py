#!/usr/bin/python3
import json

config_template = {
    'primary-foreground-color': '#969393',
    'secondary-foreground-color': '#e3a42c',

    'primary-background-color': '#302d2d',
    'secondary-background-color': 'white',

    'menu-background-color': '#302d2d',
    'tool-background-color': '#333333',
    'panel-background-color': '#252526',
    'canvas-background-color': '#1E1E1E',
    'status-background-color': '#e3a42c',
    
    'window-type': 'desktop',
    'cdn-or-local': 'local',

    'font-size-dropbox-item': 'small',
    'panel-width': '300px'
}


if __name__ == "__main__":
    open('config.json', 'w').write(json.dumps(config_template, indent=4))
