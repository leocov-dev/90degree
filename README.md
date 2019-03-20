# Maya 90 Degree
![tested_maya_2018](https://img.shields.io/badge/maya-2018-128189.svg?style=flat)
![license](https://img.shields.io/badge/license-MIT-A31F34.svg?style=flat)

**This project is still a WIP**

## Description

This Python tool for Maya will let you rotate selected objects by 90 degrees in a positive or negative direction.

That is all.

It is more interesting as an example of a frame-less Qt window with lots of custom `paintEvent()` and `mouseEvent()` work.

##### Screenshot
![Window Screenshot](.screenshots/capture_01.png)
## Installation and Use
1. Place the entire directory `qt_img_resource_browser` in your Maya scripts directory or a directory that Maya can load Python scripts from.
    
    ```
    ├- maya
       ├- scripts
          ├- 90degree
             ├- app.py
             ├- interface.py
             ├- etc . . .
    ```
    
2. Restart Maya.
3. Launch the window with this python command:

    ```python
    # Python
    from maya_90_degree import interface
    interface.load()
    ```
    
##### Notes

This should work in any recent version of Maya that has Qt but it has only been tested in Maya 2018.
## Known Issues

* Moving the mouse too quickly while dragging the window causes it to be left behind.
