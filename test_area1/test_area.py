import logging
import time
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(asctime)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')

def area(length, breadth):
    return length*breadth

def test_area():
    logging.info("This is test area method")
    author="Kiran"
    assert area(2, 3) == 6
    time.sleep(2)
    logging.info("Test area method completed by {}".format(author))

print test_area()