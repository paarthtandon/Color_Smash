from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock, mainthread
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivy.graphics.instructions import *
from kivy.core.audio import SoundLoader
from kivy.uix.modalview import ModalView
from kivy.utils import platform

from jnius import autoclass
from plyer import vibrator
from random import randint
import os


store = JsonStore('data.json')
score = 0
countdown = 0
popup = Popup()
blue  = [79/255.0, 110/255.0, 238/255.0, 1]
green = [19/255.0, 190/255.0, 19/255.0, 1]
timePopup = Popup()
sound = SoundLoader.load('click.wav')


Builder.load_file("UI.kv")

if platform=="android":
    PythonActivity=autoclass("org.renpy.android.PythonActivity")
    AdBuddiz=autoclass("com.purplebrain.adbuddiz.sdk.AdBuddiz")

class Menu(Screen):

	highScoreMenuLabelText = "High Score: " + str(JsonStore('data.json').get('userData')["highScore"])


	def setHighScore(self, dt):
		highScoreMenuLabelText = "High Score: " + str(JsonStore('data.json').get('userData')["highScore"])
		self.ids.highScoreMenuLabel.text = highScoreMenuLabelText

	def callStart(self):
		Clock.schedule_once(self.startGame, 0)

	def startGame(self, dt):
		sm.current = 'game'

		Clock.schedule_interval(self.setHighScore, 1)
		
	def backToMenu(self):
		sm.current = "menu"
		
		highScoreMenuLabelText = "High Score: " + str(JsonStore('data.json').get('userData')["highScore"])
		self.ids.highScoreMenuLabel.text = highScoreMenuLabelText
	
	def show_ads(*args):
		global AdBuddiz
		AdBuddiz.showAd(PythonActivity.mActivity)	

		




class PressButton(Screen):

	def __init__(self, **kwargs):
		super(PressButton, self).__init__(**kwargs)

		self.finalScore = ""


	def buttonsDisabled(self):

		self.ids.button1.disabled = True
		self.ids.button2.disabled = True
		self.ids.button3.disabled = True
		self.ids.button4.disabled = True
		self.ids.button5.disabled = True
		self.ids.button6.disabled = True
		self.ids.button7.disabled = True
		self.ids.button8.disabled = True
		self.ids.button9.disabled = True


	def buttonsEnabled(self):

		self.ids.button1.disabled = False
		self.ids.button2.disabled = False
		self.ids.button3.disabled = False
		self.ids.button4.disabled = False
		self.ids.button5.disabled = False
		self.ids.button6.disabled = False
		self.ids.button7.disabled = False
		self.ids.button8.disabled = False
		self.ids.button9.disabled = False


	def buttonsResetColor(self):
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


	def buttonsResetSpecificColor(self, button):
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


	def checkIfAllClicked(self):
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
			return True
			total = 0



	def changeText(self):
		global green

		print "changeText"

		x = randint(1,3)
		y = randint(4,6)
		z = randint(7,9)

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


	def startAddScore(self, button):
		self.addScore(button)


	def callVibrate(self):
		if vibrator.exists() == True:
			vibrator.vibrate(.06)
		else:
			print "No vibrator"

	
	def addScore(self, button):
		global green
		global blue
		global score
		global sound


		if button == 1:
			if self.ids.button1.background_color == green:
				self.addScoreNumber()
				self.buttonsResetSpecificColor(1)
				sound.play()
			else:
				self.minusScoreNumber()
				self.callVibrate()
		elif button == 2:
			if self.ids.button2.background_color == green:
				self.addScoreNumber()
				self.buttonsResetSpecificColor(2)
				sound.play()
			else:
				self.minusScoreNumber()
				self.callVibrate()
		elif button == 3:
			if self.ids.button3.background_color == green:
				self.addScoreNumber()
				self.buttonsResetSpecificColor(3)
				sound.play()
			else:
				self.minusScoreNumber()
				self.callVibrate()
		elif button == 4:
			if self.ids.button4.background_color == green:
				self.addScoreNumber()
				self.buttonsResetSpecificColor(4)
				sound.play()
			else:
				self.minusScoreNumber()
				self.callVibrate()
		elif button == 5:
			if self.ids.button5.background_color == green:
				self.addScoreNumber()
				self.buttonsResetSpecificColor(5)
				sound.play()
			else:
				self.minusScoreNumber()
				self.callVibrate()
		elif button == 6:
			if self.ids.button6.background_color == green:
				self.addScoreNumber()
				self.buttonsResetSpecificColor(6)
				sound.play()
			else:
				self.minusScoreNumber()
				self.callVibrate()
		elif button == 7:
			if self.ids.button7.background_color == green:
				self.addScoreNumber()
				self.buttonsResetSpecificColor(7)
				sound.play()
			else:
				self.minusScoreNumber()
				self.callVibrate()
		elif button == 8:
			if self.ids.button8.background_color == green:
				self.addScoreNumber()
				self.buttonsResetSpecificColor(8)
				sound.play()
			else:
				self.minusScoreNumber()
				self.callVibrate()
		elif button == 9:
			if self.ids.button9.background_color == green:
				self.addScoreNumber()
				self.buttonsResetSpecificColor(9)
				sound.play()
			else:
				self.minusScoreNumber()
				self.callVibrate()

		self.ids.scoreLabel.text = "Score: " + str(score)

		self.changeAfterThree()


	def changeAfterThree(self):
		global green
		global blue

		if self.checkIfAllClicked() == True:

			self.changeText()


	def addScoreNumber(self):
		global score

		score = score + 1

	def minusScoreNumber(self):
		global score

		score = score - 1



	def timer(self, dt):
		global countdown
		global timePopup

		countdown = countdown - 1
		self.ids.timeLabel.text = "Time: " + str(countdown) + " seconds"

		if countdown <= 0:
			Clock.unschedule(self.timer)

			timePopup = ModalView(auto_dismiss = False, background_color = [1, 0, 0, .7])
			timePopup.add_widget(Label(text="Game Over", font_size="50sp", color=[0,0,0,1]))
			timePopup.open()
			Clock.schedule_once(self.changeToEnd, 1.5)



	def start(self):
		global countdown

		print "Start"
		sm.current = 'game'

		self.ids.startButton.disabled = True
		self.buttonsEnabled()
		self.buttonsResetColor()
		
		countdown = 10
		Clock.schedule_interval(self.timer, 1)

		self.changeText()

	def reset(self):

		global score

		score = 0
		self.ids.scoreLabel.text = "Score: " + str(score)
		self.ids.timeLabel.text = "Time: 10 seconds"

		self.ids.startButton.disabled = False

		self.buttonsDisabled()
		self.buttonsResetColor()


	def changeToEnd(self, dt):
		global score
		global popup
		global timePopup

		timePopup.dismiss()

		self.finalScore = str(score)

		if JsonStore('data.json').get('userData')['highScore'] < score:
			JsonStore('data.json').put('userData', highScore=score)

		popupContent = BoxLayout(orientation = 'vertical', spacing=3)
		playAgainButton = Button(text = "Play Again", on_release = self.playAgain, font_size = "40sp", background_color = [0,0,0,1])
		backToMenuButton = Button(text = "Back To Menu", on_release = self.changeToMenu, font_size = "40sp", background_color = [0,0,0,1])
		finalScoreLabel = Label(text = "Score: " + self.finalScore, font_size="50sp", color=[0,0,0,1])
		highScoreLabel = Label(text = "High Score: " + str(JsonStore('data.json').get('userData',)['highScore']), font_size="50sp", color=[0,0,0,1])

		popupContent.add_widget(finalScoreLabel)
		popupContent.add_widget(highScoreLabel)
		popupContent.add_widget(playAgainButton)
		popupContent.add_widget(backToMenuButton)

		popup = ModalView(auto_dismiss=False, background_color = [1, 0, 0, .7])
		popup.add_widget(popupContent)
		popup.bind(on_dismiss=Menu().show_ads())
		popup.open()

		self.reset()

	def changeToMenu(self,dt):
		global popup
		Menu().backToMenu()
		popup.dismiss()


	def playAgain(self,dt):
		global popup
		popup.dismiss()
			


sm = ScreenManager(transition=WipeTransition())
sm.add_widget(Menu(name='menu'))
sm.add_widget(PressButton(name='game'))


class PressButtonApp(App):

	def on_start(self):
		global AdBuddiz

		AdBuddiz.setPublisherKey("PublisherKey")
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
