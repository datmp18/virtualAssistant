import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

print("🟢 Trợ lý đang lắng nghe liên tục... (Ctrl+C để dừng)")

while True:
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.3)

            audio = r.listen(source)

        text = r.recognize_google(audio, language="vi-VN")
        print("🗣️ Bạn nói:", text)

    except:
        print("❌ Không nhận diện được giọng nói.")
