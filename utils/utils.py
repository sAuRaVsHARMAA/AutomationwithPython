import inspect
import logging


class UtilsData:
    baseurl = "http://automationpractice.com/index.php"
    login_email = "saurav.1300@gmail.com"
    login_password = "saurav001"

    def whoami(self):
        return inspect.stack()[1][3]

    def logger(self, level, *message):
        formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s: ', datefmt='%d-%b-%Y %I:%M:%S %p')
        logger = logging.getLogger('Automation Failed')  #name
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('C://misc/test.txt')   #location
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        try:
            level = level.lower()
            if level == "debug":
                logger.debug(message, exc_info=True)
            elif level == "info":
                logger.info(message, exc_info=True)
            elif level == "warning":
                logger.warning(message, exc_info=True)
            elif level == "error":
                logger.error(message, exc_info=True)
            elif level == "critical":
                logger.critical(message, exc_info=True)
            else:
                print("Please enter correct level name ")
        except:
            logger.info("In exception block due to an unexpected exception", exc_info=True)






