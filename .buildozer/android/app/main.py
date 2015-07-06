from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.core.audio import SoundLoader
from kivy.uix.modalview import ModalView

from kivy.utils import platform

from random import randint
from jnius import autoclass

from plyer import vibrator

store = JsonStore('data/data.json')
score = 0
countdown = 0
popup = Popup()
blue = [79 / 255.0, 110 / 255.0, 238 / 255.0, 1]
green = [19 / 255.0, 190 / 255.0, 19 / 255.0, 1]
timePopup = Popup()
sound = SoundLoader.load('snd/click.wav')

Builder.load_file('UI.kv')

if platform == 'android':
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    AdBuddiz = autoclass('com.purplebrain.adbuddiz.sdk.AdBuddiz')


class Menu(Screen):
    high_score_menu_label_text = 'High Score: ' + str(JsonStore('data/data.json').get('userData')['highScore'])

    def call_start(self):

        Clock.schedule_once(self.start_game, 0)

    def start_game(self, dt):

        sm.current = 'game'
        Clock.schedule_interval(self.set_high_score, 1)

    def back_to_menu(self):

        sm.current = 'menu'
        high_score_menu_label_text = 'High Score: ' + str(JsonStore('data/data.json').get('userData')['highScore'])
        self.ids.highScoreMenuLabel.text = high_score_menu_label_text

    def set_high_score(self, dt):

        high_score_menu_label_text = 'High Score: ' + str(JsonStore('data/data.json').get('userData')['highScore'])
        self.ids.highScoreMenuLabel.text = high_score_menu_label_text

    def show_ads(*args):

        if platform == 'android':
            global AdBuddiz
            AdBuddiz.showAd(PythonActivity.mActivity)
        else:
            print 'Not on Android'

    def change_to_settings(self):

        sm.current = 'settings'


class PressButton(Screen):
    def __init__(self, **kwargs):

        super(PressButton, self).__init__(**kwargs)
        self.finalScore = ''

    def buttons_disabled(self):

        self.ids.button1.disabled = True
        self.ids.button2.disabled = True
        self.ids.button3.disabled = True
        self.ids.button4.disabled = True
        self.ids.button5.disabled = True
        self.ids.button6.disabled = True
        self.ids.button7.disabled = True
        self.ids.button8.disabled = True
        self.ids.button9.disabled = True

    def buttons_enabled(self):

        self.ids.button1.disabled = False
        self.ids.button2.disabled = False
        self.ids.button3.disabled = False
        self.ids.button4.disabled = False
        self.ids.button5.disabled = False
        self.ids.button6.disabled = False
        self.ids.button7.disabled = False
        self.ids.button8.disabled = False
        self.ids.button9.disabled = False

    def buttons_reset_color(self):

        global blue

        self.ids.button1.background_color = blue
        self.ids.button2.background_color = blue
        self.ids.button3.background_color = blue
        self.ids.button4.background_color = blue
        self.ids.button5.background_color = blue
        self.ids.button6.background_color = blue
        self.ids.button7.background_color = blue
        self.ids.button8.background_color = blue
        self.ids.button9.background_color = blue

    def buttons_reset_specific_color(self, button):

        global blue

        if button == 1:
            self.ids.button1.background_color = blue
        if button == 2:
            self.ids.button2.background_color = blue
        if button == 3:
            self.ids.button3.background_color = blue
        if button == 4:
            self.ids.button4.background_color = blue
        if button == 5:
            self.ids.button5.background_color = blue
        if button == 6:
            self.ids.button6.background_color = blue
        if button == 7:
            self.ids.button7.background_color = blue
        if button == 8:
            self.ids.button8.background_color = blue
        if button == 9:
            self.ids.button9.background_color = blue

    def check_if_all_clicked(self):

        global blue
        total = 0

        if self.ids.button1.background_color == blue:
            total = total + 1
        if self.ids.button2.background_color == blue:
            total = total + 1
        if self.ids.button3.background_color == blue:
            total = total + 1
        if self.ids.button4.background_color == blue:
            total = total + 1
        if self.ids.button5.background_color == blue:
            total = total + 1
        if self.ids.button6.background_color == blue:
            total = total + 1
        if self.ids.button7.background_color == blue:
            total = total + 1
        if self.ids.button8.background_color == blue:
            total = total + 1
        if self.ids.button9.background_color == blue:
            total = total + 1

        if total == 9:
            total = 0
            return True

    def change_text(self):

        global green

        x = randint(1, 3)
        y = randint(4, 6)
        z = randint(7, 9)

        if x == 1:
            self.ids.button1.background_color = green
        elif x == 2:
            self.ids.button2.background_color = green
        elif x == 3:
            self.ids.button3.background_color = green

        if y == 4:
            self.ids.button4.background_color = green
        elif y == 5:
            self.ids.button5.background_color = green
        elif y == 6:
            self.ids.button6.background_color = green

        if z == 7:
            self.ids.button7.background_color = green
        elif z == 8:
            self.ids.button8.background_color = green
        elif z == 9:
            self.ids.button9.background_color = green

    def start_add_score(self, button):

        self.add_score(button)

    def call_vibrate(self):

        if JsonStore('data/vibrate.json').get('vibrateState')['activeOrNot'] == 'True':
            if platform == 'android':
                vibrator.vibrate(.06)
            else:
                print 'No vibrator'
        else:
            pass

    def add_score(self, button):

        global green
        global blue
        global score
        global sound

        if button == 1:
            if self.ids.button1.background_color == green:
                self.add_score_number()
                self.animate_after_touch()
                self.buttons_reset_specific_color(1)
                self.play_sound()
            else:
                self.minus_score_number()
                self.call_vibrate()
        elif button == 2:
            if self.ids.button2.background_color == green:
                self.add_score_number()
                self.animate_after_touch()
                self.buttons_reset_specific_color(2)
                self.play_sound()
            else:
                self.minus_score_number()
                self.call_vibrate()
        elif button == 3:
            if self.ids.button3.background_color == green:
                self.add_score_number()
                self.animate_after_touch()
                self.buttons_reset_specific_color(3)
                self.play_sound()
            else:
                self.minus_score_number()
                self.call_vibrate()
        elif button == 4:
            if self.ids.button4.background_color == green:
                self.add_score_number()
                self.animate_after_touch()
                self.buttons_reset_specific_color(4)
                self.play_sound()
            else:
                self.minus_score_number()
                self.call_vibrate()
        elif button == 5:
            if self.ids.button5.background_color == green:
                self.add_score_number()
                self.animate_after_touch()
                self.buttons_reset_specific_color(5)
                self.play_sound()
            else:
                self.minus_score_number()
                self.call_vibrate()
        elif button == 6:
            if self.ids.button6.background_color == green:
                self.add_score_number()
                self.animate_after_touch()
                self.buttons_reset_specific_color(6)
                self.play_sound()
            else:
                self.minus_score_number()
                self.call_vibrate()
        elif button == 7:
            if self.ids.button7.background_color == green:
                self.add_score_number()
                self.animate_after_touch()
                self.buttons_reset_specific_color(7)
                self.play_sound()
            else:
                self.minus_score_number()
                self.call_vibrate()
        elif button == 8:
            if self.ids.button8.background_color == green:
                self.add_score_number()
                self.animate_after_touch()
                self.buttons_reset_specific_color(8)
                self.play_sound()
            else:
                self.minus_score_number()
                self.call_vibrate()
        elif button == 9:
            if self.ids.button9.background_color == green:
                self.add_score_number()
                self.animate_after_touch()
                self.buttons_reset_specific_color(9)
                self.play_sound()
            else:
                self.minus_score_number()
                self.call_vibrate()

        self.ids.scoreLabel.text = 'Score: ' + str(score)
        self.change_after_three()

    def animate_after_touch(self):

        Clock.schedule_once(self.un_animate_after_touch, 0.1)

    def un_animate_after_touch(self, dt):

        self.ids.buttonsGrid.spacing = [3, 3]

    def play_sound(self):

        global sound

        if JsonStore('data/sound.json').get('soundState')['activeOrNot'] == 'True':
            sound.play()
        else:
            pass

    def change_after_three(self):

        global green
        global blue

        if self.check_if_all_clicked() == True:
            self.change_text()

    def add_score_number(self):

        global score
        score = score + 1

    def minus_score_number(self):

        global score
        score = score - 1

    def timer(self, dt):

        global countdown
        global timePopup

        countdown = countdown - 1
        self.ids.timeLabel.text = 'Time: ' + str(countdown) + ' seconds'

        if countdown <= 0:
            Clock.unschedule(self.timer)
            timePopup = ModalView(auto_dismiss=False, background_color=[1, 0, 0, .7])
            timePopup.add_widget(Label(text='Game Over', font_size='50sp', color=[0, 0, 0, 1]))
            timePopup.open()
            Clock.schedule_once(self.change_to_end, 1.5)

    def start(self):

        global countdown
        sm.current = 'game'

        self.ids.startButton.disabled = True
        self.buttons_enabled()
        self.buttons_reset_color()

        countdown = 10
        Clock.schedule_interval(self.timer, 1)

        self.change_text()

    def reset(self):

        global score
        score = 0
        self.ids.scoreLabel.text = 'Score: ' + str(score)
        self.ids.timeLabel.text = 'Time: 10 seconds'
        self.ids.startButton.disabled = False
        self.buttons_disabled()
        self.buttons_reset_color()

    def change_to_end(self, dt):

        global score
        global popup
        global timePopup
        timePopup.dismiss()
        self.finalScore = str(score)

        if JsonStore('data/data.json').get('userData')['highScore'] < score:
            JsonStore('data/data.json').put('userData', highScore=score)

        popup_content = BoxLayout(orientation='vertical', spacing=3)
        play_again_button = Button(text='Play Again', on_release=self.play_again, font_size='40sp',
                                 background_color=[0, 0, 0, 1])
        back_to_menu_button = Button(text='Back To Menu', on_release=self.change_to_menu, font_size='40sp',
                                  background_color=[0, 0, 0, 1])
        final_score_label = Label(text='Score: ' + self.finalScore, font_size='50sp', color=[0, 0, 0, 1])
        high_score_label = Label(text='High Score: ' + str(JsonStore('data/data.json').get('userData', )['highScore']),
                               font_size='50sp', color=[0, 0, 0, 1])

        popup_content.add_widget(final_score_label)
        popup_content.add_widget(high_score_label)
        popup_content.add_widget(play_again_button)
        popup_content.add_widget(back_to_menu_button)

        popup = ModalView(auto_dismiss=False, background_color=[1, 0, 0, .7])
        popup.add_widget(popup_content)
        if platform == 'android':
            popup.bind(on_dismiss=Menu().show_ads())
        popup.open()

        self.reset()

    def change_to_menu(self, dt):

        global popup
        Menu().back_to_menu()
        popup.dismiss()

    def play_again(self, dt):

        global popup
        popup.dismiss()


class Settings(Screen):
    def back_to_menu(self):

        sm.current = 'menu'

    def check_sound(self):

        if JsonStore('data/sound.json').get('soundState')['activeOrNot'] == 'True':
            return True
        else:
            return False

    def change_sound(self, active):

        if active == True:
            JsonStore('data/sound.json').put('soundState', activeOrNot='True')
        else:
            JsonStore('data/sound.json').put('soundState', activeOrNot='False')

    def check_vibrate(self):

        if JsonStore('data/vibrate.json').get('vibrateState')['activeOrNot'] == 'True':
            return True
        else:
            return False

    def change_vibrate(self, active):

        if active == True:
            JsonStore('data/vibrate.json').put('vibrateState', activeOrNot='True')
        else:
            JsonStore('data/vibrate.json').put('vibrateState', activeOrNot='False')


sm = ScreenManager(transition=WipeTransition())
sm.add_widget(Menu(name='menu'))
sm.add_widget(PressButton(name='game'))
sm.add_widget(Settings(name='settings'))


class PressButtonApp(App):
    def on_start(self):
        if platform == 'android':
            global AdBuddiz
            AdBuddiz.setPublisherKey('PublisherKey')
            AdBuddiz.setTestModeActive()
            AdBuddiz.cacheAds(PythonActivity.mActivity)

    def on_pause(self):
        return True

    def on_resume(self):
        pass

    def build(self):
        return sm


if __name__ == '__main__':
    PressButtonApp().run()
