from PyPap3r import wallpaper_file, wallpaper_url
import pyautogui
import getpass
import rumps

class App(object):
    def __init__(self):
        self.app = rumps.App("BaconPaper", "🥓")
        self.set_up_menu()
        self.changeFromURLButton = rumps.MenuItem(title="Change From URL", callback=self.changeFromURL)
        self.changeFromFileButton = rumps.MenuItem(title="Change From File", callback=self.changeFromFile)
        self.app.menu = [self.changeFromURLButton, self.changeFromFileButton]

    def changeFromURL(self, sender):
        input = rumps.Window(message='', title='Enter the URL of an image here:', default_text='https://www.thebaconpug.com/css/img/background.jpg', ok='Change', cancel='Exit', dimensions=(320, 160))
        response = input.run()
        if response.clicked:
            wallpaper_url(response.text)

    def changeFromFile(self, sender):
        input = rumps.Window(message='', title='Enter the file path of an image here:', default_text=getpass.getuser() + '/image', ok='Change', cancel='Exit', dimensions=(320, 160))
        response = input.run()
        if response.clicked:
            wallpaper_file(response.text)

    def set_up_menu(self):
        self.app.title = "🥓"

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = App()
    app.run()
