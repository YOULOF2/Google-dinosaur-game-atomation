import pyautogui
import webcolors
from PIL import ImageDraw, Image
from gi.repository import Gdk

from browser import browser

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01

START_NUM_X, END_NUM_X, STEP_NUM_X = 1000, 1200, 5
Y_LIST = [480, 490]
R = 2


def take_screenshot(counter):
    filename = f"temp/my_screenshot{counter}.png"

    win = Gdk.get_default_root_window()
    h = win.get_height()
    w = win.get_width()

    pb = Gdk.pixbuf_get_from_window(win, 0, 0, w, h)

    if pb is not None:
        pb.savev(filename, "png", (), ())
    else:
        print("Unable to get the screenshot.")

    image_obj = Image.open(filename)
    rgb_image = image_obj.convert("RGB")
    return rgb_image


def jump():
    for i in range(2):
        pyautogui.press("up")


def main():
    browser.launch()

    running = True
    counter = 0

    while running:
        grey_list = []
        rgb_image = take_screenshot(counter)

        for Y in Y_LIST:
            # At Y, the HEX colour is found then appended to the half list, if its value is #535353
            half_list = [webcolors.rgb_to_hex(rgb_image.getpixel((X, Y)))
                         for X in range(START_NUM_X, END_NUM_X, STEP_NUM_X)
                         if webcolors.rgb_to_hex(rgb_image.getpixel((X, Y))) == "#535353"]
            grey_list = grey_list + half_list

            draw = ImageDraw.Draw(rgb_image)

            [draw.ellipse((X - R, Y - R, X + R, Y + R), fill=(255, 0, 0, 0))
             for X in range(START_NUM_X, END_NUM_X, STEP_NUM_X)]
            rgb_image.save(f"123/my_screenshot{counter}.png")

        print(grey_list)

        try:
            grey_list[0]
        except IndexError:
            print("STAY")
        else:
            print("JUMP")
            jump()

        if browser.check_exit():
            running = False
            exit()

        counter += 1


if __name__ == "__main__":
    main()
