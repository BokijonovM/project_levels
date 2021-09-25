# project_3
# Stack: 
Python Flask
# Files:
templates/Configs.html - Retrieving all configurations for all sensor models.
templates/SpecyficSensor - Getting configuration for a specific sensor model.
/templates - additionaly html templates from level 3
app.py - main logic with routes
handlers.py - handlers methods, saving to file.
style.css - additionaly from level 3
# Endpoints:
localhost:/ - main page with layout
localhost:/<sensor_model> - configuration for specific sensor
localhost:/Configs - all configurations 
localhost:/create/<model>/<output>/<handler> - creating config
localhost//Handleit/<string:model>/<string:handler>/<string:output> - handling

