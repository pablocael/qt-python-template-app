# qt-python-template-app
A basic template app using python and qt with QResources and a script to update Designer UI files and resources

# Usage

Just add your code to app.py and the main UI designer file is in gui/MainWindow_ui.ui
Edit gui/MainWindow_ui.ui or gui/resources.qrc and then call

```
cd gui
sh update_ui.sh
```

The generate resources binary and the MainWindow_ui python code will be generate in the root directory (due to pyside issue finding resources, it must be that way)


