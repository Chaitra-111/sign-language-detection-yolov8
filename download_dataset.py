from roboflow import Roboflow

rf = Roboflow(api_key="u0TngiNgoFitlzecmONN")

project = rf.workspace("bahaynidon").project("hsl-euovf")

version = project.version(1)

dataset = version.download("yolov8")