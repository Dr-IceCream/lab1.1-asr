from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QGraphicsBlurEffect

from asrInterface import Ui_MainWindow
import sys
import speech_recognition as sr
import threading
import time
import win32api
import os
import pyaudio
import wave
import pyautogui


class myWindow(QtWidgets.QMainWindow):

    # 添加一个新的信号，用于通知主线程更新动画和其他界面部分
    update_animation = QtCore.pyqtSignal(bool)
    update_label = QtCore.pyqtSignal(str)

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 将新信号连接到槽函数
        self.update_animation.connect(self.toggle_sound_wave_animation)
        self.update_label.connect(self.update_user_input_label)

        # 添加一个新的线程，用于运行 process_voice_command 方法
        self.voice_thread = threading.Thread(target=self.process_voice_command)
        self.voice_thread.setDaemon(True)
        self.voice_thread.start()

        # 添加 QGraphicsBlurEffect 对象
        self.blur_effect = QGraphicsBlurEffect(self.ui.inner_widget)
        self.blur_effect.setBlurRadius(0)
        self.ui.inner_widget.setGraphicsEffect(self.blur_effect)

    def set_blur_radius(self, radius):
        self.blur_effect.setBlurRadius(radius)

    # 控制声浪动画的显示和隐藏（已添加动画渐变效果）
    def toggle_sound_wave_animation(self, show):
        # 创建QPropertyAnimation对象，设置动画目标为QGraphicsBlurEffect对象的blurRadius属性
        anim = QtCore.QPropertyAnimation(self.blur_effect, b"blurRadius")
        anim.setDuration(800)  # 设置动画时长为800毫秒
        anim.setStartValue(self.blur_effect.blurRadius())  # 设置动画起始值为当前模糊半径
        if show:
            self.ui.sound_wave_gif.start()
            self.ui.sound_wave_label.show()
            # 模糊效果
            anim.setEndValue(5)  # 设置动画结束值为模糊半径5
        else:
            self.ui.sound_wave_label.hide()
            self.ui.sound_wave_gif.stop()
            # 模糊效果消失
            anim.setEndValue(0)  # 设置动画结束值为模糊半径0
        # 在动画结束时将模糊效果应用到界面
        anim.finished.connect(lambda: self.set_blur_radius(anim.endValue()))
        # 启动动画
        anim.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

    # 处理语音识别和命令执行
    def process_voice_command(self):
        r = sr.Recognizer()
        while True:

            # 在每次输入语音指令之前暂停2s
            time.sleep(2)

            with sr.Microphone() as source:
                print("Listening...")
                self.update_animation.emit(True)
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, phrase_time_limit=3)
                self.update_animation.emit(False)

                try:
                    # command = r.recognize_sphinx(audio).lower()
                    command = r.recognize_google(audio, language='en-US').lower()
                    print("You said:", command)
                    self.update_label.emit(command)

                    if "play music" in command:
                        print("Playing music...")
                        # 获取当前脚本的绝对路径
                        script_dir = os.path.dirname(os.path.abspath(__file__))
                        # 使用相对路径构建音频文件的绝对路径
                        audio_file_path = os.path.join(script_dir, 'assets', 'Sunflower.wav')
                        # 使用绝对路径调用ShellExecute
                        win32api.ShellExecute(0, 'open', audio_file_path, '', '', 1)
                        # 使用不打开音乐播放器的方式播放音乐
                        # self.play_music("./assets/Sunflower.wav")
                    elif "open notepad" in command:
                        print("Opening Notepad...")
                        win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)
                    elif "volume up" in command:
                        print("volume up...")
                        pyautogui.press("volumeup")
                    elif "volume down" in command:
                        print("volume down...")
                        pyautogui.press("volumedown")
                    elif command in ["exit", "quit"]:
                        print("Exiting...")
                        QtWidgets.qApp.quit()

                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))

    # 用于更新 user_input_label 的文本
    def update_user_input_label(self, text):
        if not self.ui.user_input_label.text():
            self.ui.user_input_label.setText(f"You: {text}")
        else:
            current_text = self.ui.user_input_label.text().split('\n')
            if len(current_text) >= 4:
                current_text.pop(0)
            current_text.append(f"You: {text}")
            self.ui.user_input_label.setText('\n'.join(current_text))

    # 使用 PyAudio 播放音乐
    def play_music(self, file_path):
        CHUNK = 1024
        wf = wave.open(file_path, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(CHUNK)
        while data:
            stream.write(data)
            data = wf.readframes(CHUNK)
        stream.stop_stream()
        stream.close()
        p.terminate()

app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())
