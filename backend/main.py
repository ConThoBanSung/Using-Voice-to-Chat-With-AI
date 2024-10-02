from flask import Flask, request, jsonify
from flask_cors import CORS  # Thêm hỗ trợ CORS
import speech_recognition as sr
import google.generativeai as genai

# Cấu hình API Key cho Gemini API
genai.configure(api_key="AIzaSyBqRFBpiXYLu4DjmE8WnxCiyBogOZW31gc")
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)
CORS(app)  # Kích hoạt CORS cho tất cả các route

# API ghi âm và nhận diện giọng nói
@app.route("/recognize-speech", methods=["POST"])
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bắt đầu ghi âm... Nói gì đó!")
        audio = recognizer.listen(source)
        print("Ghi âm xong. Đang xử lý...")

        try:
            text = recognizer.recognize_google(audio, language="vi-VN")
            print(f"Nội dung âm thanh: {text}")
            return jsonify({"text": text})
        except sr.UnknownValueError:
            return jsonify({"error": "Không thể nhận diện âm thanh."}), 400
        except sr.RequestError as e:
            return jsonify({"error": f"Lỗi khi kết nối với Google: {e}"}), 500

# API gọi Gemini
@app.route("/gemini-response", methods=["POST"])
def get_gemini_response():
    data = request.get_json()
    prompt = data.get("prompt", "")
    
    if not prompt:
        return jsonify({"error": "Prompt không được để trống."}), 400
    
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                max_output_tokens=5000,
                temperature=1.0,
            ),
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": f"Lỗi khi gọi Gemini API: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
