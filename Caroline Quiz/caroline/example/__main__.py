import os
from distutils.dir_util import copy_tree
import shutil

print("Writting example presentation in the given directory...")

carolineHTML = os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "html_dist")

carolineDestination = os.path.join(os.getcwd(), 'caroline')
if not os.path.exists(carolineDestination):
    os.makedirs(carolineDestination)

copy_tree(carolineHTML, carolineDestination)

presentationFilesDestination = os.path.join(os.getcwd(), 'presentation_files')
presentationFiles = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "presentation_files")
copy_tree(presentationFiles, presentationFilesDestination)

dataFolder = os.path.dirname(os.path.realpath(__file__))
destinationFolder  = os.getcwd()
shutil.copy(os.path.join(dataFolder, "presentation_code.py"), destinationFolder)
shutil.copy(os.path.join(dataFolder, "presentation.html"), destinationFolder)
shutil.copy(os.path.join(dataFolder, "presentation_audience.html"), destinationFolder)
shutil.copy(os.path.join(dataFolder, "simple_server.py"), destinationFolder)

print("Presentation added, to see it live, run following command from commad-line")
print("python simple_server.py")
