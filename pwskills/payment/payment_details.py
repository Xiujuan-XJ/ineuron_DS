from os.path import dirname,join,abspath
import sys
#collating  all directory in 1 place
sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from course import course_details

def payment():
    print('this is my payment file')
    
    # packages are directory or a folder
    # module is a python file
    # object is to access everything
    
course_details.course()