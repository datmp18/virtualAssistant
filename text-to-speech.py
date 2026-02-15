import pyttsx3

def speak(text):
  
    engine = None
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 150)
        
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"Lỗi khi đọc văn bản: {e}")
        
    finally:
     
        if engine:
            engine.stop()


speak("Này, tôi có bất ngờ dành cho bạn đấy")
