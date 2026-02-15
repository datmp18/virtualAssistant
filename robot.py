import pyttsx3
import speech_recognition as sr
from datetime import datetime
import ollama
# API_KEY = "fa8c5abefb9d5ddc906c907df1111104"
# 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
r = sr.Recognizer()
r.energy_threshold = 300
r.pause_threshold = 0.6
r.dynamic_energy_threshold = True

mic = sr.Microphone()

def chat_with_ai(text):
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "Bạn là trợ lý AI thân thiện nói tiếng Việt"},
            {"role": "user", "content": text}
        ]
    )
    return response["message"]["content"]
def get_datetime_vn():
    now = datetime.now()

    thu = [
        "Thứ Hai", "Thứ Ba", "Thứ Tư",
        "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"
    ][now.weekday()]

    return (
        f"Hôm nay là {thu}, "
        f"ngày {now.day} tháng {now.month} năm {now.year}, "
    )
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




while True:
    try:
       
        with mic as source:
         
            r.adjust_for_ambient_noise(source, duration=0.3)

            audio = r.listen(source)
           
        
        text = r.recognize_google(audio, language="vi-VN").lower()
        print("🗣️ Bạn nói:", text)
        if "dừng lại" in text:
            speak("bái bai")
            break

        if "ngày" in text or "hôm nay" in text:
            speak(get_datetime_vn())

        elif "giờ" in text or "mấy giờ" in text:
            now = datetime.now()
            speak(f"Bây giờ là {now.hour} giờ {now.minute} phút")
        elif "bạn tên là gì" in text or "tên bạn là gì" in text:
            speak("Tôi là Ô rôn do aladin tạo ra để hỗ trợ bạn.")
        elif "bạn có khỏe không" in text:
            speak("Cảm ơn bạn đã hỏi thăm, tôi rất khỏe.")
      
        else:
            speak(chat_with_ai(text))

    except sr.UnknownValueError:
    
        pass
    except KeyboardInterrupt:
        print("\n Dừng trợ lý")
        break
