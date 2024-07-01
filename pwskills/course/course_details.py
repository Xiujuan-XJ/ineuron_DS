# put all file paths collated
from os.path import dirname,join,abspath
import sys

sys.path.insert(0,abspath(join(dirname(__file__),'..')))


from payment import payment_details

def course():
    print('this is my course file')

payment_details.payment()