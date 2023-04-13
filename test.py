
import speech_recognition as sr
import os
from playsound import playsound
import pyaudio
import wave
import win32api
import os

# 获取当前脚本的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 使用相对路径构建音频文件的绝对路径
audio_file_path = os.path.join(script_dir, 'assets', 'Sunflower.wav')

# 使用绝对路径调用ShellExecute
win32api.ShellExecute(0, 'open', audio_file_path, '', '', 1)

# win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)
# win32api.ShellExecute(0, 'open', 'D:\\PyCharm_Project\\lab1.1-asr\\assets\\Sunflower.wav', '', '', 1)



#
# # 打开音频文件
# wav_file = wave.open('./assets/Sunflower.wav', 'rb')
#
# # 创建 PyAudio 对象
# p = pyaudio.PyAudio()
#
# # 打开音频流
# stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
#                 channels=wav_file.getnchannels(),
#                 rate=wav_file.getframerate(),
#                 output=True)
#
# # 播放音频
# data = wav_file.readframes(1024)
# while data:
#     stream.write(data)
#     data = wav_file.readframes(1024)
#
# # 停止流和 PyAudio 对象
# stream.stop_stream()
# stream.close()
# p.terminate()


# # Working with audio files
# r = sr.Recognizer()
# speech = sr.AudioFile('f1lcapae.wav')
# with speech as source:
#     audio = r.record(source)
# print(r.recognize_sphinx(audio))

# # Working with Microphones
# mic = sr.Microphone()
# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
# print(r.recognize_sphinx(audio))

# os.system("notepad.exe")