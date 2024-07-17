import unittest
from simplecolorlogger.logger import ColorLogger

class TestColorLogger(unittest.TestCase):
    def test_log(self):
        ColorLogger.log("This is a normal log message.")
        ColorLogger.log("This is a log message with a custom color.", ColorLogger.YELLOW)
        ColorLogger.info("This is an info message.")
        ColorLogger.success("This is a success message.")
        ColorLogger.warning("This is a warning message.")
        ColorLogger.error("This is an error message.")
        
if __name__ == "__main__":
    unittest.main()
