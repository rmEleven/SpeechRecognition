from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
import sys
import os
import webbrowser

import speech_recognition as sr
import threading


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    print("Start listening to the microphone...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Please start speaking...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    print("End listening to microphone。")

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        print("Processing...")
        response["transcription"] = recognizer.recognize_google(audio, language='en-US')
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    return response


class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()   # 调用父类的构造函数
        # 初始化变量 myCommand
        self.myCommand = ["play music", "open notepad"]
        # 禁用最大化按钮
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

        self.ui = Ui_MainWindow()          # 创建 Ui_MainWindow 实例
        self.ui.setupUi(self)              # 设置 UI 界面

        self.r = sr.Recognizer()           # 创建一个 Recognizer 对象，用于语音识别
        self.mic = sr.Microphone()         # 创建一个 Microphone 对象，用于处理麦克风输入的音频数据

        # 创建一个新的线程对象，运行 listen_and_recognize 方法。
        self.asr_thread = threading.Thread(target=self.listen_and_recognize)
        # 标记为守护线程，这意味着如果主线程结束，它将自动退出。
        self.asr_thread.daemon = True
        # 在窗口显示之后启动语音识别线程
        self.showEvent = self.start_asr_thread


    def start_asr_thread(self, event):
        # 启动语音识别线程
        self.asr_thread.start()


    def play_music(self, audio_file=".\\Audios\\music.mp3"):
        # 播放音乐
        webbrowser.open(audio_file)

    
    def open_text(self, text_file=".\\Texts\\lyric.txt"):
        # 打开文件
        os.startfile(text_file)


    def listen_and_recognize(self):
        while True:
            #进行语音识别
            for i in range(5):
                response = recognize_speech_from_mic(self.r, self.mic)
                if response["transcription"]:
                    break
                if not response["success"]:
                    break
                print("I didn't catch that. What did you say?\n")

            # 遇到错误退出
            if response["error"]:
                print("ERROR: {}".format(response["error"]))
                break
                
            # 显示识别结果
            response["transcription"] = response["transcription"].lower()
            print("You said: {}".format(response["transcription"]))

            if self.myCommand[0] in response["transcription"]:
                # 播放音乐
                print(self.myCommand[0], "detected!")
                self.play_music()
            elif self.myCommand[1] in response["transcription"]:
                # 打开文件
                print(self.myCommand[1], "detected!")
                self.open_text()
            else:
                print("no command detected!")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])  # 创建 QApplication 实例
    application = myWindow()          # 创建 myWindow 实例
    application.show()                # 显示窗口
    sys.exit(app.exec())              # 运行主循环