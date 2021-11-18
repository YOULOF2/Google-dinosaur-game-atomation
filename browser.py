import os

import gi
import pyautogui
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException

gi.require_version('Gdk', '3.0')
from gi.repository import Gdk


class Browser:
    def __init__(self):
        self.__path_to_exe = "firefox_websdriver/geckodriver"
        self.website = "https://elgoog.im/t-rex/"
        self.driver = webdriver.Firefox(executable_path=self.__path_to_exe)

        self.__colour_type = "RGB"
        self.__folder = "temp/"
        self.__do_clean_up = True

        self.__win = Gdk.get_default_root_window()
        self.__h = self.__win.get_height()
        self.__w = self.__win.get_width()

    def __clean_up(self):
        # Delete all the screenshots captured
        if self.__do_clean_up:
            for filename in os.listdir(self.__folder):
                file_path = os.path.join(self.__folder, filename)
                os.remove(file_path)

    def launch(self):
        # Launches the browser in full screen
        self.driver.maximize_window()

        self.driver.get(self.website)
        pyautogui.press('up')

    def check_exit(self):
        # Checks if the browser has been closed
        try:
            _ = self.driver.window_handles
        except InvalidSessionIdException:
            self.__clean_up()
            return True
        except WebDriverException:
            self.__clean_up()
            return True
        else:
            return False


browser = Browser()
